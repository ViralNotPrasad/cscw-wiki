# cscw-wiki

This repo contains the code we used for our paper, "Understanding Wikipedia practices through Hindi, Urdu, and English takes on evolving regional conflict" [[CSCW '21](https://dl-acm-org.ezproxy.lib.vt.edu/doi/abs/10.1145/3449108)] [[pdf download](bit.ly/wikihue)]. The code is not well-documented yet. If you want to use the code and you're not sure how, please don't hesitate to reach out to Molly Hickman (molly [at] vt [dot] edu), or open an issue!

Some things this code can help you do/get:
- Ratio of "IP editors" to registered editors on an article
- To search revisions on a given page for text (e.g. to see if the same text was added and redacted multiple times) (uses MediaWiki `mwreverts` Python library)
- Degree of cross-language editing (overlap between editors on two language editions of the same page, or set of pages)
- Lag time or correlation between page-view spikes and editing spikes (uses Mediawiki `pageviewapi` Python library)

# The articles

- https://en.wikipedia.org/wiki/Kashmir_conflict
- https://en.wikipedia.org/wiki/Article_370_of_the_Constitution_of_India
- https://en.wikipedia.org/wiki/Insurgency_in_Jammu_and_Kashmir
- https://en.wikipedia.org/wiki/Jammu_and_Kashmir_Reorganisation_Act,_2019
- https://en.wikipedia.org/wiki/2019_Pulwama_attack

# Code road-map
(work in progress)
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

