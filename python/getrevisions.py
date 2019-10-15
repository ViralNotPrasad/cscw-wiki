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

PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "Kashmir conflict",
    "rvprop": "timestamp|user|comment", # there's more could add like content
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" # Cap at 500 queries which is annoying
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

for page in PAGES:
    print(page["revisions"])
    with open("rev_kash_en_" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".txt", "w+") as file:
            file.write(str(page["revisions"]))