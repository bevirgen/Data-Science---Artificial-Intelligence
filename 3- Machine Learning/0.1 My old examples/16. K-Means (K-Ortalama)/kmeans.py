import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#veri yukleme

veri = pd.read_csv('musteriler.csv')


#k-means 
    #clusterlar ve init değiştirilerek başarı oranı değiştirilebilir.
X = veri.iloc[:,3:].values

from sklearn.cluster import KMeans

kmeans = KMeans ( n_clusters=3, init="k-means++")
kmeans.fit(X)
print(kmeans.cluster_centers_)

sonuclar = []

for i in range(1,11) :
    kmeans = KMeans ( n_clusters=i, init="k-means++", random_state=123)
    kmeans.fit(X)
    sonuclar.append(kmeans.inertia_)
    
plt.plot(range(1,11),sonuclar)

