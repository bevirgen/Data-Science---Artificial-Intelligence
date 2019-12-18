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
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
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

#verilerin birleştirilmesi ve dataframe oluşturulması
    #dataframe > veriyi düzenleme
    #concat > düzenlediğimiz verileri birleştirme
    #axise 1 vermemizin sebebi birleştirmek istediğimiz verileri satır bazlı birleştirmek
sonuc = pd.DataFrame(data = ulke, index = range(22), columns=["fr","tr","us"])
print(sonuc)
sonuc2 = pd.DataFrame(data = Yas, index = range(22), columns=["boy","kilo","yas"])
print(sonuc2)

cinsiyet = veri.iloc[:,-1].values
print(cinsiyet)

sonuc3 = pd.DataFrame(data = cinsiyet, index = range(22), columns=["cinsiyet"])
print(sonuc3)

s = pd.concat([sonuc,sonuc2,sonuc3],axis=1)
print(s)

#veri kümesinin eğitim ve test olarak bölünmesi
    #x_train > ana verinin büyük kısmı(öğrenme yapmasını istediğimiz kısım)
    #x_test > kalan gerçek kısım(karşılaştırma için)
    #y_train > büyük kısım tahmin
    #y_test > kalan kısım tahmin
    #random state 0 olmasının sebebi verilerin rastgele öğrenimi için
    #kodun açıklaması : xtraini al, ytraini tahmin etmeyi öğren, xtesti al ytesti tahmin et
     
from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33, random_state=0)





