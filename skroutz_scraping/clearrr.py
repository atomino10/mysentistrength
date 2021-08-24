import pandas as pd
import csv
from itertools import zip_longest
from difflib import SequenceMatcher
from hunspell import Hunspell
import os


mode='nonbin'

data = pd.read_csv("dirtyreviews.csv",encoding = "utf-8")
print('peos')
data=data.drop('topic',1)
data=data.drop('title',1)

data=data.dropna()
data=data.drop_duplicates(subset=['comment'], keep='first')
temp=[]
temp=data['stars'].values.tolist()
name='reviewstars'+mode
if mode=='bin':
	for i in range(0,len(data['stars'])):
		
		if int(temp[i])<=3:
			temp[i]=0;
		else:
			temp[i]=1;	

else:
	for i in range(0,len(data['stars'])):
		
		if int(temp[i])<=2:
			temp[i]=-1;
		elif int(temp[i])==3:
			temp[i]=0;
		else:		
			temp[i]=1;
data['stars']=temp

cols=data.columns.tolist()
cols = cols[-1:] + cols[:-1]
data=data[cols]

data.to_csv(name+'short.csv',header=['reviews','sentiment'],index=False,encoding = "utf-8")

