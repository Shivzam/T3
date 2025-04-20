import pytest
import pandas as pd
from titanic_analysis import TitanicAnalysis

@pytest.fixture
def titanic():
    return TitanicAnalysis("train.csv")

def test_clean_data(titanic):
    titanic.clean_data()
    assert 'Cabin' not in titanic.df.columns  # Ensure irrelevant columns are removed
    assert titanic.df.isnull().sum().sum() == 0  # Ensure missing values are handled

def test_transform_data(titanic):
    titanic.clean_data()
    titanic.transform_data()
    assert 'class' in titanic.df.columns
    assert 'who' in titanic.df.columns
    assert 'adult_male' in titanic.df.columns
    assert 'embark_town' in titanic.df.columns
    assert 'alive' in titanic.df.columns
    assert 'alone' in titanic.df.columns
    assert 'family_size' in titanic.df.columns
    
    # Check correct mapping for 'class'
    assert set(titanic.df['class'].unique()).issubset({'First', 'Second', 'Third'})
    
    # Check 'who' column values
    assert set(titanic.df['who'].unique()).issubset({'man', 'woman', 'child'})
    
    # Check 'adult_male' values are boolean
    assert titanic.df['adult_male'].dtype == bool
    
    # Check 'embark_town' values
    assert set(titanic.df['embark_town'].dropna().unique()).issubset({'Cherbourg', 'Queenstown', 'Southampton'})
    
    # Check 'alive' values
    assert set(titanic.df['alive'].unique()).issubset({'yes', 'no'})
    
    # Check 'alone' values are boolean
    assert titanic.df['alone'].dtype == bool
    
    # Check family size is at least 1
    assert (titanic.df['family_size'] >= 1).all()



def test_get_summary(titanic):
    summary = titanic.get_summary()
    assert isinstance(summary, pd.DataFrame)
    assert not summary.empty

def test_get_missing_values(titanic):
    titanic.clean_data()
    titanic.transform_data()
    missing = titanic.get_missing_values()
    assert isinstance(missing, pd.Series)
    assert missing.sum() == 0  # Ensure missing values are handled

def test_get_fare_mean(titanic):
    titanic.clean_data()
    titanic.transform_data()
    fare_mean = titanic.get_fare_mean()
    assert isinstance(fare_mean, float)
    assert fare_mean > 12

def test_survival_rate_by_column(titanic):
    titanic.clean_data()
    titanic.transform_data()
    result = titanic.survival_rate_by_column('class')
    assert isinstance(result, pd.Series)
    assert not result.empty
    assert (result >= 0).all() and (result <= 1).all()  # Ensure rates are valid probabilities

def test_survival_count_by_family_size(titanic):
    titanic.clean_data()
    titanic.transform_data()
    result = titanic.survival_count_by_family_size()
    assert isinstance(result, pd.Series)
    assert not result.empty
    assert (result >= 0).all()  # Ensure survival counts are non-negative

def test_fare_statistics_by_class(titanic):
    titanic.clean_data()
    titanic.transform_data()
    result = titanic.fare_statistics_by_class()
    assert isinstance(result, pd.DataFrame)
    assert not result.empty
    assert all(col in result.columns for col in ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'])  # Check key statistics exist