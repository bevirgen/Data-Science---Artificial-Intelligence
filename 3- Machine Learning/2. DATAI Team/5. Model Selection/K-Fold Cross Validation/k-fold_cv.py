# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 23:56:57 2020

@author: berka
"""

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
import numpy as np
import warnings
warnings.filterwarnings("ignore")

iris = load_iris()

x = iris.data
y = iris.target
# %% normalization
x = (x-np.min(x)) / (np.max(x)-np.min(x))
# %% train-test splitting
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=42)
# %% knn model
knn = KNeighborsClassifier(n_neighbors=5)
# %% cv accuracy
accuracies = cross_val_score(estimator=knn, X=x_train, y=y_train, cv=10)
print('average accuracy:',np.mean(accuracies))
print('average std:',np.std(accuracies))
# %% test acc
knn.fit(x_train, y_train)
print('test acc:',knn.score(x_test,y_test))
# %% grid search with cross validation
grid = {'n_neighbors':np.arange(1,50)}
knn = KNeighborsClassifier()
knn_cv = GridSearchCV(knn,grid, cv=10)
knn_cv.fit(x,y)
#  finding tuned hyperparameter and best score
print('tuned Hyp K:',knn_cv.best_params_)
print('best acc for tuned parameter',knn_cv.best_score_)
# %% Grid Search CV with logistic regression
x = x[:100,:]
y = y[:100]
# if c > it's Overfit, if c < it's underfit
grid = {'C':np.logspace(-3,3,7),'penalty':['l1','l2']} # C = log regression regularization parameter
lr = LogisticRegression()
lr_cv = GridSearchCV(lr,grid, cv=10)
lr_cv.fit(x_train, y_train)
#  finding tuned hyperparameter and best score
print('tuned Hyperparameter:',lr_cv.best_params_)
print('best acc for tuned parameter',lr_cv.best_score_)
# %%
lr2 = LogisticRegression(C=1)
lr2.fit(x_train, y_train)
print('score',lr2.score(x_test,y_test))