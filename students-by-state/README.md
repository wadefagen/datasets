# Students at The University of Illinois by their home state

A collection of students' home state at the University of Illinois for the years 1975 - 2017 in a clean CSV format.

[A single CSV containing all of the data can be downloaded here][CSV_Download]

[CSV_Download]: https://raw.githubusercontent.com/wadefagen/datasets/master/students-by-state/uiuc-students-by-state.csv


## Data Format

The first row of the CSV file contains column headers.  Every row after the first contains data.  Sample:

| State | Year | Undergrad | Professional | Grad | Total |
| ----- | ---- | --------- | ------------ | ---- | ----- |
| Alabama | 2017 | 20 | 2 | 14 | 36 |
| Alabama | 2016 | 17 | 2 | 15 | 34 |
| ... |
| Illinois | 2017 | 24251 | 537 | 3330 | 28118 |
| ... |

### Values of `State`

Data for each of the 50 US states is present for every year in the dataset.  In addition to the 50 states, the following data is labeled as `State`s:

- `District of Columbia`, data present for all years
- `Guam`, data present in 2013+
- `Military`, data present in 2000+
- `Puerto Rico`, data present in 2013+
- `Unknown`, data present in 2004-2017; this includes only unknown US residents, international students are split out into a different dataset
- `Virgin Islands`, data present in 2017+


## Data Source

All data contained here was sourced from the [Final Statistical Abstract][DMI_FSA] provided by the [Division of Management Information at The University of Illinois][DMI].  The data provided by DMI has changed over time and is a mix of Excel, HTML, and PDF formats; the data here is the same data as a single CSV file.

Additional data transcription and cleaning was completed by [tinaabraham17](https://github.com/tinaabraham17).


[DMI]: http://dmi.illinois.edu/
[DMI_FSA]: http://dmi.illinois.edu/stuenr/#abstract

