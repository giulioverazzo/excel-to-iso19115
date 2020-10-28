import requests
import difflib
from xml.etree import ElementTree as ET
from xml_templates.templates import root, dates, metadata_meta, resource_lineage, distribution_info, identification_info, kw_templates
import uuid
from datetime import datetime
from xml_templates.inspire import inspire_themes_anchors

def camelize(string):
  # remove leading and trailing white space
  string = string.strip()

  # lowercase everything
  string = string.lower()

  # Split on all spaces
  string = string.split(" ")

  # capitalize first letter of all except first item
  capitalized = list(map((lambda x: x.capitalize()),string[1:]))

  camelized = string[0]+"".join(capitalized)
  return camelized


def keyword_search(keyword):
  chrono_units = 'https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/chronounits/?format=json'
  instruments = 'https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/instruments/?format=json'
  locations = 'https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/locations/?format=json'
  platforms = 'https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/platforms/?format=json'
  providers = 'https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/providers/?format=json'
  science_keywords = 'https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/sciencekeywords/?format=json'
  
  urls = [chrono_units, instruments, locations, platforms, providers, science_keywords]
  words = []
  for url in urls:
    r = requests.get(url)
    if r.status_code != 200:
      print("ERROR ON: "+url)
      print("Error status code:"+r.status_code)
    else:
      keywords = r.json()['concepts']
      for k_obj in keywords:
        k = k_obj['prefLabel']
        words.append({"word":k, "thesaurus":get_thesaurus_name(url)})
  
  closest = difflib.get_close_matches(keyword.upper(), list(map((lambda x: x['word']),words)))
  if len(closest) != 0:
    k_found = closest[0]
    k_obj = list(filter((lambda x: x['word'].upper() == k_found.upper()),words))[0]
    print(k_obj)
    return k_obj
  else:
    print('No matches found')

def get_thesaurus_name(url):
 return url.split('/')[-2]

def generate_XML(data):

  # dates
  now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
  creationDate = dates['creation'].format(now)
  revisionDate = dates['revision'].format(now)

  # resource lineage
  resourceLineage = resource_lineage['main'].format(data.data_lineage)
  
  # Metadata uuid and linkage
  meta_uuid = uuid.uuid1()
  metadataMeta = metadata_meta['main'].format(meta_uuid)
  
  # distribution info
  transferOptions = ""
  if data.ext_resource != None:
    transferOptions = distribution_info['transfer_option'].format(data.ext_resource)
  
  distributionInfo = distribution_info['main'].format(data.type_of_data, transferOptions)

  # keywords
  keywords = data.keywords.split(",")
  keywordsXML = ""
  for keyword in keywords:
    k_obj = keyword_search(keyword)
    if k_obj != None:
      keywordsXML += kw_templates[k_obj['thesaurus']].format(k_obj['word'])+"\n"
  
  keywordsXML += kw_templates['inspire'].format(inspire_themes_anchors[data.inspire_themes], data.inspire_themes)

  ## Persons ##
  principalInvestigator = ""

  if data.pi_org != None and data.pi_email != None and data.pi_name != None:
    principalInvestigator = identification_info['person'].format("principalInvestigator", data.pi_org, data.pi_email, data.pi_name)
  
  pointOfContact = ""
  if data.poc_org != None and data.poc_email != None and data.poc_name != None:
    pointOfContact = identification_info['person'].format("pointOfContact", data.poc_org, data.poc_email, data.poc_name)
  
  # identification_info
  identificationInfo = identification_info['main'].format(
    data.title,
    meta_uuid,
    data.abstract,
    camelize(data.status),
    principalInvestigator+"\n"+pointOfContact,
    data.topic_category,
    keywordsXML,
    data.project_license,
    data.pnra_project_code,
    data.expedition_number,
    data.other,
    data.begin_date or "",
    data.end_date or ""
  )

  # root
  XMLMetadata = root['main'].format(
    (
      creationDate+"\n"+
      revisionDate+"\n"+ 
      resourceLineage+"\n"+
      metadataMeta+"\n"+
      distributionInfo+"\n"+
      identificationInfo+"\n"
    )
  )

  return XMLMetadata