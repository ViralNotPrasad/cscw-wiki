from os import listdir
from os.path import isfile, join
import json
import pandas as pd
import csv
from matplotlib_venn import venn2
from matplotlib import pyplot as plt

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

def jaccard(main, therest):
    '''
    jaccard computer. takes the list of authors of the
    "main" article and the list of authors of THE REST
    of the articles, however many, and returns the 
    jaccard coefficient
    '''
    common = list(set(main) & set(therest))
    return len(common)/(len(therest)-len(common))

def fname(which, lang):
    '''
    makes the file name we use as index for authors
    '''
    return 'authors_' + which + '_' + lang + '_' + date


def printAuthStats(keys):
    for a in keys:
        # Print language abbrev : number of unique authors
        print(a.split("_")[2], ":", len(authors[a]))


print("KASHMIR CONFLICT - ALL TIME")
print("===number of editors:")
printAuthStats([k for k in authors.keys() if 'kash' in k])
print("===common between english and hindi:")
print(len(list(set(authors['authors_kash_hi_' + date]) & set(authors['authors_kash_en_' + date]))))
print("===common between english and urdu:")
print(len(list(set(authors['authors_kash_en_' + date]) & set(authors['authors_kash_ur_' + date]))))
print("===common between hindi and urdu:")
print(len(list(set(authors['authors_kash_hi_' + date]) & set(authors['authors_kash_ur_' + date]))))

print("ARTICLE 370 - ALL TIME")
print("===number of editors:")
printAuthStats([k for k in authors.keys() if 'article' in k])
print("===common between english and hindi:")
print(len(list(set(authors['authors_article_hi_' + date]) & set(authors['authors_article_en_' + date]))))
print("===common between english and urdu:")
print(len(list(set(authors['authors_article_en_' + date]) & set(authors['authors_article_ur_' + date]))))
print("===common between hindi and urdu:")
print(len(list(set(authors['authors_article_hi_' + date]) & set(authors['authors_article_ur_' + date]))))

print("INSURGENCY - ALL TIME")
print("===number of editors:")
printAuthStats([k for k in authors.keys() if 'insurg' in k])
print("===common between english and hindi:")
print(len(list(set(authors['authors_insurg_hi_' + date]) & set(authors['authors_article_en_' + date]))))
print("===common between english and urdu:")
print(len(list(set(authors['authors_insurg_en_' + date]) & set(authors['authors_article_ur_' + date]))))
print("===common between hindi and urdu:")
print(len(list(set(authors['authors_insurg_hi_' + date]) & set(authors['authors_article_ur_' + date]))))

print("EDITORS IN COMMON BETWEEN ARTICLES IN SAME LANGUAGE")
for lang in ['hi', 'ur', 'en']:
    '''common = list(set(authors['authors_article_' + lang + '_' + date]) & set(authors['authors_kash_' + lang + '_' + date]))
    
    kash = authors['authors_kash_' + lang + '_' + date]
    article = authors['authors_article_' + lang + '_' + date]
    insurg = authors[fname("insurg", lang)]
    if (lang != 'ur'):
        insurg = authors['authors_insurg_' + lang + '_' + date]
    print(lang, len(common), "(", len(common)/len(kash)*100, "% of Kashmir Conflict editors also edited Article 370 )")
    print(lang, len(common), "(", len(common)/len(article)*100, "% of Article 370 editors also edited Kashmir Conflict )")'''
    print("Jaccard: ")
    # Article 370
    print("--<>Article 370")
    if (lang != 'ur'):
        print(lang, ":", jaccard(authors[fname('article', lang)], (authors[fname('insurg', lang)] + authors[fname('kash', lang)])))
    else:
        print(lang, ":", jaccard(authors[fname('article', lang)], authors[fname('kash', lang)]))
    # Kashmir
    print("--<>Kashmir Conflict")
    if (lang != 'ur'):
        print(lang, ":", jaccard(authors[fname('kash', lang)], (authors[fname('insurg', lang)] + authors[fname('article', lang)])))
    else:
        print(lang, ":", jaccard(authors[fname('kash', lang)], authors[fname('article', lang)]))
    if (lang != 'ur'):
        print("--<>Insurgency in Jammu and Kashmir")
        print(lang, ":", jaccard(authors[fname('insurg', lang)], (authors[fname('kash', lang)] + authors[fname('article', lang)])))
    
    print("===end===")


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
