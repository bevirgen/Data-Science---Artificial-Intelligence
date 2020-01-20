# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 14:12:10 2020

@author: berka
"""

from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# %% preparing data

x1 = np.random.normal(25,5,100)
y1 = np.random.normal(25,5,100)

x2 = np.random.normal(55,5,100)
y2 = np.random.normal(60,5,100)

x3 = np.random.normal(55,5,100)
y3 = np.random.normal(15,5,100)

x=np.concatenate((x1,x2,x3), axis=0)
y=np.concatenate((y1,y2,y3), axis=0)

dictionary={'x':x, 'y':y}
data=pd.DataFrame(dictionary)
# machine sees data like that
plt.scatter(x1,y1, c='black')
plt.scatter(x2,y2, c='black')
plt.scatter(x3,y3, c='black')
plt.show()
# %% dendogram
merg = linkage(data, method='ward')
dendrogram(merg,leaf_rotation = 90)
plt.xlabel('Data Points')
plt.ylabel('Euclidean Distance')
plt.show()
# %% hierarchical clustering
hierarchical_cluster = AgglomerativeClustering(n_clusters = 3, affinity='euclidean', linkage='ward')
cluster = hierarchical_cluster.fit_predict(data)
data['label'] = cluster

plt.scatter(data.x[data.label==0],data.y[data.label==0],c='green')
plt.scatter(data.x[data.label==1],data.y[data.label==1],c='blue')
plt.scatter(data.x[data.label==2],data.y[data.label==2],c='red')
plt.show()