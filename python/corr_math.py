#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 09:17:29 2020

For getting max correlation for each language and computing p value probably

@author: molly
"""

import pandas as pd
import numpy as np

df = pd.read_csv("../R/pearson_corr_article_370.csv")

print(df[df.lang=="hi"])


###############################################################################

def findMaxCorrOffset(df, lang):
  df2 = df[df.lang == lang]
  
  pmax = df2['pearson'].idxmax()
  print(pmax)
  maxrow = df.iloc[pmax]
  print(maxrow)
  
findMaxCorrOffset(df, "en")
findMaxCorrOffset(df, "ur")
findMaxCorrOffset(df, "hi")
  


