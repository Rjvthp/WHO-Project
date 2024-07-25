# WHO-Project
A data analysis project focusing on hypothesis testing using WHO data. This repository contains Python scripts for data processing and analysis, utilizing libraries like NumPy, Pandas, and SciPy. It includes a final report demonstrating statistical methods and insights.
## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Usage](#usage)
4. [Hypothesis Testing](#hypothesis-testing)
5. [Report](#report)
6. [Contribution](#contribution)
7. [License](#license)

## Introduction

The WHO-Project is designed to analyze and interpret data related to the use of WHO checklist. The main goal of this project is to examine the use of the WHO provided checklist by the medical staffs.

### Project Overview

This project involves several key components:
- **Data Collection**: Gathering relevant data from Hospitals.
- **Data Analysis**: Using Python and statistical methods to analyze the data.
- **Reporting**: Documenting the findings and insights in comprehensive reports.

### Objectives

- To provide insights into different factors that affects the robust use of the WHO checklist.

### Significance

Understanding the factors that affects the use of the checklist is crucial for improving public health outcomes. This project aims to contribute valuable insights and actionable information to support these efforts.

## Getting Started

To replicate the results of this project, follow these steps:

### Prerequisites

- **Python 3.x**: Ensure Python 3 is installed on your system.
- **Required Python libraries**: Install the required libraries listed in `requirements.txt`.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rjvthp/WHO-Project.git
## Usage

## Hypothesis Testing

### Overview

Hypothesis testing is a statistical method used to make inferences about a population based on sample data. In this project, hypothesis testing is used to determine the validity of various assumptions regarding the data collected.

### Hypotheses and Assumptions

- **Null Hypothesis (H0)**: There is no significant difference between the groups being compared.
- **Alternative Hypothesis (H1)**: There is a significant difference between the groups being compared.

**Assumptions**:
- The data samples are independent.
- The data follows a normal distribution.
- The variances of the populations are equal (for certain tests).

### Methods Used

- **Chi-Square Test**: Used to determine if there is a significant association between categorical variables.
  - **Implementation**: Using `scipy.stats.chi2_contingency`.

- **T-Test**: Used to compare the means of two groups.
  - **Implementation**: Using `scipy.stats.ttest_ind`.

### Results and Interpretation

- Check the Report.pdf for more clarity.
## Report

The detailed analysis and findings of this project are documented in the report. You can view the report in the `Reports` directory of this repository.

### Viewing the Report

1. Navigate to the `Reports` directory:
   ```bash
   cd Reports







