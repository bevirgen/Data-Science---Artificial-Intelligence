# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 13:58:05 2019

@author: berka
"""

# matplotlib library
# visualization library
# line plot , scatter plot, bar plot, subplots, histogram

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("iris.csv") # read csv and do it dataframe

print(df.columns)
print(df.Species.unique()) # how much variable under species column
print(df.info()) # df's info
print(df.describe(),"\n")
print(df.PetalLengthCm.describe()) # data's describes

#print(setosa.describe(),"\n")
#print(versicolor.describe())
# %% matplot > line

df1 = df.drop(["Id"], axis = 1)

#df1.plot() # get table datas for df1
#plt.show() # show table

setosa = df[df.Species == "Iris-setosa" ]
versicolor = df[df.Species == "Iris-versicolor" ]
virginica = df[df.Species == "Iris-virginica" ]

plt.plot(setosa.Id, setosa.PetalLengthCm, color = "red", label = "Setosa") # x , y, color , label > title
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color = "green", label = "Versicolor")
plt.plot(virginica.Id, virginica.PetalLengthCm, color = "blue", label = "Virginica")
plt.title("Statistic Of Petallengths")
plt.xlabel("Id") # rowline label (x)
plt.ylabel("PetalLengthCm") # columnline label (y)
plt.legend() # show titles (labels)
plt.show()
# %%

df1.plot(grid = True, linestyle = ':') # sayfa karelerini göster, çizgi şekli : , saydamlık : çok saydam
plt.show()
# %% scatter plot

plt.scatter(setosa.SepalLengthCm, setosa.PetalWidthCm, color = "red", label="setosa")
plt.scatter(versicolor.SepalLengthCm, versicolor.PetalWidthCm, color = "green", label="versicolor")
plt.scatter(virginica.SepalLengthCm, virginica.PetalWidthCm, color = "purple", label="virginica")
plt.title("Scatter Plot")
plt.xlabel("SepalLengthCm")
plt.ylabel("PetalWidthCm")
plt.legend()
plt.show()

# işlemler : önce hepsini sepallength ve petalwidh (x,y) ye göre plot ettik ve renk verdik, ardından tablo işlemlerini yapıp görüntüledik
# %% histogram

plt.hist(setosa.PetalLengthCm, bins = 18) # hist table, bins > çubuklar, setosa verisi ile denk olursa tam değerlere ulaşılacaktır
plt.xlabel("PetalLengthCm Values")
plt.ylabel("Frequency - Count")
plt.title("Histogram")
plt.show()
# %% bar plot

x = np.array([1,2,3,4,5,6])
countries = ["Turkey","Germany","USA","China","Canada","England"]
y = x *2 +5

plt.bar(countries, y) # bar table
plt.title("Bar Plot")
plt.xlabel("Countries")
plt.ylabel("Per Capita Income")
plt.show()
# %% subplot

setosa = df[df.Species == "Iris-setosa" ]
versicolor = df[df.Species == "Iris-versicolor" ]
virginica = df[df.Species == "Iris-virginica" ]

plt.subplot(2,1,1) #(2 satır , 1 sütun luk matrisin ilk verisi)
plt.plot(setosa.Id, setosa.PetalLengthCm, color = "red", label = "Setosa")
plt.ylabel("Setosa - PetalLengthCm")

plt.subplot(2,1,2)#(2 satır , 2 sütun luk matrisin ilk verisi)
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color = "green", label = "Versicolor")
plt.ylabel("Versicolor - PetalLengthCm")
plt.show()
















