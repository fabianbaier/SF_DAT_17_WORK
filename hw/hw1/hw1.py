'''
Move this code into your OWN SF_DAT_15_WORK repo

Please complete each question using 100% python code

If you have any questions, ask a peer or one of the instructors!

When you are done, add, commit, and push up to your repo

This is due 09/30/2015
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pd.set_option('max_colwidth', 50)
# set this if you need to

# where am I?
pwd
# change to my working directory
cd /Users/fabianbaier/Documents/GA\ Data\ Science/SF_DAT_17_WORK/hw/hw1

killings = pd.read_csv('data/police-killings.csv')
#killings.head()

# 1. Make the following changed to column names:

# lawenforcementagency -> agency
# raceethnicity        -> race

killings.rename(columns={'lawenforcementagency':'agency', 'raceethnicity':'race'}, inplace=True)
#killings.head()

# 2. Show the count of missing values in each column

killings.isnull().sum()
# apparently streetaddress has null values

# 3. replace each null value in the dataframe with the string "Unknown"
killings.streetaddress.fillna(value='Unknown', inplace=True)
# check if there are any missing values in each column
killings.isnull().sum()

# 4. How many killings were there so far in 2015?

# how many years are in the data set?
killings.year.value_counts()
# out: 467
# wait a minute
killings.info()
# apparently we have 467 entries, but also 467 rows with the year 2015
# that can just mean one thing:
# since we have no other year in the data set we have as many killings as observations
# those are the killings in 2015
killings[(killings.year==2015)]

# 5. Of all killings, how many were male and how many female?

# We have 445 male killings and 22 female killings
killings.gender.value_counts()


# 6. How many killings were of unarmed people?

killings[killings.armed=='No'].shape[0]
# We have 102 unarmed killings
killings.armed.value_counts()
# We also have to take into consideration that the Unknown could be unarmed

# 7. What percentage of all killings were unarmed?

from __future__ import division
# use // for integer division which rounds up to 0
killings[killings.armed=='No'].shape[0] / killings.shape[0]

# roughly 21.84% were unarmed

# 8. What are the 5 states with the most killings?

killings.state.value_counts(sort = True).head()
# Five Top states are: CA, TX, FL, AZ, OK


# 9. Show a value counts of deaths for each race

killings.race.value_counts(sort = True)
# Percentage of white deaths: 
killings.race.value_counts(sort = True)[0] / killings.shape[0]

# Percentage of black deaths: 
killings.race.value_counts(sort = True)[1] / killings.shape[0]

# Over 50 percent of those who got killed where white

# 10. Display a histogram of ages of all killings
%matplotlib inline

killings.age.hist()

# 11. Show 6 histograms of ages by race

killings.age.hist(by=killings.race, sharex=True, sharey=True)

# 12. What is the average age of death by race?

killings.groupby('race').age.mean()

# 13. Show a bar chart with counts of deaths every month

# By naming the columns after the datetime
killings['month_order'] = killings['month']
killings['month_order'].replace({'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}, inplace=True)
killings.groupby('month_order').day.count().plot(kind='bar', title='Deaths in 2015')

# By not sorting it
killings.groupby('month', sort=False).day.count().plot(kind='bar', title='Deaths in 2015')


###################
### Less Morbid ###
###################

majors = pd.read_csv('data/college-majors.csv')
majors.head()

# 1. Delete the columns (employed_full_time_year_round, major_code)

##del majors[Employed_full_time_year_round]
majors.drop('Employed_full_time_year_round', axis=1, inplace=True)

##del majors[Major_code]
majors.drop('Major_code', axis=1, inplace=True)

##check
majors.head()

# 2. Show the cout of missing values in each column

majors.isnull().sum()

# 3. What are the top 10 highest paying majors?

majors.sort(columns='Total', ascending=False).head(10)

# 4. Plot the data from the last question in a bar chart, include proper title, and labels!

top10payingmajors = majors.sort(columns='Total', ascending=False).head(10)
top10payingmajors.plot(x='Major', y='Total', kind='bar', title='10 highest paying majors')

# 5. What is the average median salary for each major category?

majors.groupby('Major_category', sort=False).Median.mean()

# 6. Show only the top 5 paying major categories

category_median_salary = majors.groupby('Major_category')[['Major_category', 'Median']].mean()
category_median_salary.head()
category_median_salary.sort('Median', ascending=False).head(5)

# 7. Plot a histogram of the distribution of median salaries

category_median_salary.shape
category_median_salary.plot(kind='hist', stacked=True, bins=16)


# 8. Plot a histogram of the distribution of median salaries by major category

category_median_salary.head(20).plot(by = majors.Major_category, kind='bar')

majors.plot(by = majors.Major_category, kind='hist')



# 9. What are the top 10 most UNemployed majors?

majors[['Major', 'Unemployed']].sort('Unemployed', ascending = False).head(10)

# What are the unemployment rates?

unemployment_rate = majors.Unemployed / majors.Total 
unemployment_rate

# 10. What are the top 10 most UNemployed majors CATEGORIES? Use the mean for each category

majors.groupby('Major_category')[['Major_category', 'Unemployed']].mean().sort('Unemployed', ascending = False).head(10)

# What are the unemployment rates?
unemployment_categories_rate = majors.groupby('Major_category').Unemployed.mean() / majors.groupby('Major_category').Total.mean()
unemployment_categories_rate


# 11. the total and employed column refer to the people that were surveyed.
# Create a new column showing the emlpoyment rate of the people surveyed for each major
# call it "sample_employment_rate"
# Example the first row has total: 128148 and employed: 90245. it's 
# sample_employment_rate should be 90245.0 / 128148.0 = .7042

# 12. Create a "sample_unemployment_rate" colun
# this column should be 1 - "sample_employment_rate"
