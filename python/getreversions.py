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
import json
from os import listdir
from os.path import isfile, join


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

  
mypath = "../data/revisions/"
session = mwapi.Session("https://en.wikipedia.org") 
    
  
if True:  
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
            reversions = []
            for revid in revids:
                #print("REVID:", revid)
                try:
                    reverting, reverted, reverted_to = mwreverts.api.check(session, revid) 
                    if reverted != None:
                        revertedcount += 1
                        #pdb.set_trace()
                        # tuple with date of reverted edit and date that it was reverted
                        revert, bad, back_to = format_revert(reverted).split(' ')
                        bad = int(bad.strip('[]'))
                        revert = int(revert)
                        reversions.append((revids[bad], revids[revert]))

                except:
                    failures += 1
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
            print(reversions)
            print("---------------")







'''
#pdb.set_trace()

reverting, reverted, reverted_to = \
    mwreverts.api.check(session, reverted.reverting['revid'])
print("reverting:", format_revert(reverting))
print("reverted:", format_revert(reverted))
print("reverted_to:", format_revert(reverted_to))

print("---------------")

reverting, reverted, reverted_to = \
    mwreverts.api.check(session, reverting.reverted_to['revid'])
print("reverting:", format_revert(reverting))
print("reverted:", format_revert(reverted))
print("reverted_to:", format_revert(reverted_to))

print("---------------")
print("Let's to detect from deleted edits")
print("---------------")

mwapi.cli.do_login(session, "English Wikipedia")
reverting, reverted, reverted_to = \
    mwreverts.api.check_deleted(session, 587400097)
print("reverting:", format_revert(reverting))
print("reverted:", format_revert(reverted))
print("reverted_to:", format_revert(reverted_to))

print("---------------")

reverting, reverted, reverted_to = \
    mwreverts.api.check_deleted(session, reverted.reverting['revid'])
print("reverting:", format_revert(reverting))
print("reverted:", format_revert(reverted))
print("reverted_to:", format_revert(reverted_to))

print("---------------")

reverting, reverted, reverted_to = \
    mwreverts.api.check_deleted(session, reverting.reverted_to['revid'])
print("reverting:", format_revert(reverting))
print("reverted:", format_revert(reverted))
print("reverted_to:", format_revert(reverted_to))
'''