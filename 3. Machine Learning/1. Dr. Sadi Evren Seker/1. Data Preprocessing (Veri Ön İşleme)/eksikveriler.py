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

from sklearn.preprocessing import Imputer 

imputer = Imputer(missing_values = "NaN", strategy = "mean", axis=0 )

Yas = veri.iloc[:,1:4].values
print(Yas)
imputer = imputer.fit(Yas[:,1:4])
Yas = imputer.transform(Yas[:,1:4])
print(Yas)