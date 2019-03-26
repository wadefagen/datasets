
# University of Illinois' GenEds

A collection of General Education ("Gen Ed") categories from the [Course Explorer's GenEd Section](https://courses.illinois.edu/gened/DEFAULT/DEFAULT)

[Download the full dataset as a single CSV file](https://raw.githubusercontent.com/wadefagen/datasets/master/geneds/uiuc-geneds.csv)


## Data Format

The first row of the CSV file contains column headers. Every row after the first contains data. Sample:

| Year | Term | YearTerm | Course | Course Title | ACP | CS | HUM | NAT | QR | SBS |
| ---- | ---- | -------- | ------ | ------------ | --- | -- | --- | --- | -- | --- |
| 2019 | Fall | 2019-fa  | AAS 100 | Intro Asian American Studies |  | US | | | | SS |
| ... |
| 2019 | Fall | 2019-fa  | CS 107 | Data Science Discovery | | | | | QR1 | |
| ... |

All courses listed contains at least one Gen Ed category.  Many courses contain multiple Gen Ed categories.

The column labels and values have the following meaning:

- `ACP` for "Advanced Composition"; values `ACP` or blank
- `CS` for "Cultural Studies"; values are `NW` for "Non-Western Cultures", `WCC` for "Western/Comparative Cultures", `US` for "US Minority Cultures", or blank
- `HUM` for "Humanities & the Arts"; values are `HP` for "Historical & Philosophical Perspectives", `LA` for "Literature & the Arts", or blank
- `NAT` for "Natural Sciences & Technology"; value are `LS` for "Life Sciences", `PS` for "Physical Sciences", or blank
- `QR` for "Quantitative Reasoning"; values are `QR1` for "Quantitative Reasoning 1", `QR2` for "Quantitative Reasoning 2", or blank
- `SBS` for "Social & Behavioral Sciences"; values are `BS` for "Behavioral Sciences", `SS` for "Social Sciences", or blank


## Projects Using this Dataset

1. [Every Gen Ed at UIUC, by GPA](http://waf.cs.illinois.edu/discovery/every_gen_ed_at_uiuc_by_gpa/)

*If you create a project with this dataset, I'd love to link it here!  Send a PR with your project added to this list!*


## Data Source

Scraped from https://courses.illinois.edu/gened/DEFAULT/DEFAULT