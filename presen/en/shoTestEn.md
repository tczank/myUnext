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

