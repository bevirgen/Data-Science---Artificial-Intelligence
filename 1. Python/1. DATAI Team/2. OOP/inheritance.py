# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 22:22:18 2019

@author: berka
"""

# inheritance
# very good source for inheritance subject > https://www.pythonprogramming.in/inheritance.html

class Animal: #parent class , tanımladığımız özellikler child classlar tarafından kullanılabilecektir
    
    def __init__(self):
        print("Animal is creating...")
        
    def toString(self):
        print("Animal")
    
    def walk(self):
        print("can walk")

class Monkey(Animal): # child
    
    def __init__(self):
        super().__init__() # use init of parent (Animal) class
        print("Monkey is created")
        
    def toString(self):
        print("Monkey")
        
    def climb(self):
        print("Monkey can climb")
        
class Bird(Animal): # child
    
    def __init__(self):
        super().__init__() # use init of parent (Animal) class
        print("Bird is created")
        
    def fly(self):
        print("Bird can fly")

m1 = Monkey()
m1.toString()
m1.walk()
m1.climb()
b1 = Bird()
b1.walk()
b1.fly()