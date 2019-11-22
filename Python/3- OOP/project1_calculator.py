# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 20:23:52 2019

@author: berka
"""

#calculator project

class Calc(object):
    
    def __init__(self, a, b):
        self.value1 = a
        self.value2 = b
    
    def add(self):
        return self.value1 + self.value2
    
    def multiply(self):
        return self.value1 * self.value2
    
    def division(self):
        return self.value1 / self.value2
    
selection = int(input ("Choose (1) for Addition, (2) for multiplaction, (3) For Division\n")) #input, konsoldan veri alıp değişkene atar
v1=int(input("First value "))
v2=int(input("Second value "))

numbers=Calc(v1,v2)

if (selection == 1):
    numbers.add()
    print("Addition : {}".format(numbers.add()))
elif (selection == 3):
    numbers.division()
    print("Division : {}".format(numbers.division()))
elif (selection == 2):
    numbers.multiply()
    print("Multiply : {}".format(numbers.multiply()))
else:
    print("There is no proper selection")
    
