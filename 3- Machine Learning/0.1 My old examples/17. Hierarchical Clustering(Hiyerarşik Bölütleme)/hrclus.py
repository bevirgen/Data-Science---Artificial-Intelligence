import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#veri yukleme

veri = pd.read_csv('musteriler.csv')

#k-means 

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
plt.show()

#karşılaştırma sonuçları için (K-Means ve HC)

#k-means++
kmeans = KMeans ( n_clusters=4, init="k-means++", random_state=123)
ypred=kmeans.fit_predict(X)
print(ypred)

plt.scatter(X[ypred==0,0],X[ypred==0,1],s=100, c="red")
plt.scatter(X[ypred==1,0],X[ypred==1,1],s=100, c="blue")
plt.scatter(X[ypred==2,0],X[ypred==2,1],s=100, c="orange")
plt.scatter(X[ypred==3,0],X[ypred==3,1],s=100, c="green")
plt.title("K-Means")
plt.show()

#hierarchical clustering
    #fonksiyon içi (parantez) değişik algoritmalar başarıyı değiştiri

#hc euc-ward
from sklearn.cluster import AgglomerativeClustering

ac = AgglomerativeClustering(n_clusters = 4, affinity="euclidean", linkage="ward")
ypred=ac.fit_predict(X)
print(ypred)

plt.scatter(X[ypred==0,0],X[ypred==0,1],s=100, c="red")
plt.scatter(X[ypred==1,0],X[ypred==1,1],s=100, c="blue")
plt.scatter(X[ypred==2,0],X[ypred==2,1],s=100, c="orange")
plt.scatter(X[ypred==3,0],X[ypred==3,1],s=100, c="green")
plt.title("HC")
plt.show()

#hc single linkage
from sklearn.cluster import AgglomerativeClustering

ac = AgglomerativeClustering(n_clusters = 4, affinity="euclidean", linkage="single")
ypred=ac.fit_predict(X)
print(ypred)

plt.scatter(X[ypred==0,0],X[ypred==0,1],s=100, c="red")
plt.scatter(X[ypred==1,0],X[ypred==1,1],s=100, c="blue")
plt.scatter(X[ypred==2,0],X[ypred==2,1],s=100, c="orange")
plt.scatter(X[ypred==3,0],X[ypred==3,1],s=100, c="green")
plt.title("HCSingle")
plt.show()

#dendogram
    #scipy kütüphanesiyle ilgili detaylar sitesinden okunabilir
    #scipy kod satırı sklearn göre farklı
    
import scipy.cluster.hierarchy as sch

dendogram=sch.dendrogram(sch.linkage(X, method="ward"))
plt.show()







