"""
Created on Thu Jan  9 14:14:22 2020

@author: berka
"""

from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import nltk
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
description = nltk.word_tokenize(description) #split data
# drop irrelavent words
description = [word for word in description if not word in set(stopwords.words('english'))]

