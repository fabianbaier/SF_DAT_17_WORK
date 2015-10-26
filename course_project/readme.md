Question and Data Set for Final Project

###What is the question you hope to answer? 
I'm planning to predict earthquakes in California.

###What data are you planning to use to answer that question? 
I'm planning to predict earthquakes in California.
I will use certain data from different pages like earthquaketrack.com, scedc.caltech.edu/recent, etc..

###What do you know about the data so far? 
I know not much about all the data so far but I am curious to find correlations.

###Why did you choose this topic?
I chose this topic because a friend of mine told me that Yahoo can predict the weather of the next 15hours in New York more precise through the amount of socks sold in the last 24hours then the weatherstations. I thought, having new relations through big data and machine learning where yet no connection exists is interesting. Maybe this leads to an complete unexpected new topic where I can predict certain stock market behaviour based on earthquakes er so.

http://earthquake.usgs.gov/earthquakes/search/

###Problem statement and hypothesis
Weather impacts the magnitude of earthquakes.

###Description of your data set and how it was obtained
For earthquakes: Downloaded it through http://earthquake.usgs.gov/earthquakes/search/
For weather: Downloaded it through http://w2.weather.gov/climate/xmacis.php?wfo=mtr


###Description of any pre-processing steps you took
Downloaded manually monthly weather data and consolidated it in one big csv file. 
Assigned each day with the corresponding weather.
Converted categorical to numerical.


###What you learned from exploring the data, including visualizations
I looked at the MaxTemp of each day. Hypthesis is not true. Need to look out for better explaining data.
Looks like MaxTemp is not correlated at all.

###How you chose which features to use in your analysis
Looking at scatter plots for some relation.

###Details of your modeling process, including how you selected your models and validated them
See files. Did machine learning with sklearn to predict the magnitude of an earthquake based on the MaxTemp with 0.82 accuracy,

###Your challenges and successes
Data was not clean and scattered over different sources. Consolidation and the right formatting (nump array/dimension of the dataframe/ etc.) was very challenging. This all was needed to just get a first glimpse on how the data could look like. Yet, not at all with any insight. Once I got rid of this road block I saw the data wasn't useful anyways. Currently on the lookout for more explanatory data that could help me in my hypothesis testing.

###Possible extensions or business applications of your project
Getting value from micro earthquakes to recognize bigger patterns for a warning system.

###Conclusions and key learnings
Weather does not statistically significat impact the earthquake magnitude.