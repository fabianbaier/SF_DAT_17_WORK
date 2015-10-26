# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 09:29:05 2015

@author: fabianbaier
"""

# # Linear Regression
# *Adapted from Chapter 3 of [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/)*

# # Part 1: Introduction
# - **Classification problem:** supervised learning problem with a categorical response
# - **Regression problem**: supervised learning problem with a continuous response
# - **Linear regression:** machine learning model that can be used for regression problems

# Why are we learning linear regression?
# - widely used
# - runs fast
# - easy to use (no tuning is required)
# - highly interpretable
# - basis for many other methods

# Lesson goals:
# - Conceptual understanding of linear regression and how it "works"
# - Familiarity with key terminology
# - Ability to apply linear regression to a machine learning problem using scikit-learn
# - Ability to interpret model coefficients
# - Familiarity with different approaches for feature selection
# - Understanding of three different evaluation metrics for regression
# - Understanding of linear regression's strengths and weaknesses

# ## Libraries
# - [Statsmodels](http://statsmodels.sourceforge.net/): "statistics in Python"
#     - robust functionality for linear modeling
#     - useful for teaching purposes
#     - will not be used in the course outside of this lesson
# - [scikit-learn](http://scikit-learn.org/stable/): "machine learning in Python"
#     - significantly more functionality for general purpose machine learning

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import statsmodels.formula.api as smf

# visualization
import seaborn as sns
import matplotlib.pyplot as plt

# ## Reading the advertising data

# read data into a DataFrame

weather = pd.read_csv('data/weather.csv')

weatherdf = pd.DataFrame(weather)

import pandas as pd
eq = pd.read_csv('data/eq.csv')

def weathereq():
    for i in range(eq.time.shape[0]):
        end = eq.time[i].find('T') # We are just interested in the date not the time
        date = eq.time[i][:end] # Getting the date, like 2014-12-24
        maxtemp = weatherdf[weatherdf.Date == date].Max # Finding the date in the weather data set
        maxtemp = maxtemp.values[0] # Getting the max temperature value
        eq.set_value(i, 'MaxTemp', maxtemp) # Adding the max temperature to the specific day

# Turning all events into the day they happened
eq['time'] = pd.DatetimeIndex(eq['time']).to_period('D')
eq['time'] = pd.Categorical.from_array(eq['time']).codes

# Turning categorical data to number
eq['place'] = pd.Categorical.from_array(eq['place']).codes

# Looking at the data
sns.pairplot(eq, x_vars=['time', 'place', 'latitude', 'longitude', 'depth',
       'nst', 'gap', 'dmin', 'rms', 'MaxTemp'], y_vars='mag', size=4.5, aspect=0.7, kind='reg')

# Scatter plot Pandas
eq.plot(kind='scatter', x='time', y='mag', figsize=(16, 6))
eq.plot(kind='scatter', x='place', y='mag')
eq.plot(kind='scatter', x='MaxTemp', y='mag')

# Not really a correlation