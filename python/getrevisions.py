#!/usr/bin/python3

"""
    get_pages_revisions.py

    MediaWiki API Demos
    Demo of `Revisions` module: Get revision data with content for pages
    with titles [[API]] and [[Main Page]]

    MIT License
"""

import json
import pdb
import requests
from datetime import datetime

def pageOps(fname):
    # Get unique authors for this page
    authors = []
    #print("=========" + page["eicontinue"])
    for rev in page["revisions"]:
        if rev["user"] not in authors:
            authors.append(rev["user"]) 
            #pdb.set_trace()
    with open("../data/authors_" + fname + "_" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".csv", "w+") as file:
        for author in authors:
            file.write(author + "\n")
    # Write revision data to file
    with open("../data/rev_" + fname + "_" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".json", "w+") as file:
            json.dump(page["revisions"], file)
    print(fname, "# revisions", len(page['revisions']))        

#======ENGLISH======

properties = "timestamp|user|comment|size|ids"

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

KASH_EN_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "Kashmir conflict",
    "rvprop": properties,  
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying
}

ARTICLE_EN_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "Article 370 of the Constitution of India",
    "rvprop": properties,  
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying
}

INSURG_EN_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "Insurgency in Jammu and Kashmir",
    "rvprop": properties,  
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying   
}

REORG_EN_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "Jammu and Kashmir Reorganisation Act, 2019",
    "rvprop": properties,  
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying   
}

PULWAMA_EN_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "2019 Pulwama attack",
    "rvprop": properties,  
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying   
}

EN_DICT = {"kash_en": KASH_EN_PARAMS, "article_en": ARTICLE_EN_PARAMS, "insurg_en": INSURG_EN_PARAMS, "reorg_en": REORG_EN_PARAMS, "pulwama_en": PULWAMA_EN_PARAMS}

for fname, params in EN_DICT.items():
    R = S.get(url=URL, params=params)
    DATA = R.json()

    PAGES = DATA["query"]["pages"]

    for page in PAGES:
        pageOps(fname)

#====================HINDI====================

URL = "https://hi.wikipedia.org/w/api.php"

KASH_HI_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "कश्मीर_विवाद", #Kashmir conflict
    "rvprop": properties, 
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying   
}

ARTICLE_HI_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "अनुच्छेद_३७०", #Article 370
    "rvprop": properties,  
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying      
}

INSURG_HI_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "जम्मू_और_कश्मीर_में_विद्रोह", # Insurgency in Jammu and Kashmir
    "rvprop": properties,  
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying      
}

REORG_HI_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "जम्मू_और_कश्मीर_पुनर्गठन_अधिनियम,_2019", # Reorganisation act
    "rvprop": properties,  
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying      
}

PULWAMA_HI_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "२०१९_पुलवामा_हमला", # Pulwama Attack
    "rvprop": properties,  
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying      
}



HI_DICT = {"kash_hi": KASH_HI_PARAMS, "article_hi": ARTICLE_HI_PARAMS, "insurg_hi": INSURG_HI_PARAMS, "pulwama_hi": PULWAMA_HI_PARAMS, "reorg_hi" : REORG_HI_PARAMS}

for fname, params in HI_DICT.items():
    R = S.get(url=URL, params=params)
    DATA = R.json()

    PAGES = DATA["query"]["pages"]

    for page in PAGES:
        pageOps(fname)

#====================URDU====================

URL = "https://ur.wikipedia.org/w/api.php"

KASH_UR_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "مسئلہ_کشمیر", #Kashmir conflict
    "rvprop": properties,  
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying   
}

ARTICLE_UR_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "آئین_ہند_کی_دفعہ_370", #Article 370
    "rvprop": properties,  
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying      
}

REORG_UR_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "جموں_و_کشمیر_تنظیم_نو_ایکٹ،_2019ء", #Reorganization
    "rvprop": properties,  
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying      
}

PULWAMA_UR_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "پلوامہ_حملہ،_2019ء", #Pulwama Attack
    "rvprop": properties,  
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying      
}

UR_DICT = {"kash_ur": KASH_UR_PARAMS, "article_ur": ARTICLE_UR_PARAMS, "reorg_ur": REORG_UR_PARAMS, "pulwama_ur": PULWAMA_UR_PARAMS}

for fname, params in UR_DICT.items():
    R = S.get(url=URL, params=params)
    DATA = R.json()

    PAGES = DATA["query"]["pages"]

    for page in PAGES:
        pageOps(fname)
               