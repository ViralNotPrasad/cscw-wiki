import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join
from matplotlib_venn import venn3
from matplotlib import pyplot as plt

file = pd.read_excel("../data/editors/wikiwho copy paste/Kashmir_Conflict_Hindi.xlsx")

def makeDict(mypath):
    thefiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    mydict = {}
    for file in thefiles:
        if (file.split(".")[1] == "xlsx"):
            data = pd.read_excel(mypath + file)
            mydict[file.split(".")[0]] = data
    return mydict  

data = makeDict("../data/editors/wikiwho copy paste/")

editors = {}

# Kashmir Venns

for e in ['Hindi', 'English', 'Urdu']:
    arr = np.array(data['Kashmir_Conflict_' + e]['Username'])
    for i in range(len(arr)):
        arr[i] = str(arr[i])
    editors[e] = np.unique(arr)

venn_kash = venn3([set(editors['Hindi']), set(editors['English']), set(editors['Urdu'])], ('Hindi', 'English', 'Urdu'))
plt.title("Unique Kashmir Conflict Page Editors")
plt.savefig('Kashmir_page_wikiwho_editors_venn.png')
plt.clf()

# Article 370 Venns

for e in ['Hindi', 'English', 'Urdu']:
    arr = np.array(data['Article_370_' + e]['Username'])
    for i in range(len(arr)):
        arr[i] = str(arr[i])
    editors[e] = np.unique(arr)

venn_370 = venn3([set(editors['Hindi']), set(editors['English']), set(editors['Urdu'])], ('Hindi', 'English', 'Urdu'))
plt.title("Unique Article 370 Page Editors")
plt.savefig('Article_370_page_wikiwho_editors_venn.png')
plt.clf()