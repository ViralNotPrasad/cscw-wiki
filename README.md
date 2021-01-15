# CSCW 2021: Understanding Wikipedia Practices Through Hindi, Urdu, and English Takes on an Evolving Regional Conflict
# Supporting Materials

## The articles

- https://en.wikipedia.org/wiki/Kashmir_conflict
- https://en.wikipedia.org/wiki/Article_370_of_the_Constitution_of_India
- https://en.wikipedia.org/wiki/Insurgency_in_Jammu_and_Kashmir
- https://en.wikipedia.org/wiki/Jammu_and_Kashmir_Reorganisation_Act,_2019
- https://en.wikipedia.org/wiki/2019_Pulwama_attack

## Links to Hindi and Urdu articles as they appeared at midnight AOE on September 1, 2019
------
Note: Time in J&K is GMT+5:30. 9:30 ahead of Eastern Time. 00:00 EDT is 16:00 (-1 day) AoE.
------
### 1. JAMMU AND KASHMIR REORGANISATION ACT, 2019

Urdu: https://ur.wikipedia.org/w/index.php?title=%D8%AC%D9%85%D9%88%DA%BA_%D9%88_%DA%A9%D8%B4%D9%85%DB%8C%D8%B1_%D8%AA%D9%86%D8%B8%DB%8C%D9%85_%D9%86%D9%88_%D8%A7%DB%8C%DA%A9%D9%B9%D8%8C_2019%D8%A1&oldid=3964960 (last edit was made 06:56, 24 August 2019)
Hindi: https://hi.wikipedia.org/w/index.php?title=%E0%A4%9C%E0%A4%AE%E0%A5%8D%E0%A4%AE%E0%A5%82_%E0%A4%94%E0%A4%B0_%E0%A4%95%E0%A4%B6%E0%A5%8D%E0%A4%AE%E0%A5%80%E0%A4%B0_%E0%A4%AA%E0%A5%81%E0%A4%A8%E0%A4%B0%E0%A5%8D%E0%A4%97%E0%A4%A0%E0%A4%A8_%E0%A4%85%E0%A4%A7%E0%A4%BF%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%AE,_2019&oldid=4287010 (there have been two edits since August; last August edit was made 10:37, 23 August 2019)

### 2. KASHMIR CONFLICT

Hindi: https://hi.wikipedia.org/w/index.php?title=%E0%A4%95%E0%A4%B6%E0%A5%8D%E0%A4%AE%E0%A5%80%E0%A4%B0_%E0%A4%B5%E0%A4%BF%E0%A4%B5%E0%A4%BE%E0%A4%A6&oldid=4295252

Urdu (as of edit Sep 1 06:05 ET (31 Aug 22:05 AoE) ): https://ur.wikipedia.org/w/index.php?title=%D9%85%D8%B3%D8%A6%D9%84%DB%81_%DA%A9%D8%B4%D9%85%DB%8C%D8%B1&oldid=3969036

### 3. ARTICLE 370

Hindi (edited 12:25 31 Aug ET (same day 04:00 AoE) ): https://hi.wikipedia.org/w/index.php?title=%E0%A4%85%E0%A4%A8%E0%A5%81%E0%A4%9A%E0%A5%8D%E0%A4%9B%E0%A5%87%E0%A4%A6_%E0%A5%A9%E0%A5%AD%E0%A5%A6&oldid=4296740

Urdu: https://ur.wikipedia.org/w/index.php?title=%D8%A2%D8%A6%DB%8C%D9%86_%DB%81%D9%86%D8%AF_%DA%A9%DB%8C_%D8%AF%D9%81%D8%B9%DB%81_370&oldid=3963861

### 4. INSURGENCY

Hindi only: https://hi.wikipedia.org/w/index.php?title=%E0%A4%9C%E0%A4%AE%E0%A5%8D%E0%A4%AE%E0%A5%82_%E0%A4%94%E0%A4%B0_%E0%A4%95%E0%A4%B6%E0%A5%8D%E0%A4%AE%E0%A5%80%E0%A4%B0_%E0%A4%AE%E0%A5%87%E0%A4%82_%E0%A4%B5%E0%A4%BF%E0%A4%A6%E0%A5%8D%E0%A4%B0%E0%A5%8B%E0%A4%B9&oldid=4286865

### 5. PULWAMA ATTACK

Urdu: https://ur.wikipedia.org/w/index.php?title=%D9%BE%D9%84%D9%88%D8%A7%D9%85%DB%81_%D8%AD%D9%85%D9%84%DB%81%D8%8C_2019%D8%A1&oldid=3958483

Hindi:
https://hi.wikipedia.org/w/index.php?title=%E0%A5%A8%E0%A5%A6%E0%A5%A7%E0%A5%AF_%E0%A4%AA%E0%A5%81%E0%A4%B2%E0%A4%B5%E0%A4%BE%E0%A4%AE%E0%A4%BE_%E0%A4%B9%E0%A4%AE%E0%A4%B2%E0%A4%BE&oldid=4291166


## Code road-map
* Page-views/edits code and plots: R/Pageviews-edits-data-viz-Clean.ipynb
```
* Inputs: 
** R/wiki_<language>_pageviews_<dates>.csv files; 
** data/revisions/rev_<article>_<lang>_<datetime>.json files
* Outputs: 
** some figures to the plots/ dir; 
** R/pearson_df.csv
```
* Peak cross-correlation: python/corr_math.py (exact numbers for TLCC)
```
* Inputs: R/pearson_df.csv
* Outputs: No files
```
* Page-views data pull: R/get-page-data.Rmd
```
* Inputs: None
* Outputs: R/wiki_<language>_pageviews_<dates>.csv files
```
* Similarity (Jaccard) computation: python/similarity.py
```
* Inputs:
* Outputs:
```
* Revisions data pull: python/getrevisions.py
```
* Inputs:
* Outputs:
```
(work in progress)

## TODO:
### Soon:
* Solve the problem of pulling page-views data from the two new Hindi articles (and presumably Urdu). Error suggested they're not "available" through the WikipediR pipeline yet.
* Compute similarity data for the full five articles (pending whether we decide it's worth going ahead with the two "new" articles)
### If we get accepted? Or in any case, longer term goals:
* Refactor code/convert ipynb code to usable, navigable Python.
* Reorganize -- it doesn't make sense that code is divided into R and Python folders.

