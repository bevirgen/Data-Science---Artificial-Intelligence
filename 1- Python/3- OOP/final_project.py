# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 19:01:48 2019

@author: berka
"""

"""
OOP : Object Oriented Programming
    : class / object/constructor
    : attirubutes / methods
    : encapsulation / abstraction
    : inheritance
    : overriding / polymorphism
"""

from abc import ABC, abstractmethod # import abstract

class Shape(ABC): # created super class with inherited ABC
    
    @abstractmethod
    def area(self) : pass

    @abstractmethod
    def perimeter(self) : pass

    def toString(self) : pass #overriding and polymorphism
    
class Square(Shape): # child
    
    def __init__(self,edge):
        self.__edge = edge # encapsulation, private attribute
        
    def area(self):
        result = self.__edge**2 
        print("Square Area :",result)
    
    def perimeter(self):
        result = self.__edge * 4
        print("Square perimeter :",result)
        
    def toString(self):
        print("Square Edge : ",self.__edge)
        

class Circle(Shape):
    
    PI = 3.14 # constant variable (sonucu hiçbir yerde değişmeyecek değişken)
    
    def __init__(self,radius):
        self.__radius = radius # encapsulation, private attribute
        
    def area(self):
        result = self.PI * self.__radius ** 2
        print("Circle Area :",result)
        
    def perimeter(self):
        result = 2 * self.PI * self.__radius
        print("Circle perimeter :",result)
        
    def toString(self):
        print("Circle radius : ",self.__radius)
        
c = Circle(5)
c.area()
c.perimeter()
c.toString()
        
s = Square(5)
s.area()
s.perimeter()
s.toString()     
        
        
        
        