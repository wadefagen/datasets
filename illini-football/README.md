
# University of Illinois' Fighting Illini Historical Football Scores

A collection of final scores of every known Fighting Illini football game since 1892, with data on location, homecoming, and national bowl games

[Download the full dataset as a single CSV file](https://raw.githubusercontent.com/wadefagen/datasets/master/illini-football/illini-football-scores.csv)

## Data Format

The first row of the CSV file contains column headers. Every row after the first contains data. Sample:

| Season | Date | Location | Opponent | Result | IlliniScore | OpponentScore | Note |
| ------ | ---- | -------- | -------- | ------ | ----------- | ------------- | ---- |
| 2019 | 2018-08-31 | vs. | Akron | W | 42 | 3 |  |
| ... |
| 2014 | 2014-10-11 | @ | Wisconsin | L | 28 | 38 |  |
| 2014 | 2014-10-25 | vs. | Minnesota | W | 28 | 24 | Homecoming |
| ... |
| 1963 | 1964-01-01 | Pasadena, CA | Washington | W | 17 | 7 | Rose Bowl |

### Notes on Data

- `Season` refers to the football season.  January bowl games occur in the next calendar year (but in the previous year's season).

- `Location` is one of the following:
  * `vs.`, for Illini home games
  * `@`, for away games played at the opponent's home stadium
  * `Town, State`, for games played at another site (ex: `Pasadena, CA`)

- `Note` contains notes on homecoming games (value: `Homecoming`) and bowl games.

## Projects Using this Dataset

1. [Illini Nation through 120+ Years of Illini Football](http://waf.cs.illinois.edu/discovery/illini_nation_through_120_years_of_illini_football/), 
2. [120 Years of Illini Football, By Coach](http://waf.cs.illinois.edu/discovery/120_years_of_illini_football_by_coach/)

*If you create a project with this dataset, I'd love to link it here!  Send a PR with your project added to this list!*

## Data Source

Data in this dataset was compiled into CSV format from two sources:

- Wikipedia pages on Illini Football seasons (ex: https://en.wikipedia.org/wiki/2001_Illinois_Fighting_Illini_football_team)
- fightingillini.com's "University of Illinois Homecoming", https://fightingillini.com/sports/2016/8/18/football-homecoming.aspx
