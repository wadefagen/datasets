# Perception of Probability Words

A collection of 123 responses to an internet survey containing perceptions of probability words.

[The complete, raw survey results can be downloaded here.][CSV_Download]

[CSV_Download]: https://raw.githubusercontent.com/wadefagen/datasets/master/Perception-of-Probability-Words/survey-results.csv


## Projects Using this Dataset

1. [Perception of Probability Words](http://waf.cs.illinois.edu/visualizations/Perception-of-Probability-Words/)

![GitHub Logo](boxplots.png)

*If you create a project with this dataset, I'd love to link it here!  Send a PR with your project added to this list!*


## Data Format

The first row of the CSV file contains column headers.  Every row after the first contains data.  Sample:

| "Almost Certain" | "Highly Likely" | "Very Good Chance" | ... |
| ---------------- | --------------- | ------------------ | --- |
| 60 | 85 | 80 | ... |
| 99 | 90 | 80 | ... |
| ... |

### Methodology

The survey was conducted using Google Forms and was advertised with a single post on reddit, Facebook, Twitter, and LinkedIn by Wade Fagen-Ulmschneider.  Users were asked to provide their perception of 17 different probability words.


The instructions given at the top of the survey:

> There is a classic research paper that outlines a group perception of the underlying percentage of various words used to describe uncertain events.  I'm very interested if these perceptions have changed and to collect a dataset among my group of friends.
>
> Consider the statement:
> "Researchers are ABSOLUTELY CERTAIN that eating dark chocolate decreases your risk of heart disease."
>
> The words "ABSOLUTELY CERTAIN" will convey a 99% (if you are a skeptic) or 100% probability that the statement is true.  In the following survey, answer the numeric probability you give to each of these probability words.
>
> - Your answer MUST be a SINGLE NUMBER (not a range of numbers).
> - You do not need to add a percent sign (eg: use "100" as an answer to indicate 100%).


Each word was presented in random order with the word in a large font and a description that reads:

> What percentage do you assume something to be if researchers are "almost certain" of the result?


A total of 123 users responded to the survey during the two weeks the survey was available.  The full raw results are available in `survey-results.csv`.