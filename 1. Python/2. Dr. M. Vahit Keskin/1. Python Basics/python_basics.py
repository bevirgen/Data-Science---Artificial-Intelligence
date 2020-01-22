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







