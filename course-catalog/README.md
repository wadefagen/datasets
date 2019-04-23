
# University of Illinois' Course Catalog

A collection of all courses offered by the University of Illinois, as found in the [Course Catalog](https://courses.illinois.edu/cisapp/explorer/catalog/DEFAULT/DEFAULT.xml)

[Download the full dataset as a single CSV file](https://raw.githubusercontent.com/wadefagen/datasets/master/course-catalog/uiuc-course-catalog.csv)


## Data Format

The first row of the CSV file contains column headers. Every row after the first contains data. Sample:

| Year | Term | YearTerm | Subject | Number | Name  | Description | Credit Hours | Section Info | Degree Attributes | Schedule Information | 
| ---- | ---- | -------- | ------- | ------ | ----- | ----------- | ------------ | ------------ | ----------------- | -------------------- |
| 2019 | Fall | 2019-fa  | AAS | 100 | Intro Asian American Studies | Interdisciplinary introduction to the basic concepts and approaches in Asian American Studies [...] | 3 hours. |  | Social & Beh Sci - Soc Sci, and Cultural Studies - US Minority course. |  |
| ... |
| 2019 | Fall | 2019-fa  | STAT | 107 | Data Science Discovery | Data Science Discovery is the intersection of statistics, computation, and real-world relevance [...] | 4 hours. | Same as CS 107 and IS 107. | Quantitative Reasoning I course. | |
| ... |


## Data Source

Scraped from https://courses.illinois.edu/cisapp/explorer/catalog/2019/fall.xml on April 9, 2019