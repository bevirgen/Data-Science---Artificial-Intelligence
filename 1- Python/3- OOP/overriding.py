# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 17:57:48 2019

@author: berka
"""

# overriding

class Animal:
    
    def toString(self):
        print("animal")
        
class Monkey(Animal):
    
    def toString(self): # we create same name class
        print("Monkey")
        
a1 = Animal()
a1.toString()

m1 = Monkey()
m1.toString() # monkey calls overriding method , sub classın toString methodu overriding oldu, yani ağırbastı (diğer methodu geçersiz kıldı)