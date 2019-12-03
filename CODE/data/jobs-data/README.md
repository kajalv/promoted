# Job Dataset

Monster and Dice datasets were obtained from Kaggle and cleaned.

## Keyword extraction

The keywords extraction script `keyword_extraction.py` can be run as follows:

```
python keyword_extraction.py
```

Python 3.x must be used. The script picks the cleaned data and generates `jobs_skills_keywords.csv` containing job titles and their corresponding keywords.

## Dependencies

`pandas`, `ntlk`, `sklearn`, `ntlk.stopwords`, `ntlk.wordnet` need to be installed.
