from os import listdir
from os.path import isfile, join
import json
import pandas as pd
import csv

def makeDict(mypath):
    thefiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    mydict = {}
    for file in thefiles:
        with open(mypath + file) as thefile:
            if file.split(".")[1] == "json":
                data = json.load(thefile) 
                mydict[file.split(" ")[0]] = pd.DataFrame(data)
            elif file.split(".")[1] == "csv":
                data = thefile.readlines()
                mydict[file.split(" ")[0]] = data
            else:
                print("wrong file type: " + file.split(".")[1])
    return mydict  

# Read data from the revisions files
revs = makeDict("../data/revisions/")

# Read data from the authors files
authors = makeDict("../data/editors/")

# Stripping newlines
for article, data in authors.items():
    newdata = []
    for a in data:
        newdata.append(a.rstrip('\n'))
    authors[article] = newdata

'''keys ['authors_article_en_17-10-2019', 
'authors_article_hi_17-10-2019', 
'authors_article_ur_17-10-2019', 
'authors_insurg_en_17-10-2019', 
'authors_kash_en_17-10-2019', 
'authors_kash_hi_17-10-2019', 
'authors_kash_ur_17-10-2019']
'''

def printAuthStats(keys):
    for a in keys:
        # Print language abbrev : number of unique authors
        print(a.split("_")[2], ":", len(authors[a]))

print("KASHMIR CONFLICT - LAST 500 EDITS OF EACH PAGE")
print("===number of editors:")
printAuthStats([k for k in authors.keys() if 'kash' in k])
print("===common between english and hindi:")
print(len(list(set(authors['authors_kash_hi_17-10-2019']) & set(authors['authors_kash_en_17-10-2019']))))
print("===common between english and urdu:")
print(len(list(set(authors['authors_kash_en_17-10-2019']) & set(authors['authors_kash_ur_17-10-2019']))))
print("===common between hindi and urdu:")
print(len(list(set(authors['authors_kash_hi_17-10-2019']) & set(authors['authors_kash_ur_17-10-2019']))))

print("ARTICLE 370 - LAST 500 EDITS OF EACH PAGE")
print("===number of editors:")
printAuthStats([k for k in authors.keys() if 'article' in k])
print("===common between english and hindi:")
print(len(list(set(authors['authors_article_hi_17-10-2019']) & set(authors['authors_article_en_17-10-2019']))))
print("===common between english and urdu:")
print(len(list(set(authors['authors_article_en_17-10-2019']) & set(authors['authors_article_ur_17-10-2019']))))
print("===common between hindi and urdu:")
print(len(list(set(authors['authors_article_hi_17-10-2019']) & set(authors['authors_article_ur_17-10-2019']))))

print("EDITORS IN COMMON BETWEEN ARTICLES IN SAME LANGUAGE")
for lang in ['hi', 'ur', 'en']:
    common = list(set(authors['authors_article_' + lang + '_17-10-2019']) & set(authors['authors_kash_' + lang + '_17-10-2019']))
    kash = authors['authors_kash_' + lang + '_17-10-2019']
    article = authors['authors_article_' + lang + '_17-10-2019']
    print(lang, len(common), "(", len(common)/len(kash)*100, "% of Kashmir Conflict editors also edited Article 370 )")
    print(lang, len(common), "(", len(common)/len(article)*100, "% of Article 370 editors also edited Kashmir Conflict )")


