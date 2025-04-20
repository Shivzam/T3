import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class TitanicAnalysis:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)
        
    
    """ Data Cleaning
    - Dropping irrelevant columns (`Cabin`, `Ticket`, `Name`)
    - Filling missing values in `Age` with the mean and `Embarked` with the most common value
    """
    def clean_data(self):
        ## ADD YOUR CODE HERE
    
    """ Data Transformation
    - Creating new columns such as `class`, `who`, `adult_male`, `embark_town`, `alive`, `alone`, and `family_size`
    - Grouping passengers into age categories
    # Transforms the dataset: create new columns based on condition
    # 1 - create a new column called 'class' such that the values are the strings "First", "Second", or 'Third" when the column 'Pclass' has value 1,2,3 respectively
    # 2 - create a new column called 'who' such that the values are "woman", "man", or "child", depending on the values of the columns "Age" and "Sex". Use the function "woman_child_or_man" provided
    # 3 - create a new column called 'adult_male" such that the value is 1 when the value of the column 'who' is man
    # 4 - create a new column called 'embark_town' such that the valies are "Cherbourg", "Queenstown", or "Southampton" if the passager has 'Embarked" in "C", "Q", or "S".
    # 5 - create a new column called 'alive' such that the value are 1 if the passenger survived, and 0 otherwise
    # 6 - create a new column called 'alone' such that the values is 'True' if the person does not have any siblings / spouses or  parents / children aboard the Titanic
    # 7 - create a new column called 'family_size' by conmbining the number of siblings/spouses and parents/children and the individual
    """
    def transform_data(self):
        self.df['class'] = ## ADD YOUR CODE HERE
        self.df['who'] = ## ADD YOUR CODE HERE
        self.df['adult_male'] = ## ADD YOUR CODE HERE
        self.df['embark_town'] = ## ADD YOUR CODE HERE
        self.df['alive'] = ## ADD YOUR CODE HERE
        self.df['alone'] = ## ADD YOUR CODE HERE
        self.df['family_size'] = ## ADD YOUR CODE HERE

    """
    Analysis Functions
    - Returns descriptive statistics of the dataset
    """
    def get_summary(self):
        return ## ADD YOUR CODE HERE

    """
    Analysis Functions
    - Identifies missing values
    """
    def get_missing_values(self):
        return ## ADD YOUR CODE HERE

    """
    Analysis Functions
    _ Return the mean of the fare prices
    """
    def get_fare_mean(self):
        return ## ADD YOUR CODE HERE

    """
    Analysis Functions
    - Computes survival rates based on a given column
    """
    def survival_rate_by_column(self, column):
        return ## ADD YOUR CODE HERE
    
    """
    Analysis Functions
    - Analyzes survival count by family size
    """
    def survival_count_by_family_size(self):
        return ## ADD YOUR CODE HERE
  
    """
    Analysis Functions
    - Returns fare stastics by class
    """
    def fare_statistics_by_class(self):
        return ## ADD YOUR CODE HERE
   

    """
    Visualizations
    - Visualize survival count plot
    """
    def visualize_survival(self):
        plt.figure(figsize=(8, 5))
        ## ADD YOUR CODE HERE
        plt.title('Survival Count')
        plt.show()

    """
    Visualizations
    Visualize fare distribution histogram
    """
    def visualize_fare_distribution(self):
        plt.figure(figsize=(8, 5))
        ## ADD YOUR CODE HERE
        plt.title('Fare Distribution')
        plt.show()

    """
    Visualizations
    Visualize age distribution by gender
    """
    def visualize_age_distribution(self):
        plt.figure(figsize=(8, 5))
        ## ADD YOUR CODE HERE
        plt.title('Age Distribution by Gender')
        plt.show()

    """
    Visualizations
    Visualize survival rate by passenger class
    """
    def visualize_survival_by_class(self):
        plt.figure(figsize=(8, 5))
        ## ADD YOUR CODE HERE
        plt.title('Survival Count by Class')
        plt.show()

    """
    Visualizations
    Visualize survival count by embarkation point
    """
    def visualize_survival_by_embark(self):
        plt.figure(figsize=(8, 5))
        ## ADD YOUR CODE HERE
        plt.title('Survival Count by Embarkation')
        plt.show()
    
    
    """
    Visualizations
    Box plot comparing fare and survival status
    """
    def compare_survival_by_fare(self):
        plt.figure(figsize=(8, 5))
        ## ADD YOUR CODE HERE
        plt.title('Comparison of Fare Paid by Survival Status')
        plt.show()
