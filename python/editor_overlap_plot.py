#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 14:55:29 2020

Read in data copy/pasted from Sang's xlsx document and recreate the plot with 
better labels and colors etc

@author: molly
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('nbAgg')



df = pd.read_csv("../data/editors/editor_overlap.csv")

print(df.columns)

print(df.head())
print(df['Language'])
print(df['Article'])

x = df['SCALE'] # Number of editors on that article
y = df['Percent editors who also edited any other page in that language']

colors = {'English': 'b', 'Hindi': 'g', 'Urdu': 'r'}
markers = {'A370': 'v', 'Insurgency': '^', 'KC': 'd', 'Reorg Act': 's', 'Pulwama': '>'}
    
fig, ax = plt.subplots()


ax.scatter(x, y, c=df['Language'].apply(lambda x: colors[x]))
    
plt.xlabel('Number of editors who edited page')
plt.ylabel('Percent editors who edited another page within language')
ax.legend()

plt.savefig('fig1.png')

#df['color'] = df['Language'].apply(lambda x: 'g' if ('English' in x) else \
 #   ('r' if 'Hindi' in x) else ('b' if 'Urdu' in x))