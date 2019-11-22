#!/usr/bin/env python
# coding: utf-8


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns # effective library for visualizaton


# In[5]:


df = pd.read_csv('heart.csv') #import data
df.info() # give me informations


# In[8]:


df.corr() > 0.5 # correlationship about datas
# we cannot draw important conclusions here , lets analyse more


# In[16]:


#correlation map
f, ax = plt.subplots(figsize=(13,11))
sns.heatmap(df.corr(), annot=True, linewidths = .5, fmt = '.1f', ax=ax)
plt.show()


# In[23]:


print(df.head(6)) # first 6 data
print(df.tail(6)) # last 6 data
print("\n",df.columns)


# In[40]:


df.age = df.age.astype('int')
df.describe()


# In[75]:


# line plot
# Correlation FBS Male-Female
male = df[df.sex == 1] # male
female = df[df.sex == 0] # female
"""f, ax = plt.subplots(figsize=(15, 15))
male.fbs.plot(kind='line', color='b', label='Male', linewidth=1,grid=True, linestyle=':',)
female.fbs.plot(kind='line', color='r', label='Female', linewidth=1, grid=True, linestyle='-.')
plt.legend(loc='upper right')
plt.title('Fasting Blood Sugar Test (FBS)')
plt.xlabel('Index')
plt.ylabel('FBS Statistics')
plt.show()"""
f, ax = plt.subplots(figsize=(15, 15))
plt.plot(male.index, male.fbs, color='b', label='Male')
plt.plot(female.index, female.fbs, color='r', label='Female')
plt.title('Fasting Blood Sugar Test (FBS)')
plt.xlabel('Index')
plt.ylabel('FBS')
plt.legend(loc='upper right')
plt.show()


# In[81]:


# Scatter Plot
# let's look correlation chol and max heart rate

df.plot(kind='scatter', x='chol', y='thalach', alpha=.5, color='r',figsize=(11, 9))
plt.xlabel('Chol')
plt.ylabel('Thalach')
plt.title('Chol-Max Heart Rate(Thalach) Scatter Plot')
plt.show()


# In[88]:


#Histogram
# age values
df.age.plot(kind='hist', bins=100,figsize=(13,10))
plt.show()


# In[96]:


# dictionary work
dctnry = {'Turkey' : 'Istanbul', 'Spain' : 'Granada', 'USA' : 'Las Vegas'}
print(dctnry.keys())
print(dctnry.values())
dctnry['Turkey'] = 'Izmir','Kirklareli' # changed and added one more data
print(dctnry)
dctnry['Spain'] = 'Madrid' # changed it
print(dctnry)
print('Istanbul' in dctnry) # is there any Istanbul values in dictionary? > no!
dctnry.clear() # clean it
print(dctnry)
# del dictionary > delete it


# In[100]:


# Work some pandas library basics

series=df.age
print(type(series))
dtframe=df[['sex']]
print(type(dtframe))

#logic
print(4<2)
print(3==2)
print(5==5)
#boolean
print(True and False)
print(True or False)


# In[106]:


# going ahead with pandas
agecholuppermean = df[np.logical_and(df.age > 54 , df.chol > 246)] #filtered two values in a dataframe
agecholuppermean.head()


# In[108]:


# Dont forget to while and for loops :)
# while

i=0
while i != 5 :
    print(i)
    i += 1
print(i, 'is equal to 5')


# In[119]:


# for

lis = [1,2,3,4,5]
for i in lis:
    print('i is : ',i)
print('\n')

# enumarate index and value of list
for index, value in enumerate(lis):
    print(index,':',value)
print('\n')

#using for loop with dictionaries
dictionary = {'spain':'madrid','france':'paris'}
for key, value in dictionary.items():
    print(key,':',value)
print('\n')

# we can achieve index and value with using pandas
for index, value in df[['cp']][0:5].iterrows():
    print(index,':',value)


# In[125]:


# look some tuple
def tuple_ex():
    """ return defined t tuble"""
    t = (1,2,3)
    return t
a,b,c = tuple_ex()
print(a,b,c)


# In[127]:


# local and global scope subject
x = 5
def f():
    x = 4
    return x
print(x) # this will return 5 > because this is global scope
print(f()) # this will return 4 > because this is local scope


# In[128]:


# What if there is no local scope
x = 3
def f():
    y=4+x
    return y
print(f()) # there is no local scope in fuction, so it'll uses the global x


# In[130]:


# How can we learn what is built in scope
import builtins
dir(builtins)


# In[131]:


# We should just some look nested Func (func inside func)
def square():
    def add():
        x,y = 3,7
        z = x+y
        return z
    return add()**2
print(square())


# In[134]:


# DEFAULT and FLEXIBLE ARGUMENTS
def f(a,b=1,c=2):
    y = a+b+c
    return y
print(f(7))
# can we change default args?
print(f(7,5,5)) # so, yes

