# University of Illinois Course Prerequisite Dataset

This dataset uses rudimentary natural language processing to find the list of prerequisites for each course at UIUC.

## Data Format

The data is available in two formats: JSON, and CSV.


For a course like CS 374, the description is "Same as ECE 374. Prerequisite: One of CS 173, MATH 213; CS 225.". Each clause of the description is represented as a "prerequisite group". You must take one course from each prerequisite group in order to satis.

The JSON is formatted like so:

```json
{
  "CS 374": [
    [
      {
        "course": "CS 173",
        "is_concurrent": false
      },
      {
        "course": "MATH 213",
        "is_concurrent": false
      }
    ],
    [
      {
        "course": "CS 225",
        "is_concurrent": false
      }
    ]
  ],
}
```

And the CSV is formatted like so:

```
CS 374,CS 225,False,0
CS 374,CS 173,False,1
CS 374,MATH 213,False,1
```

## Scripts

The prerequisite dataset is derived from the `course-catalog` dataset. To regenerate the dataset,

Change the script line:

```python
terms = ['2023-sp', '2022-fa']
```

To your desired terms, and rerun the program to regenerate the files `uiuc-prerequisites.csv` and `uiuc-prerequisites.json`.

```
$ python3 main.py
```

## Important Note

The prerequisite list is filtered! For example, if the class "REL 223" says that the prerequisite list is REL 213 or REL 214 but only REL 214 was offered in `['2023-sp', '2022-fa']`, then the item "REL 213" will not show up as a potential way to satisify that prerequisite.