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
