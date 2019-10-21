from os import listdir
from os.path import isfile, join
import json
import pandas as pd

# Read data from the revisions files

mypath = "../data/revisions/"
revfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in revfiles:
    with open(mypath + file) as thefile:
        data = json.load(thefile)
        df = pd.DataFrame(data)

# print the last df just to see if it's ok
print(df)

