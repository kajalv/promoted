# PromotED
PromotEd recommends courses from multiple MOOC providers based on the skills required for a specific job role. The skills required for each job is collected beforehand from available datasets. Similarly, information about available courses are also procured from multiple MOOC platforms like Udacity, Udemy, and edX. At runtime, both these datasets are used to recommend courses to the user.

# Installation

After retrieving the github code, doing the following steps to setup the application.

## Running the server

> python server.py # should have Flask installed

## Running the client (user interface)

> yarn install 
> yarn start

NPM can be used instead of Yarn.

# Demo

# Datasets

# APIs

> /get_courses?job_title=_JOB TITLE_

The response is an array of JSON objects each of which represents a course. An example is given below.

```json
  [
    {
        "duration": 1,
        "duration_unit": "week",
        "level": 1,
        "price": 149.99,
        "site": "udemy",
        "title": "R Programming: Mastering R for data analysis"
    },
    {
        "duration": 1,
        "duration_unit": "week",
        "level": 1,
        "price": 29.99,
        "site": "udemy",
        "title": "Certified business analysis professional (CBAP) practice"
    }
  ]
```

> /get_jobs

The response is an array of job titles

```json
[
  "Software Developer", 
  "Senior Mobile Developer"
]
```
