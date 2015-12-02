# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 11:55:39 2015

@author: fabianbaier
"""

cd /Users/fabianbaier/Documents/GA Data Science/SF_DAT_17_WORK/course_project/data
#Importing necessary packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import statsmodels.formula.api as smf
import seaborn as sns
import Quandl
#Using the magic variable
%matplotlib inline

eq = pd.read_csv('eq1977-2015.csv')
eq.info()

eq.columns

eq.shape

eq.head()

eq.describe()

print eq.sort_index(by='mag',ascending=False)

#eq['time'] = pd.DatetimeIndex(eq['time']).to_period('D')

eq.plot(x='time', y='mag', style=".")

sns.heatmap(eq.corr())

eq.corr()


lm = smf.ols(formula='time ~ mag', data=eq).fit()

'''
MACHINE LEARNING WITH KNN
'''    
X, y = eq['mag'], eq['place']
y = eq['place']

for i in range(1, 6):
    knn = KNeighborsClassifier(n_neighbors=i)
    X = X.reshape(6055,1)
    y = y.reshape(6055,)
    knn.fit(X, y) 
    print 'With ',i,' neighbor:', knn.score(X, y)
    
    
data = Quandl.get("BEA/GSP_NAICS_ALL_C_CALIFORNIA")
data.tail()

quandlapikey='Z8qVjfqK6crG5T_Ur4g2'
mydata = Quandl.get("WGC/GOLD_DAILY_USD", authtoken=quandlapikey)


