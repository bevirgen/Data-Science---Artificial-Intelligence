# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:33:39 2019

@author: berka
"""

# encapsulation > belirli bir class içinde yaratılan variablelara (değişkenlere) dışardan erişimin kısıtlanması

class BankAcoount():
    
    def __init__(self, name, money, address):
        self.name = name # bir şey belirtmediysek veri default global olacaktır
        self.__money = money # fakat başına __ eklersek private olacaktır, yani sadece class içinde çağırılabilecektir
        self.address = address
        
        # get ve set metodları dünya genelinde kabul görmüş herkesin anladığı şekilde yazılan metodlar
        # get > istediğimiz veriye erişim sağlamak için yaratılan metod
        # set > istediğimiz değişkeni set etmek (adjust(ayarlama),güncelleme yapmak) için yaratılan metod
        
    def getMoney(self): # global method
        return self.__money
    
    def setMoney(self, amount): # global method
        self.__money = amount
        
    def __increase(self): # private method > dışardan erişimi engelledik
        self.__money += 1000


person1 = BankAcoount("Jay-Jay Okocha", 500000, "Nigeria")
person2 = BankAcoount("Ahmet Dursun", 230000, "Turkey,Istanbul")

# print(person1.__money()) # private veriye erişmeye çalıştığımız için hata verdi
print("get method : ",person1.getMoney()) # istediğimiz veriye ulaştık 

person1.setMoney(5000) # set ettik
print("after set method : ",person1.getMoney())

#person1.__increase() # zam yaptık , method private olduğu için class dışında erişemeyeceğiz
#print("after raise : ",person1.getMoney())