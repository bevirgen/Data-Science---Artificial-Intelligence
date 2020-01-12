# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 21:17:31 2020

@author: berka
"""

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd

#data prepare
iris = load_iris()

x = iris.data
feature_names = iris.feature_names
y = iris.target
df = pd.DataFrame(x, columns=feature_names)
df['species'] = y
# %% principal component analysis

pca = PCA(n_components=2, whiten=True) #whiten = normalization
x_pca = pca.fit_transform(x)

print('variance ratio:',pca.explained_variance_ratio_)
print('Summation:',sum(pca.explained_variance_ratio_))
# %% visualization
df['comp1'] = x_pca[:,0]
df['comp2'] = x_pca[:,1]
color = ['red','green','blue']

for each in range(3):
    plt.scatter(df.comp1[df.species==each],df.comp2[df.species==each],color=color[each], label=iris.target_names[each])
    
plt.legend()
plt.show()
