# cscw-wiki

## The articles

## Code road-map
* Page-views/edits code and plots: R/Pageviews-edits-data-viz-Clean.ipynb
** Inputs: R/wiki_<language>_pageviews_<dates>.csv files; data/revisions/rev_<article>_<lang>_<datetime>.json files
** Outputs: some figures to the plots/ dir; R/pearson_df.csv
* Peak cross-correlation: python/corr_math.py (exact numbers for TLCC)
** Inputs: R/pearson_df.csv
** Outputs: No files

## TODO:
### Soon:
* Solve the problem of pulling page-views data from the two new Hindi articles (and presumably Urdu). Error suggested they're not "available" through the WikipediR pipeline yet.
* Compute similarity data for the full five articles (pending whether we decide it's worth going ahead with the two "new" articles)
### If we get accepted? Or in any case, longer term goals:
* Refactor code/convert ipynb code to usable, navigable Python.
* Reorganize -- it doesn't make sense that code is divided into R and Python folders.

