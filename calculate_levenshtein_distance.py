# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 13:09:27 2022

@author: Elena
"""

# calculating Levenshtein distance ratio between original and predicted relation
# input: the results of the language model in json
# output: csv file with the original and predicted results and the levenshtein ratio between the two 

import json
from fuzzywuzzy import fuzz
import pandas as pd


# enter path to language models' results in json 
with open("path to language model results in json", "r", encoding="utf-8") as i:
    test = json.load(i)
    
    
all_rels = {'P495': ['country of origin',
  'place of origin',
  'comes from',
  'origin (country)',
  'originates',
  'CoO'],
 'P1412': ['languages spoken, written or signed',
  'languages spoken',
  'language spoken',
  'language of expression',
  'languages of expression',
  'languages signed',
  'language signed',
  'language written',
  'language read',
  'language used',
  'language',
  'speaks language',
  'writes language',
  'signs language',
  'uses language',
  'wrote language',
  'spoke language',
  'used language',
  'signed language',
  'second language',
  'languages spoken, written, or signed',
  'language(s) spoken, written or signed'],
 'P39': ['position held',
  'political office held',
  'political seat',
  'public office',
  'office held',
  'position occupied',
  'holds position'],
 'P105': ['taxon rank', 'taxonomic rank', 'rank', 'type of taxon'],
 'P171': ['parent taxon', 'taxon parent', 'higher taxon'],
 'P137': ['operator',
  'service operator',
  'facility operator',
  'operated by',
  'managed by',
  'administrator',
  'item operator',
  'user'],
 'P31': ['instance of',
  'is a',
  'is an',
  'has class',
  'has type',
  'is a particular',
  'is a specific',
  'is an individual',
  'is a unique',
  'is an example of',
  'member of',
  'unique individual of',
  'distinct member of',
  'non-type member of',
  'unsubclassable example of',
  'uninstantiable instance of',
  'unsubclassifiable member of',
  'not a type but is instance of',
  'unsubtypable particular',
  'unitary element of class',
  'distinct element of',
  'distinct individual member of',
  'occurrence of',
  'rdf:type',
  'type'],
 'P159': ['headquarters location',
  'head office location',
  'HQ',
  'garrison',
  'admin HQ',
  'seat',
  'principle office',
  'headquarters',
  'head quarters',
  'HQ location',
  'based in'],
 'P27': ['country of citizenship',
  'citizen of',
  'national of',
  'subject of (country)',
  'citizenship',
  'nationality'],
 'P3005': ['valid in place',
  'applies to location',
  'valid in location',
  'applies to place',
  'country',
  'true in',
  'valid in territory'],
 'P17': ['country', 'sovereign state', 'state', 'land', 'host country'],
 'P735': ['given name',
  'forename',
  'first name',
  'personal name',
  'middle name',
  'Christian name'],
 'P131': ['located in the administrative territorial entity',
  'located in the administrative unit',
  'located in administrative unit',
  'is in administrative unit',
  'is located in',
  'is in the state of',
  'is in the province of',
  'is in the county of',
  'is in the district of',
  'is in the department of',
  'is in the region of',
  'is in the borough of',
  'is in the city of',
  'is in the town of',
  'is in the village of',
  'is in the municipality of',
  'is in the territory of',
  'is in the prefecture of',
  'is in the voivodeship of',
  'is in the Indian reservation of',
  'is in the Indian reserve of',
  'is in the ward of',
  'is in the administrative region of',
  'is in the settlement of',
  'is in the local government area of',
  'is in the rural city of',
  'is in the shire of',
  'happens in',
  'is in the commune of',
  'in administrative unit',
  'in',
  'is in the administrative unit',
  'administrative territorial entity',
  'city',
  'town',
  'state',
  'Indian reservation',
  'in the administrative unit',
  'locality',
  'is in the parish of',
  'location (administrative territorial entity)',
  'is in the principal area of',
  'based in',
  'located in the administrative territorial entity',
  'located in the territorial entity',
  'region',
  'is in the arrondissement of'],
 'P404': ['game mode', 'mode', 'gameplay'],
 'P3450': ['sports season of league or competition',
  'is season of',
  'is a season of',
  'seasons of',
  'season of',
  'season of sports competition',
  'season of sports tournament',
  'season of sports league',
  'sport season'],
 'P413': ['position played on team / speciality',
  'player position',
  'fielding position',
  'specialism',
  'position (on team)',
  'speciality'],
 'P118': ['league', 'division', 'sports league'],
 'P19': ['place of birth',
  'birthplace',
  'born in',
  'POB',
  'birth place',
  'location born',
  'born at',
  'birth location',
  'location of birth',
  'birth city'],
 'P69': ['educated at',
  'alma mater',
  'education',
  'alumni of',
  'alumnus of',
  'alumna of',
  'college attended',
  'university attended',
  'school attended',
  'studied at',
  'graduate of',
  'graduated from',
  'faculty'],
 'P58': ['screenwriter',
  'scriptwriter',
  'screenplay by',
  'teleplay by',
  'writer (of screenplays)',
  'film script by',
  'written by'],
 'P734': ['family name', 'last name', 'has surname', 'surname'],
 'P155': ['follows',
  'succeeds to',
  'previous is',
  'before was',
  'predecessor',
  'preceded by',
  'prequel is',
  'sequel of',
  'split from',
  'comes after',
  'successor to'],
 'P344': ['director of photography',
  'cinematographer',
  'DOP',
  'Cinematography'],
 'P1313': ['office held by head of government',
  'office of head of government',
  'position of head of government',
  'position held by head of government',
  'title of head of government'],
 'P106': ['occupation',
  'profession',
  'job',
  'work',
  'career',
  'employment',
  'craft'],
 'P54': ['member of sports team',
  'member of team',
  'team',
  'team played for',
  'played for',
  'plays for',
  'teams played for',
  'of team',
  'club played for',
  'player of',
  'part of team'],
 'P641': ['sport', 'sports', 'sport played', 'play', 'plays'],
 'P47': ['shares border with',
  'borders',
  'bordered by',
  'adjacent to',
  'next to',
  'border'],
 'P20': ['place of death',
  'deathplace',
  'died in',
  'death place',
  'POD',
  'location of death',
  'death location'],
 'P279': ['subclass of',
  'rdfs:subClassOf',
  'hyponym of',
  'has superclass',
  'is also a',
  'subtype of',
  'is a subtype of',
  'subcategory of',
  'is a category of',
  'is thereby also a',
  'is necessarily also a',
  'whose instances are among',
  'whose instances ⊆ those of',
  '⊆',
  '⊂',
  'is a type of',
  'is a class of',
  'subset of',
  'type of',
  'form of'],
 'P264': ['record label', 'label'],
 'P161': ['cast member',
  'starring',
  'film starring',
  'actor',
  'actress',
  'contestant or a play'],
 'P156': ['followed by',
  'prequel of',
  'succeded by',
  'next is',
  'precedes',
  'sequel is',
  'successor',
  'preceeds',
  'comes before'],
 'P375': ['space launch vehicle',
  'carrier rocket',
  'launch vehicle',
  'Rocket used'],
 'P1877': ['after a work by',
  'copy of a work by',
  'artist who inspired this',
  'inspiring artist',
  'inspirational artist'],
 'P3373': ['sibling',
  'brother',
  'sister',
  'has sister',
  'bro',
  'has brother',
  'brother or sister',
  'sister or brother',
  'sis',
  'sib'],
 'P138': ['named after',
  'eponym',
  'named for',
  'namesake',
  'etymology',
  'toponym',
  'name after'],
 'P407': ['language of work or name',
  'broadcasting language',
  'audio language',
  'available in',
  'language of work',
  'language of the reference',
  'language of website',
  'language of URL',
  'used language',
  'language of the name',
  'language of name',
  'language of spoken text',
  'named in language'],
 'P509': ['cause of death',
  'method of murder',
  'death cause',
  'die from',
  'murder method',
  'die of'],
 'P749': ['parent organization',
  'owned by (company or organization)',
  'subsidiary of',
  'parent company',
  'parent organisation',
  'owned by (company or organisation)',
  'holding',
  'holding company',
  'part of',
  'parent unit',
  'parent agency',
  'superior formation'],
 'P361': ['part of',
  'meronym of',
  'section of',
  'system of',
  'subsystem of',
  'subassembly of',
  'merged into',
  'contained within',
  'assembly of',
  'part of-property',
  'merged with',
  'component of',
  'in',
  'within',
  'is part of'],
 'P421': ['located in time zone', 'timezone', 'time zone', 'time'],
 'P166': ['award received',
  'prize received',
  'awards',
  'honorary title',
  'recognition title',
  'award',
  'honours',
  'honors',
  'medals',
  'awarded',
  'award won',
  'prize awarded',
  'awards received',
  'win',
  'winner of'],
 'P135': ['movement', 'school', 'trend']}   


rel_res = []
counter = 1


for item in test:
    
    for key, value in all_rels.items():
        if item["original_r"] in value:
            rels = value

    
    len_org = len(item["original_r"])
    len_pred = len(item["predicted_r"])
    
    len_diff = len_org - len_pred
    
    name = 'r' + '_' + str(counter)
    
    name  = {
        'original': item["original_r"],
        'predicted': item["predicted_r"],
        'fuzzwuzz_ratio': []
    }
    
    for rel in rels:
        similarity = fuzz.ratio(item["predicted_r"].lower().strip(), rel.lower().strip())
        new_dict = {
            rel: similarity
            }
        
        name['fuzzwuzz_ratio'].append(new_dict)
        
    rel_res.append(name)
    
    
results = []
  
for item in rel_res:
    
    ground_truth_score = []
    pred = item['predicted']
    
            
    for element in item['fuzzwuzz_ratio']:
        for key, value in element.items():
            results.append([key.strip(), pred.strip(), value])
            
    

print(results[0])
df = pd.DataFrame(results, columns = ['orig', 'pred', 'fuzzwuzz_score'])   

print(df.describe())

df.to_csv("output path for pandas file") # enter output path for pandas df  

















 