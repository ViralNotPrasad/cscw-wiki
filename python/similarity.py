from os import listdir
from os.path import isfile, join
import json
import pandas as pd
import csv
import matplotlib
from matplotlib_venn import venn2
from matplotlib import pyplot as plt
matplotlib.use('nbAgg')

date = '15-05-2020'

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
        
        
def crossLanguage(lang1, lang2, authors):
    '''
    Hastily written cross-language Jaccard method
    '''
    lang1keys = [k for k in authors.keys() if ('_' + lang1 + '_' in k) ]
    lang2keys = [k for k in authors.keys() if ('_' + lang2 + '_' in k) ]
    sets1List = []
    sets2List = []
    for key in lang1keys:
        sets1List.append(authors[key])
    for key in lang2keys:
        sets2List.append(authors[key])
    set1 = set(sets1List[0])
    for i in range(1,len(sets1List)):
        set1 = set1 | set(sets1List[i])
    set2 = set(sets2List[0])
    for i in range(1,len(sets2List)):
        set2 = set2 | set(sets2List[i])
        
    venn2([set1, set2], (lang1, lang2))
    plt.savefig(lang1 + '_' + lang2 + '_venn.png')
    plt.clf()


crossLanguage('en', 'hi', authors)
crossLanguage('en', 'ur', authors)
crossLanguage('hi', 'ur', authors)
    


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

venn_ur = venn2([set(authors['authors_article_ur_' + date]), set(authors['authors_kash_ur_' + date] \
                 + authors['authors_pulwama_ur_' + date] + authors['authors_reorg_ur_' + date])], ('Urdu Article 370', 'The Rest'))
plt.savefig('Urdu_authors_article370.png')
plt.clf()

venn_hi = venn2([set(authors['authors_article_hi_' + date]), set(authors['authors_kash_hi_' + date] \
                 + authors['authors_pulwama_hi_' + date] + authors['authors_reorg_hi_' + date] + authors['authors_insurg_hi_' + date])], ('Hindi Article 370', 'The Rest'))
plt.savefig('Hindi_authors_article370.png')
plt.clf()

venn_en = venn2([set(authors['authors_article_en_' + date]), set(authors['authors_kash_en_' + date] \
                 + authors['authors_pulwama_en_' + date] + authors['authors_reorg_en_' + date] + authors['authors_insurg_en_' + date])], ('English Article 370', 'The Rest'))
plt.savefig('English_authors_article370.png')
plt.clf()



venn_ur = venn2([set(authors['authors_kash_ur_' + date]), set(authors['authors_article_ur_' + date] \
                 + authors['authors_pulwama_ur_' + date] + authors['authors_reorg_ur_' + date])], ('Urdu Kashmir Conflict', 'The Rest'))
plt.savefig('Urdu_authors_kashmir.png')
plt.clf()

venn_hi = venn2([set(authors['authors_kash_hi_' + date]), set(authors['authors_article_hi_' + date] \
                 + authors['authors_pulwama_hi_' + date] + authors['authors_reorg_hi_' + date] + authors['authors_insurg_hi_' + date])], ('Hindi Kashmir conflict', 'The Rest'))
plt.savefig('Hindi_authors_kashmir.png')
plt.clf()

venn_en = venn2([set(authors['authors_kash_en_' + date]), set(authors['authors_article_en_' + date] \
                 + authors['authors_pulwama_en_' + date] + authors['authors_reorg_en_' + date] + authors['authors_insurg_en_' + date])], ('English Kashmir Conflict', 'The Rest'))
plt.savefig('English_authors_kashmir.png')
plt.clf()



venn_ur = venn2([set(authors['authors_reorg_ur_' + date]), set(authors['authors_article_ur_' + date] \
                 + authors['authors_pulwama_ur_' + date] + authors['authors_kash_ur_' + date])], ('Urdu Reorganization Act', 'The Rest'))
plt.savefig('Urdu_authors_reorg.png')
plt.clf()

venn_hi = venn2([set(authors['authors_reorg_hi_' + date]), set(authors['authors_article_hi_' + date] \
                 + authors['authors_pulwama_hi_' + date] + authors['authors_kash_hi_' + date] + authors['authors_insurg_hi_' + date])], ('Hindi Reorganization Act', 'The Rest'))
plt.savefig('Hindi_authors_reorg.png')
plt.clf()

venn_en = venn2([set(authors['authors_reorg_en_' + date]), set(authors['authors_article_en_' + date] \
                 + authors['authors_pulwama_en_' + date] + authors['authors_kash_en_' + date] + authors['authors_insurg_en_' + date])], ('English Reorganization Act', 'The Rest'))
plt.savefig('English_authors_reorg.png')
plt.clf()




venn_ur = venn2([set(authors['authors_pulwama_ur_' + date]), set(authors['authors_article_ur_' + date] \
                 + authors['authors_reorg_ur_' + date] + authors['authors_kash_ur_' + date])], ('Urdu Pulwama', 'The Rest'))
plt.savefig('Urdu_authors_pulwama.png')
plt.clf()

venn_hi = venn2([set(authors['authors_pulwama_hi_' + date]), set(authors['authors_article_hi_' + date] \
                 + authors['authors_reorg_hi_' + date] + authors['authors_kash_hi_' + date] + authors['authors_insurg_hi_' + date])], ('Hindi Pulwama', 'The Rest'))
plt.savefig('Hindi_authors_pulwama.png')
plt.clf()

venn_en = venn2([set(authors['authors_pulwama_en_' + date]), set(authors['authors_article_en_' + date] \
                 + authors['authors_reorg_en_' + date] + authors['authors_kash_en_' + date] + authors['authors_insurg_en_' + date])], ('English Pulwama', 'The Rest'))
plt.savefig('English_authors_pulwama.png')
plt.clf()


'''
venn_hi = venn2([set(authors['authors_insurg_hi_' + date]), set(authors['authors_article_hi_' + date] \
                 + authors['authors_reorg_hi_' + date] + authors['authors_kash_hi_' + date] + authors['authors_pulwama_hi_' + date])], ('Hindi Article 370', 'The Rest'))
plt.savefig('Hindi_authors_insurg.png')
plt.clf()

venn_en = venn2([set(authors['authors_insurg_en_' + date]), set(authors['authors_article_en_' + date] \
                 + authors['authors_reorg_en_' + date] + authors['authors_kash_en_' + date] + authors['authors_pulwama_en_' + date])], ('English Article 370', 'English Kashmir Conflict'))
plt.savefig('English_authors_insurg.png')
plt.clf()
'''