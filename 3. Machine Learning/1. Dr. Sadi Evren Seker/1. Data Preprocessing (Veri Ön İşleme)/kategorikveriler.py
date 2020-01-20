#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 04:18:20 2018

@author: sadievrenseker
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#veri on isleme

veri = pd.read_csv('eksikveriler.csv')
print(veri)
boy = veri[['boy']]
print(boy)
boykilo = veri[['boy','kilo']]
print(boykilo)

class insan:
    boy=180
    def kosmak(self,b):
        return b+10

ali = insan()
print(ali.boy)
print(ali.kosmak(90))

#eksik veriler

    #sklearn sci-kit learn > bilimsel makine öğrenmesi
    #Import,imputation > eksik verilerin uygun bir şekilde doldurulması
    #iloc > veriyi almaya yarar
    #preprocessing > ön işleme
    #fit > istediğimizi uygulama
    #transform> istediğimizi içine yazdırma(dönüştürme)
    
from sklearn.preprocessing import Imputer 

imputer = Imputer(missing_values = "NaN", strategy = "mean", axis=0 )

Yas = veri.iloc[:,1:4].values
print(Yas)
imputer = imputer.fit(Yas[:,1:4])
Yas = imputer.transform(Yas[:,1:4])
print(Yas)

#kategorik veriler
    #LabelEncoder > Verilen metinleri sayıya çevirir
    #OneHotEncoder > Etiketi kolon başlığına çevirir ardından
      #kolon altında olma durumunu 1 (değilse 0) ile yorumlar
      
from sklearn.preprocessing import LabelEncoder , OneHotEncoder

ulke = veri.iloc[:,0:1].values
print(ulke)
le = LabelEncoder()
ohe = OneHotEncoder(categorical_features = "all")
ulke[:,0] = le.fit_transform(ulke[:,0])
print(ulke)
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)

















