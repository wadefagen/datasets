
# University of Illinois' Course Catalog

A collection of all courses offered by the University of Illinois, as found in the [Course Catalog](https://courses.illinois.edu/cisapp/explorer/catalog/DEFAULT/DEFAULT.xml).

- [Spring 2023](https://raw.githubusercontent.com/wadefagen/datasets/master/course-catalog/data/2023-sp.csv)

- [Fall 2022](https://raw.githubusercontent.com/wadefagen/datasets/master/course-catalog/data/2022-fa.csv)
- [Spring 2022](https://raw.githubusercontent.com/wadefagen/datasets/master/course-catalog/data/2022-sp.csv)

- [Fall 2021](https://raw.githubusercontent.com/wadefagen/datasets/master/course-catalog/data/2021-fa.csv)
- [Spring 2021](https://raw.githubusercontent.com/wadefagen/datasets/master/course-catalog/data/2021-sp.csv)

- [Fall 2020](https://raw.githubusercontent.com/wadefagen/datasets/master/course-catalog/data/2020-fa.csv)
- [Spring 2020](https://raw.githubusercontent.com/wadefagen/datasets/master/course-catalog/data/2020-sp.csv)

- [Fall 2019](https://raw.githubusercontent.com/wadefagen/datasets/master/course-catalog/data/2019-fa.csv)
- [Spring 2019](https://raw.githubusercontent.com/wadefagen/datasets/master/course-catalog/data/2019-sp.csv)

- [Fall 2018](https://raw.githubusercontent.com/wadefagen/datasets/master/course-catalog/data/2018-fa.csv)
- [Spring 2018](https://raw.githubusercontent.com/wadefagen/datasets/master/course-catalog/data/2018-sp.csv)

- [Fall 2017](https://raw.githubusercontent.com/wadefagen/datasets/master/course-catalog/data/2017-fa.csv)
- [Spring 2017](https://raw.githubusercontent.com/wadefagen/datasets/master/course-catalog/data/2017-sp.csv)

- [Fall 2016](https://raw.githubusercontent.com/wadefagen/datasets/master/course-catalog/data/2016-fa.csv)



## Data Format

The first row of the CSV file contains column headers. Every row after the first contains data. The following example shows the beginning of the CSV file (in terms of both rows and columns):

| Year | Term | YearTerm | Subject | Number | Name  | Description | Credit Hours | Section Info | Degree Attributes | Schedule Information | ... |
| ---- | ---- | -------- | ------- | ------ | ----- | ----------- | ------------ | ------------ | ----------------- | -------------------- | --- |
| 2019 | Fall | 2019-fa  | AAS | 100 | Intro Asian American Studies | Interdisciplinary introduction to the basic concepts and approaches in Asian American Studies [...] | 3 hours. |  | Social & Beh Sci - Soc Sci, and Cultural Studies - US Minority course. |  | ... |
| ... |
| 2019 | Fall | 2019-fa  | STAT | 107 | Data Science Discovery | Data Science Discovery is the intersection of statistics, computation, and real-world relevance [...] | 4 hours. | Same as CS 107 and IS 107. | Quantitative Reasoning I course. | | ... |
| ... |


## Data Source

Scraped from the Course Explorer API found at [https://courses.illinois.edu/cisapp/](https://courses.illinois.edu/cisapp/)
