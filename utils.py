import requests
import difflib
from xml.etree import ElementTree as ET
from xml_templates.templates import root, dates, metadata_meta, resource_lineage, distribution_info, identification_info, kw_templates
import uuid
from datetime import datetime
from xml_templates.inspire import inspire_themes_anchors
from thesaurus_utils import keyword_search

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
    camelize(data.topic_category),
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