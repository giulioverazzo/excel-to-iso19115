import csv, json, difflib

def read_csv_thesaurus(filename):
  thesaurus_name = filename.split("/")[-1].split(".")[0]
  with open(filename, mode='r', encoding='utf-8') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      
      words = []
      for row in csv_reader:
        k = row['Related Descriptor']
        words.append({"word":k, "thesaurus":thesaurus_name})
      
      return words

def read_json_thesaurus(filename):
  thesaurus_name = filename.split("/")[-1].split(".")[0]
  f = open(filename,)
  data = json.load(f)
  keywords = data['concepts']

  words = []
  for k_obj in keywords:
    k = k_obj['prefLabel']
    words.append({"word":k, "thesaurus":thesaurus_name})

  f.close()
  return words

def keyword_search(keyword):
  chrono_units = 'thesaurus/chronounits.json'
  instruments = 'thesaurus/instruments.json'
  locations = 'thesaurus/locations.json'
  platforms = 'thesaurus/platforms.json'
  providers = 'thesaurus/providers.json'
  science_keywords = 'thesaurus/sciencekeywords.json'
  
  filenames = [chrono_units, instruments, locations, platforms, providers, science_keywords]
  words = []

  for f in filenames:
    words.extend(read_json_thesaurus(f))
  
  nasa = 'thesaurus/nasa.csv'
  words.extend(read_csv_thesaurus(nasa))
  
  closest = difflib.get_close_matches(keyword.upper(), list(map((lambda x: x['word'].upper()),words)))
  if len(closest) != 0:
    k_found = closest[0]
    k_obj = list(filter((lambda x: x['word'].upper() == k_found.upper()),words))[0]
    print(k_obj)
    return k_obj
  else:
    print('No matches found') 
