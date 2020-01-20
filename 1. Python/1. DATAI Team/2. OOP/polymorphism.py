# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 18:09:31 2019

@author: berka
"""

# polyporphism (çokşekillilik,çok biçimlilik) 
# > superclass'tan (parent) sub class'a (child) kalıtım yoluyla (inheritance) aktarılan, ama sub classta farklı bir şekilde kullanılmasıdır

class Employee:
    
    def addition(self):
        raise_rate=0.1
        result = 100 + 100 *raise_rate
        print("Employees :",result)
    
class CompEng(Employee):
    
    def addition(self):# we used same method
        raise_rate=0.2 # with different value
        result = 100 + 100 *raise_rate
        print("Comp.Engineers :",result)
    
class EEE(Employee):
    
    def addition(self): # we used same method
        raise_rate=0.3 # with different value
        result = 100 + 100 *raise_rate
        print("EEE :",result)
        
e1 = Employee()
ce = CompEng()
eee = EEE()

emp_list = [e1,ce,eee]

for i in emp_list:
    i.addition()