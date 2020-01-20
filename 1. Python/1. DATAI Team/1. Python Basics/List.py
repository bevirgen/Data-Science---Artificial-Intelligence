# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:53:53 2019

@author: berka
"""

# %% list

mylist = [1,2,3,4,5,6]
type(mylist)

list_str=["ptesi","sali","carsamba"]
type(list_str)

print(mylist[0]) #0.indeks ilk eleman demektir
print(list_str[1])

value = mylist[2]
print(value)
value2 = list_str[2]
print(value2)

last_value = mylist[-1] #listenin -1. indeksi onun son değeridir
print(last_value)

list_divide = mylist[0:3] 
print(list_divide) # 0'dan 3'e kadar indeksleri al (3 dahil değil)

print(dir(mylist)) #list için kullanılabilir komutlar

print(help(list.append)) #tüm komutlar için (append yerine başka bir komut olabilirdi) kullanım kılavuzu

mylist.append(7) # listeye 7 eklendi
print(mylist)

mylist.remove(2) # listeden 2 kaldırıldı
print(mylist)

mylist.reverse() #listeyi ters çevir
print(mylist)

mylist2 = [5,1,2,9,8,3,4,7,0]
print(mylist2)
mylist2.sort() #listeyi sırala
print(mylist2)

str_int_list = [1,2,3,4, "berkay", "evirgen"]
print(str_int_list) #liste farklı değişkenleri barındırabilir
# %% tuple

print(dir(tuple)) #help usable commands for tuple

t=(1,1,1,2,3,3,4,5,6,7,8)
t.count(1) # t tuple'ının içinde kaç adet 1 olduğunu gösterir

t.index(6) # 6'nın indeksini bul
# %% dictionary (sözlük)

dictionary={"Ali":20,
            "Veli":25,
            "Ceyhun":33,
            "Sinem":30,
            "Berkay":23} # " içindeki veriye (key), yanına : ile belirttiğimiz değer atandı(value)

print(dictionary["Ali"]) #Ali'ye atanan değeri göster
print(type(dictionary["Ali"])) #Ali'ye atanılan değerin integer olduğunu dogrulama
print(dictionary.keys())
print(dictionary.values())

def test():
    dictionary={"Ali":20,
                "Veli":25,
                "Ceyhun":33,
                "Sinem":30,
                "Berkay":23}
    return dictionary

dic=test()
print(type(dic))
print(dic["Berkay"])
# %% conditionals (koşullar)

#if-else statement

var1=10
var2=20

if(var1 > var2):
    print("1. degisken buyuktur")
elif(var1==var2):
    print("2 degisken birbirine esit")  
else:
    print("2. degisken buyuktur")
    
mylist=[1,2,3,4,5,6,7,8,9]

if 10 in mylist:
    print("Evet,10 degeri listededir.")
else:
    print("Hayir, bu listede 10 degeri yoktur.")
    
value=9

if value in mylist:
    print("Evet {} degeri listenin icinde.".format(value))
else:
    print("Hayir listede degil.")

keys=dictionary.keys()

if "Berkay" in keys:
    print("Evet,dictionary içinde Berkay var.")
else:
    print("Hayır, dictionary içinde Berkay yok.")
# %% QUIZ
    
#from year to century (yılı yuzyila donusturme)
    
def year2century(year):
    str_year=str(year)
    
    if(len(str_year) < 3): 
        return 1 # eger yil 3 basamaktan kucukse 1.yuzyil demektir
    elif(len(str_year) == 3):
        if(str_year[1:3] == "00") : #100,200,300,....800,900
            return int(str_year[0])
        else:
            return int(str_year[0])+1
    else:
        if(str_year[2:4] == "00"): #1000,1100,......,1700,1800,1900,2000
            return int(str_year[:2])
        else:
            return int(str_year[:2])+1

test = year2century(1666)
print(test, ".yuzyil")
# %% loops(donguler)

# for loop

for each in range(1,11): #11 dahil değil 1> intended , 11>extended
    print(each)

for each in "ankara ist":
    print(each)

for each in "ankara ist".split(): # split (ayır), ankara , ist
    print(each)

liste = [1,34,2,5,7,8,66,22,36]
summation = sum(liste) # listenin içindeki verilerin toplamı

    #veya

count=0
for each in liste:
    count += each
print(count)

# while loop

i=0
while(i<4):
    print(i)
    i+=1

limit=len(liste)
each=0
count=0

while(each < limit):
    count+=liste[each]
    each += 1
# %% QUIZ

listem = [1,2,334,77,223,775,235,677,3,-100,-999]    

min_value = 10000000

for each in listem:
    if(each < min_value):
        min_value = each
        print(each)
    else:
        continue



















