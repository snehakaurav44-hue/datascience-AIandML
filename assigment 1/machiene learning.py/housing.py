import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
def test_train_splits(data_x,data_y):
    l=len(data_x)
    train_size=int(l*0.8)
    test_size=int(l*0.2)
    return[data_x.loc[0:train_size],data_x.loc[train_size:l],data_y.loc[0:train_size],data_y.loc[train_size:l]]

def encoder(data,col_list):
    for col in col_list:
       t=data[col].unique()
       t.sort()
       mapping={}
       for i,v in enumerate(t):
          mapping[v]=i 
          data[col]=data[col].map(mapping)
          return data

column=['locality','city','property_type','furnished']
data=pd.read_csv("D:/mumbai_dataset.csv")
print(data)
data_y=data['price']
print(data_y)
data_x=data.drop(['price'],axis=1)
print(data_x.columns)
x_train,x_test,y_train,y_test=train_test_split(data_x,data_y)
print(y_test)
print(y_train)
data_x.drop(['title'],inplace=True,axis=1)
print(data_x)