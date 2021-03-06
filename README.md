# cscw-wiki

## The articles

OG:
- https://en.wikipedia.org/wiki/Kashmir_conflict
- https://en.wikipedia.org/wiki/Article_370_of_the_Constitution_of_India
- https://en.wikipedia.org/wiki/Insurgency_in_Jammu_and_Kashmir

Possible new articles:
- https://en.wikipedia.org/wiki/Jammu_and_Kashmir_Reorganisation_Act,_2019
- https://en.wikipedia.org/wiki/2019_Pulwama_attack

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

