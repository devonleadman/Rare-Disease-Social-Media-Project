<img src = "https://ncats.nih.gov/sites/all/themes/ncats-2014/images/assets/ncats-logo.png" align=right width="30%" height="30%">

# RDSMproj

RDSMproj (**R**are **D**iseases **S**ocial **M**edia **Proj**ect) for the [National Center for Advancing Translational Sciences](https://ncats.nih.gov/) at the [NIH](https://www.nih.gov/). This project looks at mining information from social media ([Reddit](https://www.reddit.com/)) and finding subreddits that are related to different rare diseases found in the [GARD](https://rarediseases.info.nih.gov/) database. The project matches rare diseases to Reddit subreddits, downloads the post and comment data, and then analyzes the text data to find the different topics that people are talking about.

## Overview

The project is split into four packages as part of rdsmproj:
1. [mapper](https://github.com/ncats/Rare-Disease-Social-Media-Project/tree/main/rdsmproj/mapper) is a python package that maps text to a rare disease(s) using [nltk](https://www.nltk.org/) and [spaCy](https://spacy.io/). An alternate name for this package is **NormMap V2**.
2. [sm_reddit](https://github.com/ncats/Rare-Disease-Social-Media-Project/tree/main/rdsmproj/sm_reddit) is a collection of scripts that utilizes [pmaw](https://github.com/mattpodolak/pmaw) to download Reddit post and comment text data for use in topic modeling or other text analyses.
3. [tm_t2v](https://github.com/ncats/Rare-Disease-Social-Media-Project/tree/main/rdsmproj/tm_t2v) is a python package that creates topic models of text using [Top2Vec](https://github.com/ddangelov/Top2Vec).
4. [tm_lda](https://github.com/ncats/Rare-Disease-Social-Media-Project/tree/main/rdsmproj/tm_lda) is a (**legacy**) python package that creates topic models of text primarily using LDA as implemented by [Gensim](https://radimrehurek.com/gensim/). This package was used in this [paper](https://doi.org/10.3389/frai.2022.948313).

## Installation
Ensure that you have up to date copies of `pip`, `setuptools`, and `wheel` prior to installation.
```bash
pip install --upgrade pip setuptools wheel
```


For now, each package above is installed separately.
```bash
pip install rdsmproj[mapper]
pip install rdsmproj[sm_reddit]
pip install rdsmproj[tm_t2v]
pip install rdsmproj[tm_tlda]
```

## Quick Start

```python
from rdsmproj import sm_reddit

# Add in simple examples for each package.
```

## To Do
- [x] Test package install from TestPyPI.
- [ ] Update main README.md Quick Start with examples for each package.
- [ ] Create [sm_reddit](https://github.com/ncats/Rare-Disease-Social-Media-Project/tree/main/rdsmproj/sm_reddit) README.md.
- [ ] Create [tm_t2v](https://github.com/ncats/Rare-Disease-Social-Media-Project/tree/main/rdsmproj/tm_t2v) README.md.
- [ ] Create [tm_lda](https://github.com/ncats/Rare-Disease-Social-Media-Project/tree/main/rdsmproj/tm_lda) README.md.
- [ ] Add visualizations and flowcharts to the readme files.
- [ ] Upload to PyPI.
