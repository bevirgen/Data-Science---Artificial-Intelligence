"""
Created on Thu Jan  9 14:14:22 2020

@author: berka
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import nltk as nlp
import re
from nltk.corpus import stopwords

# data preprocessing
data = pd.read_csv('data.csv',encoding='latin1')
data = pd.concat([data.gender,data.description],axis=1)
data.replace(['unknown'],np.nan, inplace=True)
data.dropna(axis=0, inplace=True)

le = LabelEncoder()
data.gender=le.fit_transform(data.gender) # 0 brand, 1 female, 2 male
# %% text processing
first_desc = data.description[4]
# from upper to lower and not from a-z A-Z to ' '
description = re.sub('[^a-z A-Z]',' ',first_desc).lower()
description = nlp.word_tokenize(description) #split data
# drop irrelavent words
description = [word for word in description if not word in set(stopwords.words('english'))]
# %% lemmatazation > kök bulma işlemi
lemma = nlp.WordNetLemmatizer()
description = [lemma.lemmatize(word) for word in description]
description = ' '.join(description) #combine words
# %% apply it for all comments

description_list = []
for description in data.description:
    description = re.sub('[^a-z A-Z]',' ',description).lower()
    description = nlp.word_tokenize(description)
    #description = [word for word in description if not word in set(stopwords.words('english'))]
    description = [lemma.lemmatize(word) for word in description]
    description = ' '.join(description)
    description_list.append(description)
"""
df = pd.DataFrame({'description':description_list})
data = pd.concat([df.description, data.gender], axis=1)
data.dropna(axis=0, inplace=True)
"""
# %%
max_features = 50 #the most used 50 word
count_vectorizer = CountVectorizer(max_features=max_features,stop_words='english')
sparce_matrix = count_vectorizer.fit_transform(description_list).toarray()
print('The most used 50 word :',count_vectorizer.get_feature_names())
# %% creating model
y = data.iloc[:,0].values
x = sparce_matrix

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.1, random_state=42)
#%%
nb = GaussianNB()
nb.fit(x_train,y_train)
#%%
pred = nb.predict(x_test)
print('accuracy:',nb.score(pred.reshape(-1,1),y_test))