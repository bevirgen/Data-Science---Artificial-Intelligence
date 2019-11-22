# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 17:25:43 2019

@author: berka
"""

# %% Classes

class Calisan:
    
    additionToSalaryRate = 0.2 #class variable
    counter = 0 #sayaç
    
    def __init__(self,name,surname,salary): #constructor (initial) > class'ın default özellikleri
        self.name = name                    #attirubute
        self.surname = surname
        self.salary = salary
        self.email = name + surname +"@mymail.com"
        
        Calisan.counter += 1 # Çalışan classına yeni değişken eklenince (yeni bir obje yaratılınca > isci1) sayaç artacaktır
    
    def giveNameSurname(self): #self, class içindeki tanımlanmış değişkenlere erişmemiz için gereklidir
        return self.name + " " + self.surname #class içinde çağırmak istediğimiz değişken için self kullanmalıyız
    
    def doAddition(self):
        self.salary += self.salary*self.additionToSalaryRate
        
#isci1=Calisan("Berkay","Evirgen",3300)
#print(isci1)
#print(isci1.giveNameSurname())
#print(isci1.salary)
#print(isci1.email)
        
#class variable
        
isci1=Calisan("Berkay","Evirgen",3300)
print("Old Salary : " ,isci1.salary)
isci1.doAddition()
print("New Salary : " ,isci1.salary)

isci2=Calisan("Ahmet","Dursun",6000)
print("Old Salary : " ,isci2.salary)
isci2.doAddition()
print("New Salary : " ,isci2.salary)

print(Calisan.counter)

isci3=Calisan("Ahmet","Dursun",8800)
isci4=Calisan("Ahmet","Dursun",9600)
isci5=Calisan("Ahmet","Dursun",2550)
isci6=Calisan("Ahmet","Dursun",2300)
isci7=Calisan("Ahmet","Dursun",4300)

#class example

liste = [isci1,isci2,isci3,isci4,isci5,isci6]
liste.append(isci7)

max_salary = -1
index = -1

for each in liste:
    if(each.salary > max_salary):
        max_salary=each.salary
        index = each.giveNameSurname()
    else:
        continue
    
print(index, max_salary)
#%% examples

class Square:
    
    def __init__(self,edge):
        self.edge = edge
        
    def areacalc(self):
        return self.edge * self.edge
    
    def sidelengthcalc(self):
        return self.edge * 4
    
sq1=Square(5)
sq1.areacalc()
sq1.sidelengthcalc()


