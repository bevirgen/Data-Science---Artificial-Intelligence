# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 00:01:41 2019

@author: berka
"""

# libraries
import numpy as np
import pandas as pd 
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# %%

timesData = pd.read_csv('timesData.csv')
timesData.head()