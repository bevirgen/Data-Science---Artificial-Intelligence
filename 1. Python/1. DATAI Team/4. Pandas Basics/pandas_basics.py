# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 09:47:47 2019

@author: berka
"""

# why need pandas? fast and effective for dataframes
# pandas can open and analyze csv and text files , and it can save our results easily save
# pandas make our job easy for missing data
# we can do reshape data and use effectively
# slicing and indexing is easy on pandas
# very help fully in time series data analysis
# most important : speed ,pandas is optimised speed one library

import numpy as np
import pandas as pd

mydict = {"Names":["Ali","Veli","Kenan","Hilal","Ayse","Evren"],
          "Ages" :[33,22,54,44,23,27],
          "Salaries" :[100,134,156,188,215,356]}

df1 = pd.DataFrame(mydict)

head = df1.head() # give first 5 row , generally using for preliminary examination
tail = df1.tail() # last 5 row
tail2row = df1.tail(2) #last 2 row
# %% pandas basic methods

print(df1.columns) # just columns names
print("\n",df1.info()) # informations about dataframe
print("\n", df1.dtypes) # just column types
print("\n",df1.describe()) # describe method only takes numeric features
# %% indexing and slicing

# pandasta indexlemede [x:y, z:t] y ve t ler inclusive yani indexlemeye dahildir
print(df1["Names"]) # just Names column
print(df1.Names) # same thing above row

df1["New_Column"] = [-1,-2,-3,-4,-5,-6]
print(df1.loc[:, "Ages"])
df1.loc[0, 1:2] = 24 # ilk satır (Ali), 1.kolon (Ages) = 24
df1.loc[2, "Ages"]=70 # 3. satır , Ages kolonu = 70
print(df1.Ages)

print(df1.loc[:3, "Ages":"New_Column"]) # görüldüğü gibi 3.satır ve New column aralıkları dahil
print(df1.loc[:3, ["Ages","New_Column"]]) # that is not slicing > burada aralık yok seçim var, Ages ve New column seçildi, aralık verilmedi

print(df1.loc[::-1,]) # satıra göre tersten sırala
print(df1.loc[:, :"Salaries"]) # Salaries aralığına kadar olan verileri al

print(df1.iloc[:,2]) # iloc > indexe göre slice yapmak (analiz etmek,bulmak), tüm satırlar dahil, 2.indexi al yazıldı
# %% filtering

filter1 = df1.Salaries > 200
filtered_data = df1[filter1] # take filter1 table in df1 dataframe

filter2= df1.Ages < 27
df1[filter1 & filter2] # combine filter1 and filter2 and filter it

#veya numpy kullanarak şu şekilde yapılabilir

filter3 = np.logical_and(df1.Salaries > 200, df1.Ages < 27)
filtered_data2 = df1[filter3]

# the handy method is when filtering data :

filtered_data3 = df1[np.logical_and(df1.Ages > 25, df1.Salaries > 150)] # this way is better
# %% list comprehension

mean_salary = df1.Salaries.mean() # take mean of salaries
upper_of_mean = df1[df1.Salaries > df1.Salaries.mean()] # taking salary upper of mean
lower_of_mean =df1[df1.Salaries < df1.Salaries.mean()] # taking salary lower of mean

df1["salary_level"] = ["higher" if each > mean_salary else "lower" for each in df1.Salaries]

df1.columns = [each.lower() for each in df1.columns] # do lower column names
df1["yeni sutun"] = [-1,-2,0,3,5,8]
df1.columns = [each.split()[0] + "_" + each.split()[1] if len(each.split()) > 1 else each for each in df1.columns] # kolon ismi boslukluysa "_" koy
# %% drop and concetaning

df1.drop(["yeni_sutun"],axis=1, inplace = True) # drop "yeni_sutun" column and apply it on dataframe

dt1 = df1.head()
dt2 = df1.tail()

data_v_concat = pd.concat(df1.head(), df1.tail(), axis = 0) # same thing bottom row
#data_v_concat = pd.concat([dt1,dt2], axis = 0) # concat columns vertical

#dt3 = df1.SALARIES
#dt4 = df1.AGES
df1.columns = [each.lower() for each in df1.columns] # do lower column names

data_h_concat = pd.concat(df1.salaries,df1.ages, axis = 1)
# %% transforming data

df1["list_comp"] = [each * 2 for each in df1.ages]

# apply method

def multiply(age):
    return age*2

df1["apply_method"] = df1.ages.apply(multiply)















