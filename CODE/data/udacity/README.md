# Udacity API

## API Information

The Udacity catalog is available publicly.

URL: [https://www.udacity.com/public-api/v1/courses](https://www.udacity.com/public-api/v1/courses)

Method: GET

Authorizations: NONE

Fields used:

* title
* level
* expected_duration
* expected_duration_unit
* skills
* is_free_course 

## Dataset Creation

The script `udacity.py` reads the catalog from Udacity and creates a `dataset_udacity.csv` dataset.
