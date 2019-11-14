from os import listdir
from os.path import isfile, join
import json
import pandas as pd
import csv
from matplotlib_venn import venn2
from matplotlib import pyplot as plt
import regex as re

date = '29-10-2019'

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

def printAuthStats(keys):
    for a in keys:
        # Print language abbrev : number of unique authors
        print(a.split("_")[2], ":", len(authors[a]))

print("KASHMIR CONFLICT - ALL TIME EDITS OF EACH PAGE")
print("===number of editors:")
printAuthStats([k for k in authors.keys() if 'kash' in k])
print("===common between english and hindi:")
print(len(list(set(authors['authors_kash_hi_' + date]) & set(authors['authors_kash_en_' + date]))))
print("===common between english and urdu:")
print(len(list(set(authors['authors_kash_en_' + date]) & set(authors['authors_kash_ur_' + date]))))
print("===common between hindi and urdu:")
print(len(list(set(authors['authors_kash_hi_' + date]) & set(authors['authors_kash_ur_' + date]))))

print("ARTICLE 370 - ALL TIME EDITS OF EACH PAGE")
print("===number of editors:")
printAuthStats([k for k in authors.keys() if 'article' in k])
print("===common between english and hindi:")
print(len(list(set(authors['authors_article_hi_' + date]) & set(authors['authors_article_en_' + date]))))
print("===common between english and urdu:")
print(len(list(set(authors['authors_article_en_' + date]) & set(authors['authors_article_ur_' + date]))))
print("===common between hindi and urdu:")
print(len(list(set(authors['authors_article_hi_' + date]) & set(authors['authors_article_ur_' + date]))))

print("EDITORS IN COMMON BETWEEN ARTICLES IN SAME LANGUAGE")
for lang in ['hi', 'ur', 'en']:
    common = list(set(authors['authors_article_' + lang + '_' + date]) & set(authors['authors_kash_' + lang + '_' + date]))
    kash = authors['authors_kash_' + lang + '_' + date]
    article = authors['authors_article_' + lang + '_' + date]
    print("======jaccard======")
    print(lang, len(common), "\t", len(common)/(len(kash)+len(article)-len(common)))
    print("========old========") 
    print(lang, len(common), "(", len(common)/len(kash)*100, "% of Kashmir Conflict editors also edited Article 370 )")
    print(lang, len(common), "(", len(common)/len(article)*100, "% of Article 370 editors also edited Kashmir Conflict )")


# Venn diagrams

venn_ur = venn2([set(authors['authors_article_ur_' + date]), set(authors['authors_kash_ur_' + date])], ('Urdu Article 370', 'Urdu Kashmir Conflict'))
plt.savefig('Urdu_authors.png')
plt.clf()

venn_hi = venn2([set(authors['authors_article_hi_' + date]), set(authors['authors_kash_hi_' + date])], ('Hindi Article 370', 'Hindi Kashmir Conflict'))
plt.savefig('Hindi_authors.png')
plt.clf()

venn_en = venn2([set(authors['authors_article_en_' + date]), set(authors['authors_kash_en_' + date])], ('English Article 370', 'English Kashmir Conflict'))
plt.savefig('English_authors.png')
plt.clf()


# Kashmir IP address 

count_en = 0
print("% IP addresses editing")
for author in authors['authors_kash_en_' + date]:
    if (re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", author) != None):
        count_en += 1
print("English: ", count_en / 1577)

count_ur = 0
for author in authors['authors_kash_ur_' + date]:
    if (re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", author) != None):
        count_ur += 1
print("Urdu: ", count_ur / 17)

count_hi = 0
for author in authors['authors_kash_hi_' + date]:
    if (re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", author) != None):
        count_hi += 1
print("Hindi: ", count_hi / 51)