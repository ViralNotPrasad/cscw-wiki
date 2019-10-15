#!/usr/bin/python3

"""
    get_pages_revisions.py

    MediaWiki API Demos
    Demo of `Revisions` module: Get revision data with content for pages
    with titles [[API]] and [[Main Page]]

    MIT License
"""

import requests
from datetime import datetime

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

KASH_EN_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "Kashmir conflict",
    "rvprop": "timestamp|user|comment", # there's more could add like content
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying
}

ARTICLE_EN_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "Article 370 of the Constitution of India",
    "rvprop": "timestamp|user|comment", # there's more could add like content
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying
}

INSURG_EN_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "Insurgency in Jammu and Kashmir",
    "rvprop": "timestamp|user|comment", # there's more could add like content
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying   
}

EN_DICT = {"kash_en": KASH_EN_PARAMS, "article_en": ARTICLE_EN_PARAMS, "insurg_en": INSURG_EN_PARAMS}

for fname, params in EN_DICT.items():
    R = S.get(url=URL, params=params)
    DATA = R.json()

    PAGES = DATA["query"]["pages"]

    for page in PAGES:
        print(page)
        #print(page["revisions"])
        with open("../data/rev_" + fname + "_" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".txt", "w+") as file:
                file.write(str(page["revisions"]))


#====================HINDI====================

URL = "https://hi.wikipedia.org/w/api.php"

KASH_HI_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "कश्मीर_विवाद", #Kashmir conflict
    "rvprop": "timestamp|user|comment", # there's more could add like content
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying   
}

ARTICLE_HI_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "अनुच्छेद_३७०", #Article 370
    "rvprop": "timestamp|user|comment", # there's more could add like content
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying      
}

INSURG_HI_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "जम्मू_और_कश्मीर_में",
    "rvprop": "timestamp|user|comment", # there's more could add like content
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying      
}

HI_DICT = {"kash_hi": KASH_HI_PARAMS, "article_hi": ARTICLE_HI_PARAMS, "insurg_hi": INSURG_HI_PARAMS}

for fname, params in HI_DICT.items():
    R = S.get(url=URL, params=params)
    DATA = R.json()

    PAGES = DATA["query"]["pages"]

    for page in PAGES:
        print(page)
        #print(page["revisions"])
        with open("../data/rev_" + fname + "_" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".txt", "w+") as file:
                file.write(str(page["revisions"]))

#====================URDU====================

URL = "https://ur.wikipedia.org/w/api.php"

KASH_UR_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "مسئلہ_کشمیر", #Kashmir conflict
    "rvprop": "timestamp|user|comment", # there's more could add like content
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying   
}

ARTICLE_UR_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "آئین_ہند_کی_دفعہ_370", #Article 370
    "rvprop": "timestamp|user|comment", # there's more could add like content
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying      
}

UR_DICT = {"kash_ur": KASH_UR_PARAMS, "article_ur": ARTICLE_UR_PARAMS}

for fname, params in UR_DICT.items():
    R = S.get(url=URL, params=params)
    DATA = R.json()

    PAGES = DATA["query"]["pages"]

    for page in PAGES:
        print(page)
        #print(page["revisions"])
        with open("../data/rev_" + fname + "_" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".txt", "w+") as file:
                file.write(str(page["revisions"]))