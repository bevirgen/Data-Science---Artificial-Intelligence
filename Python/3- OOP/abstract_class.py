# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 17:22:42 2019

@author: berka
"""

# abstract class
# bu classlar diğer classlar için şablon görevi görür
# abstract class (soyut sınıflar), bu sınıfların içinden hiçbir şekilde instance edilemez (obje yaratılamaz)
# abstract classında kullanılan herhangi bir abstract method(parent class), herhangi bir sub classta (child class) kullanılmak zorundadır

from abc import ABC, abstractmethod # abc > abstract basic class , abstract kullanabilmek için metodu import ettik

class Animal(ABC): # parantez içine ABC'yi inherit ettik (kalıtım yaptık,tanımladık)
    
    @abstractmethod # walk metodunu abstract olarak tanımladık
    def walk(self) : pass

    def run(self) : pass #normal metod

class Bird(Animal):
    
    def __init__(self):
        print("Bird")
        
    def walk(self):
        print("Walk")

b1=Bird()