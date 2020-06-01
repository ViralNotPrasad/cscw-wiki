#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 19:31:33 2020

@author: molly
"""

with open(fname) as thefile:
    authors = thefile.readlines()
    ipcount = 0
    total = 0
    for author in authors:
        if isdigit(author):
            ipcount += 1
        total += 1