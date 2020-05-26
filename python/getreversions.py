#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 20:10:34 2020

@author: molly

https://github.com/mediawiki-utilities/python-mwreverts/blob/master/demo_api_check.py
"""

import mwapi
import mwapi.cli
import mwreverts.api
import pdb
import pandas as pd
from datetime import datetime
import json
from os import listdir
from os.path import isfile, join
import re


def get_revids(fname):
    """
    Read the file output by getrevisions and compile list of revid's
    """
    with open(fname) as json_file:
        data = json.load(json_file)
        revids = {}
        for item in data:
            revids[item['revid']] = item['timestamp']
    return revids

def format_revert(revert):
    if revert is None:
        return ""
    else:
        return " ".join([str(revert.reverting['revid']),
                         str([r['revid'] for r in revert.reverteds]),
                         str(revert.reverted_to['revid'])])

def multi_reverted(formatted_revert): 
    if len(formatted_revert.split(' ')) == 3:
        revert, bad, back_to = formatted_revert.split(' ')
        bad = int(bad.strip('[]'))
        revert = int(revert)
    else:
        full = formatted_revert.split(' ')
        revert = int(full[0])
        bad = []
        for i in range(len(full) - 2):
            bad.append(int(full[ 1 + i ].strip('[,]'))) # the middle ones (all but first and last)
    return revert, bad

        
  
mypath = "../data/revisions/"
session = mwapi.Session("https://en.wikipedia.org") 
    
  
if True:          
    df = pd.DataFrame({'fname': [], 'edit': [], 'reverted': []})
    for lang in ["hi", "en", "_ur_"]:
        print("Language:", lang)
        thefiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and \
                                       (lang in f)) and ("history" not in f)]
        session = mwapi.Session("https://" + lang + ".wikipedia.org")
        
        for fname in thefiles: # For each file (each article in the language)
            revids = get_revids(mypath + fname)
            netcount = 0
            revertedcount = 0
            failures = 0
            for revid in revids:
                #print("REVID:", revid)
                reverted = None
                try:
                    reverting, reverted, reverted_to = mwreverts.api.check(session, revid) 

                except:
                    failures += 1
                    
                if (reverted != None):
                    revertedcount += 1
                    # tuple with date of reverted edit and date that it was reverted
                    #print(reverted)
                    #pdb.set_trace()
                    revert, bad = multi_reverted(format_revert(reverted))
                    if not (isinstance(bad, list)):
                        new_row = {'fname': fname, 'edit': revids[bad], \
                                   'reverted': revids[revert]}
                    else:
                        for i in range(len(bad)):
                            new_row = {'fname': fname, 'edit': revids[bad[i]], \
                                       'reverted': revids[revert]}
                    #pdb.set_trace()
                    df = df.append(new_row, ignore_index = True)
                #print("reverting:", format_revert(reverting))
                #print("reverted:", format_revert(reverted))
                #print("reverted_to:", format_revert(reverted_to))
                netcount += 1
        
            print("File:", fname)
            print("Total:", netcount)
            print("Reverted:", revertedcount)
            if netcount != 0:
                print("Reverted / Total:", revertedcount/netcount)
            print("Failures:", failures) #https://github.com/mediawiki-utilities/python-mwreverts/issues/11
            print("---------------")
            
            
df.to_csv("../data/reversions/reversions_" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") \
          + ".csv", index=False)
