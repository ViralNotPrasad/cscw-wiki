#!/usr/bin/python3

"""
    get_pages_revisions.py

    MediaWiki API Demos
    Demo of `Revisions` module: Get revision data with content for pages
    with titles [[API]] and [[Main Page]]

    MIT License
"""

import pprint
import requests
from datetime import datetime
import json

#============ file saving ===========

def pageOps(fname, revisions):
    # Get unique authors for this page
    authors = []
    for rev in revisions:
        if "user" in rev:
            authors.append(rev["user"]) 
        elif "userhidden" in rev:
            authors.append("anon")
        else:
            print ("strange format: " + str(rev))
        authors = list(set(authors))

    #save to files
    with open("../data/authors_" + fname + "_" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".csv", "w+") as file:
        for author in authors:
            file.write(author + "\n")
    # Write revision data to file
    with open("../data/rev_" + fname + "_" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".json", "w+") as file:
            json.dump(revisions, file)
    print(fname, "# revisions", len(revisions))


#============ request parameters ===========

GLOBAL_PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "",
    "rvprop": "timestamp|user|comment|size",  # append content if you want the contents but it will take forever to run
    "rvslots": "main",
    "formatversion": "2",
    "format": "json",
    "rvlimit": "500" 
}

# XX_URL - url for XX lang
# XX_DICT - mapping from filename to "title" parameter value

EN_URL = "https://en.wikipedia.org/w/api.php"
EN_DICT = { 
    "kash_en": "Kashmir conflict", 
    "article_en": "Article 370 of the Constitution of India", 
    "insurg_en": "Insurgency in Jammu and Kashmir" 
}

HI_URL = "https://hi.wikipedia.org/w/api.php"
HI_DICT = {
    "kash_hi": "कश्मीर_विवाद", #Kashmir conflict
    "article_hi": "अनुच्छेद_३७०", #Article 370
    "insurg_hi": "जम्मू_और_कश्मीर_में_विद्रोह" # Insurgency in Jammu and Kashmir 
}

UR_URL = "https://ur.wikipedia.org/w/api.php"
UR_DICT = {
    "kash_ur": "مسئلہ_کشمیر", #Kashmir conflict
    "article_ur": "آئین_ہند_کی_دفعہ_370", #Article 370 
}

# final sanity mapping, XX url to XX dict
EN = { EN_URL:EN_DICT }
HI = { HI_URL:HI_DICT }
UR = { UR_URL:UR_DICT }


#============ revision history request ===========

S = requests.Session()
#pp = pprint.PrettyPrinter(indent=2)

#pp.pprint([EN, HI, UR])
for LANG in [EN, HI, UR]:
    #pp.pprint(LANG)
    for LANG_URL in LANG:
        LANG_DICT = LANG[LANG_URL]
        for fname in LANG_DICT:
            ARTICLE_URL = LANG_DICT[fname]
            # point to correct lang-specific article, reset rvcontinue
            GLOBAL_PARAMS["titles"] = ARTICLE_URL
            if "rvcontinue" in GLOBAL_PARAMS:
                del GLOBAL_PARAMS["rvcontinue"]

            # first request, variable init befor loop
            R = S.get(url=LANG_URL, params=GLOBAL_PARAMS)
            DATA = R.json()
            revisions = DATA["query"]["pages"][0]["revisions"]
            print(len(revisions))

            # if total > rvlimit, API will chunk it and offer "continue" param
            # which just needs to be added to the next request
            while True:
                if "continue" in DATA:
                    print(DATA["continue"])
                    GLOBAL_PARAMS["rvcontinue"] = DATA["continue"]["rvcontinue"]
                    R = S.get(url=LANG_URL, params=GLOBAL_PARAMS)
                    DATA = R.json()
                    newrevs = DATA["query"]["pages"][0]["revisions"]
                    print(len(newrevs))
                    revisions += newrevs
                else:
                    print("==============END==============")
                    break

            pageOps(fname, revisions)
