
# University of Illinois' Course Catalog

A collection of all courses offered by the University of Illinois, as found in the [Course Catalog](https://courses.illinois.edu/cisapp/explorer/catalog/2019/spring.xml)

[Download the full dataset as a single CSV file](https://raw.githubusercontent.com/wadefagen/datasets/master/course-catalog/uiuc-course-catalog.csv)


## Data Format

The first row of the CSV file contains column headers. Every row after the first contains data. Sample:

| Year | Term | YearTerm | Subject | Number | Title |
| ---- | ---- | -------- | ------- | ------ | ----- |
| 2019 | Spring | 2019-sp  | AAS | 100 | Intro Asian American Studies |
| ... |
| 2019 | Spring | 2019-sp  | CS | 225 | Data Structures |
| ... |


## Data Source

Scraped from https://courses.illinois.edu/cisapp/explorer/catalog/2019/spring.xml on September 30, 2018