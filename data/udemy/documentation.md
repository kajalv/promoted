# Udemy API

## Usage

The script `api_udemy.py`  runs the Udemy API and collects data into `dataset.csv`. The Udemy API credentials need to be configured in `~/.bash_profile` as environment variables `$UDEMY_CLIENT_ID`, `$UDEMY_CLIENT_SECRET`, and `$UDEMY_BASE64`. It takes about 15 minutes to run.

```
python api_udemy.py
```

Then, since the Udemy API makes use of `[]` reserved characters, a shell script is needed to obtain course-level information for each course. The script `get_ratings.sh` reads the file `dataset.csv` and produces `dataset_with_ratings.csv`. This takes almost 2 hours to run.

```
sh get_ratings.sh
```

## API Information

### Courses

Fields we can use:

- title (Name)
- is_paid
- price
- avg_rating
- description
- headline
- url
- primary_category
- instructional_level

Rating, duration, instructional level, category:
We can filter courses by these in the request, but the information is not available in the response by default.

### Categories

- Business
- Design
- Development
- Finance & Accounting
- Health & Fitness
- IT & Software
- Lifestyle
- Marketing
- Music
- Office Productivity
- Personal Development
- Photography
- Teaching & Academics

### Ordering

- relevance
- most-reviewed
- highest-rated (We will use this one)
- newest
- price-low-to-high
- price-high-to-low

## Required dependencies

`jq` needs to be installed. On Mac: `brew install jq`