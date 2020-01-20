# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:38:22 2019

@author: berka
"""

class Website:
    "parent"
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    
    def loginInfo(self):
        return self.name + " " + self.surname

class Website1(Website):
    "child"
    def __init__(self,name,surname,ids):
        Website.__init__(self,name,surname)
        self.ids = ids
    
    def login(self):
        return self.name + " " + self.surname + " " + self.ids

class Website2(Website):
    "child"
    def __init__(self,name, surname, email):
        Website.__init__(self,name,surname)
        self.email = email
    
    def login(self):
        return self.name + " " + self.surname + " " + self.email

p2=Website1("Berkay", "Evirgen", "b.evirgen")
p3=Website2("Berkay", "Evirgen", "@evirgenmail.com")