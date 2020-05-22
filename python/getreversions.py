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
        revids = []
        for item in data:
            revids.append(item['revid'])
    return revids

def format_revert(revert):
    if revert is None:
        return ""
    else:
        return " ".join([str(revert.reverting['revid']),
                         str([r['revid'] for r in revert.reverteds]),
                         str(revert.reverted_to['revid'])])

  
for lang in ["hi", "en", "ur"]:
    print("Language:", lang)
    mypath = "../data/revisions/"
    thefiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and (lang in f))]
    session = mwapi.Session("https://" + lang + ".wikipedia.org")
    
    for fname in thefiles: # For each file (each article in the language)
        revid_list = get_revids(mypath + fname)
        netcount = 0
        revertedcount = 0
        for revid in revid_list:
            #print("REVID:", revid)
            reverting, reverted, reverted_to = mwreverts.api.check(session, revid) 
            #print("reverting:", format_revert(reverting))
            #print("reverted:", format_revert(reverted))
            #print("reverted_to:", format_revert(reverted_to))
            netcount += 1
            if reverted != None:
                revertedcount += 1
        print("---------------")
        print("File:", fname)
        print("Total:", netcount)
        print("Reverted:", revertedcount)
        print("Total / Reverted:", revertedcount/netcount)
        






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