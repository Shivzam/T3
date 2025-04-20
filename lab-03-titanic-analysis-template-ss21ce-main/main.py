from titanic_analysis import TitanicAnalysis

titanic = TitanicAnalysis("train.csv")

print("Dataset Summary:")
print(titanic.get_summary())

print("\nMissing Values:")
print(titanic.get_missing_values())

print("Clean Summary:")
titanic.clean_data()

print("Transform Dataset:")
titanic.transform_data()

print("Dataset Summary:")
titanic.get_summary()

print("\nMissing Values:")
print(titanic.get_missing_values())

print("\nFare Mean:")
print(titanic.get_fare_mean())

print("\nSurvival Rate by Class:")
print(titanic.survival_rate_by_column('class'))

print("\nSurvival Rate by Gender:")
print(titanic.survival_rate_by_column('Sex'))

print("\nSurvival Count by Family Size:")
print(titanic.survival_count_by_family_size())

print("\nFare Statistics by Class:")
print(titanic.fare_statistics_by_class())

print("\nGenerating Visualizations...")
titanic.visualize_survival()
titanic.visualize_fare_distribution()
titanic.visualize_age_distribution()
titanic.visualize_survival_by_class()
titanic.visualize_survival_by_embark()
titanic.compare_survival_by_fare()

print("Analysis complete!")