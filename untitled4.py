# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14sgTiRkJ5RtHT109ZwJ_dtDjHNqtnsTP
"""

import pandas as pd

Reviewdata=pd.read_csv('testdata.csv')

Reviewdata.shape

Reviewdata.head()

Reviewdata.info()

Reviewdata.describe().transpose()

count = Reviewdata.isnull().sum().sort_values(ascending=False)
percentage = ((Reviewdata.isnull().sum()/len(Reviewdata)*100)).sort_values(ascending=False)
missing_data = pd.concat([count,percentage],axis=1,
keys = ['Count','Percentage'])
print('Count and percentage of missing values for the coloumns:')

missing_data

