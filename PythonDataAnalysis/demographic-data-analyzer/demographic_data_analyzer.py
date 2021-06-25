import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv",delimiter=',')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(np.mean(df[df['sex'] == 'Male']['age']),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(len(df[df['education'] == 'Bachelors']['sex']) / len(df) * 100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    all_higher_education = df.loc[(df["education"].str.startswith("B")) | (df["education"].str.startswith("M")) | (df["education"].str.startswith("D"))]
    high_income_higher_edu = len(df.loc[(df["education"].str.startswith("B")) | (df["education"].str.startswith("M")) | (df["education"].str.startswith("D"))][df["salary"] == ">50K"])
    high_income_lower_edu = len(df.loc[df["salary"] == ">50K"]) -  high_income_higher_edu

    # percentage with salary >50K
    higher_education_rich = round(100 * high_income_higher_edu / len(all_higher_education),1)
    lower_education_rich = round(100 * high_income_lower_edu / (len(df) - len(all_higher_education)),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_work = df.loc[(df["hours-per-week"] == min_work_hours)]
    num_min_workers = df.loc[(df["hours-per-week"] == 1) & (df["salary"] == ">50K")]

    rich_percentage = round(100 * len(num_min_workers) / len(min_work) , 1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (df.loc[(df["salary"] == ">50K")]["native-country"].value_counts() / df["native-country"].value_counts()).sort_values(ascending = False).index[0]
    highest_earning_country_percentage = round(100 * (df.loc[(df["salary"] == ">50K")]["native-country"].value_counts() / df["native-country"].value_counts()).max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (df.loc[(df["salary"] == ">50K") & ( df["native-country"] == "India")]["occupation"])
    top_IN_occupation = pd.Series.mode(top_IN_occupation)[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
