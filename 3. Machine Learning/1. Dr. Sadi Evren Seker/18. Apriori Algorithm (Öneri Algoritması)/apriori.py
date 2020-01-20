import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


veri = pd.read_csv('sepet.csv', header=None)


from apyori import apriori

t=[]

for i in range(0,7501):
    t.append([str(veri.values[i,j]) for j in range(0,20)])
    
rules = apriori(t, min_support=0.01, min_confidence=0.2, min_lift=3, min_length=2)
print(list(rules))

#rules, apriori sınıfından ürteilen bir nesne olduğu için liste haline getirmeden bastırılamaz.


