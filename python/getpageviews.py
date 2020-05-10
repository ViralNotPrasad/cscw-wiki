#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:41:39 2020

Pageviews datat pull via pageviewsapi (previously done in R via WikipediR)

@author: molly hickman (mollygh@vt.edu)
@version: 1
"""

import pageviewapi
import pandas as pd

start = 20180101
end = 20190101

# Urdu articles are in a different order from the others, but this was the best I could do.
# Copy/paste does not work with Arabic script as you'd expect.
# The order is: (0) 2019 Pulwama attack, (1) Reorganisation Act, (2) Article 370, (3) Kashmir conflict

ARTICLES_DICT = {"en": ["Kashmir_conflict",
                            "Article_370_of_the_Constitution_of_India",
                            "Insurgency_in_Jammu_and_Kashmir"],
                            #"2019_Pulwama_attack",
                            #"Jammu_and_Kashmir_Reorganisation_Act,_2019"
                "hi": ["कश्मीर_विवाद", "अनुच्छेद_३७०", "जम्मू_और_कश्मीर_में_विद्रोह"],
                "ur":["مسئلہ_کشمیر"]}


def getPageviews(articleName, lang):
  '''
  Get pageviews for given article and language version of Wikipedia, convert to
  dataframe.
  ---
  Parameters: article name, language abbreviated ('en', 'hi', 'ur', ...)
  Returns: dataframe. 1 row per day; columns are project, article, views, etc
  ---
  '''
  dailyPageViewsDict = pageviewapi.per_article(lang + '.wikipedia', articleName, start, end,
                            agent='all-agents', granularity='daily')
  return pd.DataFrame.from_dict(dailyPageViewsDict['items'])


def main():
  '''
  Loop through languages and articles; clean up; write data to csv
  ---
  Parameters: none
  Returns: nothing, just writes one file per language to ~/data/pageviews
  ---
  '''
  for lang in ARTICLES_DICT.keys():
    
    dfList = []
    
    for article in ARTICLES_DICT[lang]:
      print(lang, article)
      # Call getPageviews for lang/article pair
      articleDF = getPageviews(article, lang)
      
      # Make article names English
      if ("فعہ_370" in article) | ("३७०" in article):
        articleDF.article = "Article 370 of the Constitution of India"
      elif ("یکٹ" in article) | ("कश्मीर_पुनर्गठन_" in article):
        articleDF.article = "Jammu and Kashmir Reorganisation Act, 2019"
      elif ("حملہ" in article) | ("२०१९_पुलवामा" in article):
        articleDF.article = "2019 Pulwama attack"
      elif ("کشمیر" in article) | ("कश्मीर_विवाद" in article):
        articleDF.article = "Kashmir conflict"
      elif ("जम्मू_और" in article):
        articleDF.article = "Insurgency in Jammu and Kashmir"
        
      # Remove semi-colons from en names
      if lang == "en":
        articleDF.article = articleDF.article[0].replace("_", " ")
        
      # Change timestamp field to what R script used to do
      dateCol = articleDF.timestamp.apply(lambda x: x[:4]+"-"+x[4:6]+\
                                                 "-"+x[6:8])
      articleDF['date'] = dateCol
      articleDF = articleDF.drop('timestamp', axis=1)
     
      print(articleDF.head())

      dfList.append(articleDF)
            
    # Put the DFs for this language together into one DF and save
    wholeDf = pd.concat(dfList)
    wholeDf.to_csv("../data/pageviews/wiki_" + lang + \
                   "_pageviews_2018.csv")
  

if __name__ == "__main__":
  main()


    

    
    
    
    
    