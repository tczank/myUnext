---
title:
- Short Test

subtitle:
- Improving users use rate

author: |
 | [Thomas Czank](sendto:thomas.czank@gmail.com)

urlcolor: red

theme:
- metropolis

fonttheme: professionalfonts
mainfont: "HaranoAjiMincho-Regular.otf"
mainfontoptions:
      - BoldFont=HaranoAjiMincho-Bold
      - ItalicFont=RobotoMono-LightItalic
sansfont: "NotoSans-Regular"
monofont: "JetBrainsMono-Regular"

themeoptions: "progressbar=foot, block=fill, background=light"

date:
- 2024, October 25th

header-includes:

- \usepackage{appendixnumberbeamer}
- \usepackage{booktabs}
- \usepackage{longtable}
- \usepackage{array}
- \usepackage{multirow}
- \usepackage{wrapfig}
- \usepackage{float}
- \usepackage{colortbl}
- \usepackage{pdflscape}
- \usepackage{tabu}
- \usepackage{xcolor}
- \usepackage{threeparttable}
- \usepackage{soul}
- \usepackage{minted}
- \usepackage{hyperref}
- \hypersetup{colorlinks=true, urlcolor=magenta, linkcolor=red}
- \newcommand{\columnsbegin}{\begin{columns}}
- \newcommand{\columnsend}{\end{columns}}
- \AtBeginSubsection{}
- \AtBeginSection{}
- \makeatletter
- \setlength{\metropolis@titleseparator@linewidth}{2pt}
- \setlength{\metropolis@progressonsectionpage@linewidth}{2pt}
- \setlength{\metropolis@progressinheadfoot@linewidth}{2pt}
- \makeatother

fontsize: 10pt
---

# Outline

\tableofcontents

# Preparation

\tableofcontents[currentsection]

## Setting up the environment


**Analysis Preservation**

1. Setting up a `git` repository
2. Creating a `conda` environment
3. installing required packages
4. exporting the `env` package list


This analysis environment is now documented enough to be saved from breaking upon future software updates

## The Problem?


## Feature engineering - Data cleaning

 * Are there `null` entries?
 * Are there `NaN` entries?
 * How to deal with them?
 
 * In this case 7 `user_id` were not available
 * So these entries were deleted
 * total entries 23242 $\rightarrow$ 23235

## Feature engineering - Data transformation

 * Initially, these are all `objects` (`strings`):
   1. `log_date`
   2. `view_start_time`
   3. `view_end_time`
   
 * They were transformed into `datetime`
 * And new variables were calculated:
   1. `view_duration(s)`
   2. `log_date` was divided into `year` `month` and `day`

## Feature overview

|  | `ep_type` | `ep_id`	| `show_id` |	`user_id`	| `log_date` |
|----- | ------  | ----- | ----- | ---- |-----------|
|count |23235 |	23235 |	23235 |	23235 |	23235 |
|unique |	3 |	7275 | 384 | 999 | 60 |
|top |	b	| ep5 |	s4 |	uu43 | 2024-03-03 |
|freq |	13684 |	408 |	2253 |	1226 |	854 |

* There are __7275__ unique _episodes_
* There are __384__ unique _shows_
* There are __999__ unique _users_
* The most popular `episode_type` is b
* The most popular `episode_id` is `ep00000005`
* The most popular `show_id` is `s00000004`

# Confirming the problem preliminary conditions

\tableofcontents[currentsection]

## Confirming the problem preliminary conditions



# Exploratory Data Analysis (EDA)

## 変数チェック`episode_id`

```python
def hello():
    print("Hello World!")
```

## Looking at the variables: `episode_type`

## Looking at the variables: ...

# Key variables

# Conclusion

