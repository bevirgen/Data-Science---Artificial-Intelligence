#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 04:18:20 2018

@author: sadievrenseker
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veri = pd.read_csv('veriler.csv')
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