#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 19:31:33 2020

@author: molly
"""

from os import listdir
from statistics import mean, stdev
import json
from os.path import isfile, join


# First, unique IP editors / total unique editors, averaged over articles.

def find_ips(mypath, fname):
    '''
    Takes files with lists of unique authors, one author per line, and computes
    number of IP editors / 
    '''
    with open(mypath + fname) as thefile:
        print(fname)
        authors = thefile.readlines()
        ipcount = 0
        total = 0
        for author in authors:                
            if author[0].isdigit():
                ipcount += 1
            total += 1
            
        print(ipcount)
        print(total)
        print("IP count / total:", ipcount/total)
        print("------------")
    return ipcount/total
    

            
mypath = "../data/editors/"
author_files = [f for f in listdir(mypath) if ("authors_" in f)] # date!!!

en = []
hi = []
ur = []

if False: # don't unfalse this
  for fname in author_files:
      ip_ratio = find_ips(mypath, fname)
      if "_en_" in fname:
          en.append(ip_ratio)
      elif "_hi_" in fname:
          hi.append(ip_ratio)
      else:
          ur.append(ip_ratio)
          
  for lang_list in [en, hi, ur]:
      print("Mean:", mean(lang_list))
      print("Standard dev:", stdev(lang_list))
    
# Now, want IP edits over all edits
    
def get_editors(fpath):
    """
    Read the file output by getrevisions and compile list of revid's
    """
    with open(fpath) as json_file:
        print(fpath)
        data = json.load(json_file)
        nonIP = []
        IP = []
        for item in data:
            if item['user'][0].isdigit():
                IP.append(item['user'])
            else:
                nonIP.append(item['user'])
    return nonIP, IP

en2 = []
hi2 = []
ur2 = []

mypath = "../data/revisions/"

rev_files =  [f for f in listdir(mypath) if (isfile(join(mypath, f)) and ("history" not in f))]

for fname in rev_files:
    if "_article" in fname:
        nonIP, IP = get_editors(mypath + fname)
        ip_ratio = len(IP) / (len(nonIP) + len(IP))
        if "_en_" in fname:
            en2.append(ip_ratio)
        elif "_hi_" in fname:
            hi2.append(ip_ratio)
        else:
            ur2.append(ip_ratio)
        
for lang_list in [en2, hi2, ur2]:
    print("Mean:", mean(lang_list))
    #print("Standard dev:", stdev(lang_list))
    