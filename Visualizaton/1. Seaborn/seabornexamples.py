# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:19:46 2019

@author: berka
"""

#seaborn library (for visualization)

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from collections import Counter

#importing datas
MedianHouseholdIncome = pd.read_csv("MedianHouseholdIncome2015.csv",encoding="cp1252")
PercentagePeopleBelowPovertyLevel = pd.read_csv("PercentagePeopleBelowPovertyLevel.csv",encoding="cp1252")
PercentOver25CompletedHighSchool = pd.read_csv("PercentOver25CompletedHighSchool.csv",encoding="cp1252")
PoliceKillingsUS = pd.read_csv("PoliceKillingsUS.csv",encoding="cp1252")
ShareRaceByCity = pd.read_csv("ShareRaceByCity.csv",encoding="cp1252")
# %% poverty rate of each state - eyaletlerdeki fakirlik oranı

PercentagePeopleBelowPovertyLevel.head()
# looking for missing values
PercentagePeopleBelowPovertyLevel.poverty_rate.value_counts()

# 201 missing value , what we should do ? Sync to 0
PercentagePeopleBelowPovertyLevel.poverty_rate.replace(['-'],0.0, inplace=True)
PercentagePeopleBelowPovertyLevel.poverty_rate = PercentagePeopleBelowPovertyLevel.poverty_rate.astype(float)

area_list = list(PercentagePeopleBelowPovertyLevel['Geographic Area'].unique()) # make list states
len(PercentagePeopleBelowPovertyLevel['Geographic Area'].unique()) #51 states

area_poverty_ratio = []

# average poverty rate for each states
for i in area_list:
    x = PercentagePeopleBelowPovertyLevel[PercentagePeopleBelowPovertyLevel['Geographic Area'] == i]
    area_poverty_rate = sum(x.poverty_rate) / len(x)
    area_poverty_ratio.append(area_poverty_rate)

# do dataframe it
data = pd.DataFrame({'area_list': area_list, 'area_poverty_ratio': area_poverty_ratio})
new_index = (data['area_poverty_ratio'].sort_values(ascending=False)).index.values #sorting , ascending = decreasing
sorted_data = data.reindex(new_index)

# visualizaton
plt.figure(figsize=(13,8))
sns.barplot(sorted_data['area_list'], sorted_data['area_poverty_ratio'])
plt.xticks(rotation = 60) # put xlabels 60 degrees
plt.xlabel('States')
plt.ylabel('Poverty Rate')
plt.title('Poverty Rate of States')
#%% Most common 15 Name or Surname of killed people

# PoliceKillingsUS.name.value_counts()
seperate = PoliceKillingsUS.name[PoliceKillingsUS.name != 'TK TK'].str.split() # take data who hasn't name 'TK TK' as string
a,b = zip(*seperate) # unzipping
name_list = a+b
name_count = Counter(name_list)
most_common_names = name_count.most_common(15)
# take them as list for visualization
d,c = zip(*most_common_names)
d,c = list(d), list(c)
# visualizaton
plt.figure(figsize=(13,8))
sns.barplot(d, c, palette= sns.cubehelix_palette(len(x)))
# palette > uzunluk sayısı kadar birbiriyle uyumlu farklı renk şeklinde çizdirir
plt.xlabel('Name or Surname of killed Person')
plt.ylabel('Frequency')
plt.title(' Most common 15 Name or Surname of killed people')

