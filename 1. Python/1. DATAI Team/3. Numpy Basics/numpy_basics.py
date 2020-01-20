# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 14:21:03 2019

@author: berka
"""

# %% numpy

# frequently using for statistical processing

import numpy as np #imported

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) # 1 * 15 vector
print(array.shape)

a = array.reshape(3,5) # 3 * 5 matris (3sutun * 5satir)
print("shape : ", a.shape) # 
print("dimension : ", a.ndim)
print("data type : ", a.dtype)
print("size : ", a.size)
print("type : ", type(a))

array1 = np.array([[1,4,2,3],[5,6,9,0],[8,3,4,1]])

zeros = np.zeros((3,4)) # 0'lardan olusan 3 * 4 luk matris yarat, locate et (yer ayırt, daha sonra kullanmak için hazır bekletilir)

# eğer veri buyukse append komutu bellegi yorar , if data is big , append command is frazzle memory
# bunun icin yeri ayirdiktan sonra daha sonra matriste guncelleme yapabiliriz

zeros[1,0] = 5 # 1.satir , 0.sutun = 5
zeros[0,3] = 7 # 0.satir, 3.sutun = 7
zeros

ones = np.ones((3,4)) # 1,lerden olusan 3 * 4 matris olusturuldu
ones

empty = np.empty((3,2)) # create 3 *2 null matris
empty

arange = np.arange(10,51,5) # 10'dan baslayip 50'ye kadar sayiları 5er 5er yaz
arange

arng= np.arange(1,17,2) # 1 intend 17 extend, 1-17 arası 2 şer artan sayıları yaz
arng

linsp = np.linspace(10,50,20) # 50 intend (dahil), 10 ve 50 arasında 20 adet sayı yaz
linsp
# %% numpy basic operations

a = np.array([1,2,3])
b = np.array([4,7,10])
print(a + b)
print(a - b)
print(a**2)
print(np.sin(a)) # a'nın sinüsünü al > tüm verilerin tek tek sinüsünü alır
print(a < 2) # bu koşula göre verileri true veya false döndürecektir



# element wise product

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[4,6,8],[11,14,17]])
print(a*b)

# matris product
#print(a.dot(b))
""" b'nin transpozunu almadığımız için hata verecektir
 detay vermek gerekirse (2,3) ' luk matrisi (3,2) lik matrisle çarpabiliriz, yani (2,3)'luk b matrisini
Transpoz edersek (x,y) yer değiştirirsek (3,2) bir matris olacaktır ve a matrisiyle çarpıma uygun hale gelecektir"""
print(a.dot(b.T))

print(np.exp(a)) # matris exponential (üstel değerini alma)

a = np.random.random((5,5)) # 5 * 5 , 0-1 aralıgında oluşturulmuş matris

print(a.sum())
print(a.max())
print(a.min())

print(a.sum(axis=0)) # sum columns > tüm kolon verilerini toplar
print(a.sum(axis=1)) # sum rows > satır verilerini toplar

print(np.sqrt(a)) # tek square root a , a'nın karekökünü all
print(np.square(a)) # a'nın karesini al

array3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
d = array3.reshape(5,5)

print(np.add(a,d)) # addition = sum , > a + d
# %% indexing and slicing

array = np.array([1,2,3,4,5])

reverse_array = array[::-1] # reverse array
print(reverse_array)

array1 = np.array([[1,4,2,3],[5,6,9,0],[8,3,4,1]])
print(array1[0:2]) # 0 ve 1.boyutları bastır

print(array1[2,3]) # 2.index satır 3.index kolon veri

print(array1[:,1]) # tüm satırları al 1.kolondaki verileri yaz

print(array1[1:3,1:3]) # 1 : 3 satır (3 is not included) , 1 : 3 kolon verilerini bastır

print(array1[-1:,]) # son satır tüm kolon verileri
print(array1[:,-1]) # tüm satır son kolon verileri
# %% shape manipulation

array = np.array([[1,2,3],[4,5,6],[9,5,1]])

# flatten

a = array.ravel() # matris to vector > array'i vektor haline getirir [1,2,3,4,5,6,9,5,1] 
print(a)

array = a.reshape(3,3) # vector to matris
print(array)

arrayT = array.T # take transpoz of array
print(arrayT.shape) # matrisin boyutlarını goster

array2 = np.array([[1,2],[3,4],[4,5]])
print(array2)
b = array2.reshape(2,3) # reshape array2 to 2*3 matris

# reshape ve resize arasındaki fark, reshape komutu reshape ettiği veriyi başka bir değişken üzerine kaydeder, aynı değişkene yazmaz
# resize komutu yaptığı değişikliği aynı array (matris) üzerine direkt olarak kaydeder. > ikisi de aynı işlemi yapar

array2.resize(3,2)
# %% stacking arrays (array birleştirme)

array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])

# vertical stack
a = np.vstack((array1,array2))

# horizontal stack
b = np.hstack((array1,array2))
# %% convert and copy array

liste = [1,2,3,4]
array = np.array(liste) # list to array
liste2 = list(array)

a = np.array([1,2,3,4,5])

b = a
b[0] = 5 # bu işlemde b nin 0 indeksini 5 yaptığımda a ve c nin de 0 indeks = 5 olacaktır, sebebi, değeri birbirine eşitleyerek verdiğim için
print(b) #bellekte aynı alanı kaplayan a array ini kullanırlar ve aynı alandaki veri değişince hepsinin verisi değişir, çözümü copy kullanmaktır
c = a
print(c)

d = a.copy() # bellekte d için başka bir alan ayırıldı
d[0] = 3
print(d)
f = a.copy() # f için bellekte başka bir alan ayırıldı
print(f)







