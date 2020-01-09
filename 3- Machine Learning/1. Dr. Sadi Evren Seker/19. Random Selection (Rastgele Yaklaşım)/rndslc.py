import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veri = pd.read_csv("Ads_CTR_Optimisation.csv")


#random selection , örneğin 10.000 tıklamalı , 10 reklamdan oluşan rastgele seçimde, 800. satırda
    #bazı satırlar true(ödül =1) olarak işaretlenmiştir, program o satırlarda 1 olan
    #sütunu seçtiğinde ödül kolonu artırılacaktır, böylece elde edilen ödül sürekli toplanıp
    #rastgele seçimle yakalanan ihtimal gösterilecektir (10000 de X)
    
import random

secilenler = []
toplam = 0

for n in range (0,10000) :
    ad = random.randrange(10)
    secilenler.append(ad)
    odul = veri.values[n,ad] #verilerdeki n.satır 1 ise ödül +=1
    toplam += odul

plt.hist(secilenler)
plt.show()