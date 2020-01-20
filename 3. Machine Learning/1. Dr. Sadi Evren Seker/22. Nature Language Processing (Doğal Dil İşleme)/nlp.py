import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

yorumlar = pd.read_csv('Restaurant_Reviews.csv')

#Sparse Matrix - İmla işaretleri

import re
import nltk

from nltk.stem.porter import PorterStemmer #kelimelerin çekim eklerini atmak için kullanacağımız sınıfını çekme
ps = PorterStemmer()

nltk.download("stopwords") #nltk kütüphanesi içinden stopwords kısmını yükle
from nltk.corpus import stopwords

#Preprocessing (önişleme)
derlem = []
for i in range(1000):
    yorum = re.sub("[^a-zA-Z]",' ', yorumlar["Review"][i]) # ^ işareti değil anlamında , küçük-küçükbüyük-büyük dışı filtrele
    yorum = yorum.lower() #tamamını küçük harfe çevir
    yorum = yorum.split() #kelimeleri liste haline çevir
    yorum = [ps.stem(kelime) for kelime in yorum if not kelime in set(stopwords.words("english"))] #stopwordsleri bir kümeye çevir,o kelime stopwords değilse (eğer stopwordsse at),kökünü bul ve listenin ilk elemanı yap
    yorum = " ".join(yorum) #listeyi cümle haline getirme
    derlem.append(yorum) #derlem listesinin içine ekle

#Feature Extraction (Öznitelik Çıkarımı)
from sklearn.feature_extraction.text import CountVectorizer

cv=CountVectorizer(max_features = 2000) #en çok geçen 2000 kelimeyi belirle
X = cv.fit_transform(derlem).toarray() #belirlediğimiz 2000 kelime, derlemdeki 1000 cümlede geçiyor mu?
y = yorumlar.iloc[:,1].values #o cümle beğeni cümlesi mi, değil mi?


