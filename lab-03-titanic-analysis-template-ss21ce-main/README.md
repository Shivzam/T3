# Titanic Analysis Project

## Overview
The sinking of the RMS Titanic is one of the most infamous shipwrecks in history. On April 15, 1912, during her maiden voyage, the Titanic sank after colliding with
an iceberg, killing 1502 out of 2224 passengers and crew. This tragedy shocked the international community and led to better safety regulations for ships.

One of the reasons that the shipwreck led to such loss of life was that there were not enough lifeboats for the passengers and crew. Although there was some element of luck involved in surviving the sinking, some groups of people were more likely to survive than others, such as women, children, and the upper-class.

You are asked to do an analysis of the sinking of the RMS Titanic. This implementation includes tasks such as visualizing the distribution of ages of the passengers, analyzing survival rates based on passenger class, analyzing survival rates based on the embarkation port, and analyzing survival counts based on family size.

## Dataset
The dataset used for this analysis is `train.csv`, which contains information about passengers on the Titanic, including:

|Variable|	Definition|	Key|
|--------|------------|-------|
|Survived|	Survival|	    0 = No, 1 = Yes|
|Pclass|	    Ticket class|	1 = 1st, 2 = 2nd, 3 = 3rd|
|Sex|	        Sex||
|Age|	        Age in years||
|SibSp|	    # of siblings / spouses aboard the Titanic||
|Parch|	    # of parents / children aboard the Titanic||
|Ticket|	    Ticket number||
|Fare|	    Passenger fare||
|Cabin|	    Cabin number||
|Embarked|	Port of Embarkation|C = Cherbourg, Q = Queenstown, S = Southampton|


## Methods
The project consists of the following key steps:
1. **Data Cleaning**
   - Dropping irrelevant columns (`Cabin`, `Ticket`, `Name`)
   - Filling missing values in `Age` with the mean and `Embarked` with the most common value
2. **Data Transformation**
   - Creating new columns such as `class`, `who`, `adult_male`, `embark_town`, `alive`, `alone`, and `family_size`
   - Grouping passengers into age categories
3. **Analysis Functions**
   - `get_summary()`: Returns descriptive statistics of the dataset
   - `get_missing_values()`: Identifies missing values
   - `get_fare_mean(self)`: Return the mean of the fare prices
   - `survival_rate_by_column(column)`: Computes survival rates based on a given column
   - `survival_count_by_family_size()`: Analyzes survival count by family size
   - `fare_statistics_by_class()`: Provides fare statistics by passenger class
4. **Visualizations**
   - `visualize_survival()`: Survival count plot
   - `visualize_fare_distribution()`: Fare distribution histogram
   - `visualize_age_distribution()`: Age distribution by gender
   - `visualize_survival_by_class()`: Survival rate by passenger class
   - `visualize_survival_by_embark()`: Survival count by embarkation point
   - `compare_survival_by_fare()`: Box plot comparing fare and survival status

## Testing
The analysis functions are tested using `pytest` in `test_titanic_analysis.py`. The tests validate:
- Data cleaning and transformation processes
- Correctness of survival rate calculations
- Proper functioning of statistical analysis methods

## Running the Project
To run the analysis, use the following command:
```sh
python titanic_analysis.py
```
To run tests:
```sh
pytest test_titanic_analysis.py
```

## Dependencies
Install required libraries using:
```sh
pip install pandas numpy matplotlib seaborn pytest
```

## Conclusion
This project provides a structured approach to analyzing the Titanic dataset. The implemented methods allow for statistical exploration and visual analysis of survival trends.

