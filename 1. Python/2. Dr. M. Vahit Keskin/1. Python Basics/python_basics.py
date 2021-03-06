# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 00:38:18 2020

@author: berka
"""

#helpful functions and code cells

abs(5-7) # absolute value 
divmod(122,5) # modular arithmetic , example > (24*5) + 2 ... 2 is leftover

a = 8000

complex_variable = 1+2j
type(complex_variable)

del a, complex_variable # delete variable

list_ = ['a','b','c',4,5,6,7]
list_

list_2 = [['a','b','c'],4,[5,6,7,8],6,11.9]
len(list_2)

type(list_2[2])
type(list_2[1])

ali = 'Aliislookingtohorse'
listed = list(ali)
connected_list = [list_,list_2,listed]

# indexing and slicing

ali[0:1]
ali[4:]
ali[-1:]
list_2[2:]
list_2[2][2] # list in list

strlist = ['ali','veli','abdulmut','joe','cole','berkay','su']
strlist[2] = 'velinin babasi'
strlist[2:6] = 'velinin babasi',"joe's father",'his father',"berkayin babasi"
strlist += ['new father']

# methods

strlist.append('who is the father') # add
strlist.remove('who is the father') # remove
strlist.insert(1,'who is the father') # adding component according to index what we say
strlist.insert(len(strlist), 'I am the father')
strlist.pop(1) # deleting component according to index what we say
strlist.pop(-1)
strlist.extend(['father try']) # concatenate list
strlist.sort()

# dictionaries

dctnry = {
    'reg':'regression model',
    'log':'logistic regression',
    'cart':'classification and regression trees'
    }

dictionary = {
    'reg':['RMSE',10],
    'log':['MSE',11],
    'cart':['SSE',12]
    }

dctnry['reg']

dict_in_dict = {
    'reg':{'RMSE':101,
           'MSE':111,
           'SSE':121},
    'log':{'RMSE':102,
           'MSE':112,
           'SSE':122},
    'cart':{'RMSE':103,
           'MSE':113,
           'SSE':123},
    }

dict_in_dict['reg']['RMSE']

dctnry['gbm'] = 'gradient boosting machines'

liste = [1,2,3]
# dctnry[liste] = 'one','two','three' # there will be an error

# set

l = [1,'a','b',2]
s = set(l)

t = ('a','ali')
s = set(t)
# s[0] , there will be an error
veli = 'veli is looking to the space'
s = set(veli) # this is important, every character just one time in set
joe = ['stop', 'looking', 'to', 'the', 'space', 'please', 'Joe','please']
s = set(joe) # there is just one please in s
s.add('hot water')
s.remove('hot water')

set1=set([1,3,4,5])
set2=set([2,3,5,8])

print(set1.difference(set2)) # set 1 - set 2
print(set2.difference(set1)) # set 2 - set1
print(set1.symmetric_difference(set2)) # (set 1 - set 2) + (set 1 - set 2)

set1-set2

set1.intersection(set2) # SET1 n SET2
set1 & set2 # same thing above line
set1.union(set2) # set1,set2 unique combine
set1.intersection_update(set2) # apply and change set1 according to intersections

set3=set([10,11,12])
set4=set([10,11,12,13,14,454])
set3.isdisjoint(set4) # is SET3 n SET4 empty? >> False
set3.issubset(set4) # is SET3 c SET4 ? >> True
set4.issuperset(set3) # is SET4 superset SET3 ? >> True

# functions

def square(x,y):
    if y != 0:
        # return int((x*y) / (x/y))
        print('Operation of the number you entered:',int((x*y) / (x/y)))
    else:
        print('Operation failed because y is can not be equal 0')

square(3,0)

    # lambda function
new_multiply = lambda a,b : a*b
new_multiply(2,4)
unordered_list = [('b',3),('a',8),('d',12),('c',1)]
sorted(unordered_list, key = lambda x : x[1])
    # map & filter & reduce
v = [1,2,3,4,5]
map(lambda x: x+10, v) # mapping
list(map(lambda x: x+10, v)) # output

v = [1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x: x % 2 == 0, v)) # filter

from functools import reduce
reduce(lambda x,y : x+y, v) # reduce

# if-else (conditional) statements

limit = 5000
income = 1111

if income > limit:
    print('You are not relevant for cash support! ')
elif income <= 1000:
    print('You are relevant to A type support')
elif income > 1000:
    print('You are relevant to B type support')

# for loop

salaries = [1000,2000,3000,4000,5000,6500,8000]

# =============================================================================
# def new_salaries(x):
#     if x < 3000:
#         x = x * 1.25
#     else:
#         x = x * 1.1
#     print(int(x))
# =============================================================================

for each in salaries:
    if each < 4000:
        each = each * 1.25
    else:
        each = each * 1.1
    print(int(each))
    
# break continue
    
mean_sales = [100,55,68,22,77,105,200]

for each in mean_sales:
    if each < 30:
        print('Sales is very few, check the problems, sales =',each)
        break # break loop
    print(each)

for each in mean_sales:
    if each == 22:
        continue # jumped 22
    print(each)
    
number = 0

while number < 10:
    number += 0.5
    print(number)





