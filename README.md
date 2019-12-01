# PromotEd

PromotEd recommends courses from multiple MOOC providers based on the skills required for a specific job role. The skills required for each job is collected beforehand from available datasets. Similarly, information about available courses are also procured from multiple MOOC platforms like Udacity, Udemy, and edX. At runtime, all these datasets are used to recommend courses to the user.

# Installation

After retrieving the GitHub code, perform the following steps to setup the application.

## Running the server

`cd` to the `CODE` directory and start the server with the following command:

```
python server.py
```

Flask should be installed and Python v3.x should be used. The command may change to `python3 server.py` in some systems.

## Running the client (user interface)

`cd` to the `CODE/ui` directory and start the interface with `yarn`.

```
yarn install 
yarn start
```

Alternatively, `npm` can also be used instead of `yarn`.

```
npm install
npm start
```

# Demo

Once you have the client and server running (follow steps above), open your browser and go to http://localhost:3000. This opens up the home page of the application.

# Datasets

## Job skills dataset

We used two datasets for this application.

* https://www.kaggle.com/PromptCloudHQ/us-jobs-on-monstercom
* https://www.kaggle.com/PromptCloudHQ/usbased-jobs-from-dicecom

We did some custom transformations on the datasets using OpenRefine. Some of the transformations include

* Clustering similar job titles
* Standardizing vocabulary e.g. converting Software Engineer, Software Development Engineer etc., to Software Developer

The cleaned and transformed datasets are provided under `/data/jobs-data` in the files `dice_US_jobs-clean.csv` and `monster_com_jobs-clean.csv`

The job skillset keywords are extracted by executing `keywords.py` provided under `/data/jobs-data`.

## Course catalog dataset

We used the data from three platforms for this project - Udemy, Udacity and edX. The details about the APIs and the scripts used are provided in respective folders under `/data`. 

# APIs

> GET /get_courses?job_title=_JOB TITLE_

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

> GET /get_jobs

The response is an array of job titles.

```json
[
  "Software Developer", 
  "Senior Mobile Developer"
]
```
