# PromotED
DVA project


## APIs

The client uses the below GET API to get the courses for a specified job title.

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
  
