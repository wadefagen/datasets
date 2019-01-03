# wadefagen's Useful Datasets

This repository contains a collection of datasets I've found useful.  Many of these datasets are clean versions of public datasets, provided in a clean, consistent format for use in data science projects.

## Avaialble Datasets

- [GPAs of Courses at The University of Illinois](gpa/), `gpa/uiuc-gpa-dataset.csv`
- [Teachers Ranked as Excellent by their Students at UIUC](teachers-ranked-as-excellent/), `teachers-ranked-as-excellent/uiuc-tre-dataset.csv`
- [UIUC Courses by their General Education category](geneds/), `geneds/uiuc-geneds-dataset.csv`
- [Students at The University of Illinois by their home state](students-by-state/), `students-by-state/uiuc-students-by-state.csv`
- [UIUC Course Catalog](course-catalog/), `course-catalog/uiuc-course-catalog.csv`
- [Fighting Illini Historical Football Scores](illini-football/), `illini-football/illini-football-scores.csv`

## General Format

Unless otherwise noted, all datasets are CSV files where the first row contains column headers.

Common column names across multiple datasets include:

- `Year`, a four digit year (ex: `2018`, `2017`, etc)
- `Term`, one of `Spring`, `Summer`, `Fall`, or `Winter`
- `YearTerm`, a four digit year followed by `-sp`, `-su`, `-fa`, or `-wi`.  For example: `2018-sp`.  This format ensure that all `YearTerm >= "2016-fa"` contains all data available from the Fall 2016 to present.

## Useful Scripts

If you're working with these datasets, the following snippets may be helpful to load the data.  Each example assumes you have cloned this repo inside of your project's working directory (as `datasets`, the default name).

### Python (pandas)
```
import pandas as pd

df = pd.read_csv('datasets/gpa/uiuc-gpa-dataset.csv')
# `df` is a DataFrame of the CSV file
```

### Python (dictionary)
```
import csv

with open("datasets/gpa/uiuc-gpa-dataset.csv", "r") as f:
  reader = csv.DictReader(f)
  for row in reader:
    # Each `row` is a row from the CSV as a Python dict indexed with column headers.
    
    # Example usage:
    term = row["Term"]
    year = int(row["Year"])    # Note that Python treats all data as strings; may be useful to make the year an `int`
```

### JavaScript (node.js)
With the [csv-parse package](https://www.npmjs.com/package/csv-parse) (`npm install --save csv-parse`):

```
const parse = require('csv-parse/lib/sync');

var rows = parse( fs.readFileSync("datasets/gpa/uiuc-gpa-dataset.csv"), {columns: true} );
rows.forEach(function (row) {
  // Each `row` is a row from the CSV as a dictionary indexed with column headers.

  // Example usage:
  var term = row["Term"];
  var year = row["Year"];
});
```

