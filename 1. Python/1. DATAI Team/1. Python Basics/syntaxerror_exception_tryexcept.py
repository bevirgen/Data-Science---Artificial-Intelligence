# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:16:40 2019

@author: berka
"""

# %% syntax error

# it means you made typo

print (9)
#print 9 # syntax , missed parantheses

int(10.0)
#int 10.0 # syntax error
# %% exceptions
# başka bir hata varsa bile ondan önce syntax hatası varsa, python syntax error verir ve gerisini kontrol etmez

a = 10
b = "3"

liste=[1,2,3]
print(sum(liste)) 
#print(a+b) # int ve str'yi toplamayı denedigimiz icin hata ile karsilastik
print(a + int(b)) #dogrusu bu sekilde

k = 10
zero = 0
#print(k / 0) # ZeroDivisionError > 0'a bölüm hatası

if (zero == 0):
    a=0
else:
    a = k / zero

try:        #  try k / zero , if you take this ZeroDivisionError > a= 0
    a = k / zero
except ZeroDivisionError:
    a = 0

