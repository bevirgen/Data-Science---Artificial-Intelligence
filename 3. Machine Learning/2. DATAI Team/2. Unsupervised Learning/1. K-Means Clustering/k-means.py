# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 11:41:06 2020

@author: berka
"""

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# %% preparing data

x1 = np.random.normal(25,5,1000)
y1 = np.random.normal(25,5,1000)

x2 = np.random.normal(55,5,1000)
y2 = np.random.normal(60,5,1000)

x3 = np.random.normal(55,5,1000)
y3 = np.random.normal(15,5,1000)

x=np.concatenate((x1,x2,x3), axis=0)
y=np.concatenate((y1,y2,y3), axis=0)

dictionary={'x':x, 'y':y}
data=pd.DataFrame(dictionary)

# k-means algorithm sees data like that
plt.scatter(x1,y1, c='black')
plt.scatter(x2,y2, c='black')
plt.scatter(x3,y3, c='black')
plt.show()
# %% searching best number of k value

wcss = []

for k in range(1,15):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,15),wcss)
plt.xlabel('Number of Cluster(k)')
plt.ylabel('WCSS')
plt.show()
# %% k-means

kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(data)

data['label'] = clusters
# well, was k-means clustered data successfully?
plt.scatter(data.x[data.label==0],data.y[data.label==0],c='green')
plt.scatter(data.x[data.label==1],data.y[data.label==1],c='blue')
plt.scatter(data.x[data.label==2],data.y[data.label==2],c='red')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],c='yellow')
plt.show()