# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# %% variables (degiskenler)

"""standart convention of python (python standartları yazımında) değişkenler genelde küçük harfle başlar"""
# ctrl+1 seçilim tüm satırları commente alır

var1=10 #int
var2=10.3 #double(float)
gun ="pazartesi" #string
# 5var=10 > hata verecektir, degisken tanimlamalari sayi ile baslamaz
# %% string, numbers, degisken tipi sorgulama, print

ilkgun="pazartesidir"
variable_type=type(ilkgun) #degisken formatini sorgular > type(degiskenadi)

print(ilkgun) #console bastirma(yazdirma,cikti alma)

var1="ankara"
var2="istanbul"
var3=var1+var2 #'ankaraistanbul'

var4="100"
var5="200"
var6=var4+var5 #'100200' > bunlar birer string, int degil

uzunluk=len(var6) #satir uzunlugu

# var6[0] > 0.indeksi verir (1)

int_deneme=-50
float_deneme=-30.3
# %% built in functions

str1="deneme"
float1=10.6
int(float1) # 10a yuvarlar
round(float1) # yakın olan tam sayıya yuvarlar(11e)
str2="1005"
int(str2) # str2 degiskenini int'e cevir
# %% user defined functions

var1 = 20
var2 = 50
output=(((var1+var2)*50)/100.0) * (var1/var2)

def my_first_func(a,b): # function 
    output=(((a+b)*50)/100.0)*a/b
    return output

result=my_first_func(var1,var2)

def test1(): #her fonksiyon return gerektirmez
    print("this is my second test")
# %% defauld and flexible functions

    #default function
def calc_perimeter_of_circle(r,pi=3.14): #pi default 3.14 verildi
    return 2*pi*r
calc_perimeter_of_circle(4)

    #flexible function
def calculate(height,kilo,*args):
    return (height+kilo) + args[0] #isteğe bağlı eklenilen verinin ilk değeri
calculate(180,90,88,4)
    
# %% QUIZ

age=10
name="Ali"
surname="Coban"

def quiz_function(age,name,*args,foot_nr=35):
    print("Name of child: ",name,"Yasi: ",age,"Foot number: ",foot_nr)
    print(type(name))
    print(float(age))
    return args[0]*age

result=quiz_function(age,name,surname)
print("args[0]*age: ",result)
# %% lambda function

 #standart fonksiyon
 
def calc(x):
    output=x*x
#   print(output)
    return output
result = calc(2)

#aynı fonksiyonun daha sade yazımı

def calc2(y):
    return y*y
result2=calc2(4)

#aynı fonksiyonun lambda kullanarak yazımı

result3 = lambda x : x*x
print(result3(6))


















































