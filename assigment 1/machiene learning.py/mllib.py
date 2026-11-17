import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
def test_train_splits(data_x,data_y):
    l=len(data_x)
    train_size=int(l*0.8)
    test_size=int(l*0.2)
    return[data_x.loc[0:train_size],data_y.loc[0:train_size],data_x.loc[train_size:l],data_y.loc[train_size:l]]

def encoder(data,col_list):
    for col in col_list:
       T=data[col].unique()
       T=sorted(T)
       mapping={}
       for i,v in enumerate(T):
          mapping[v]=i 
       data[col]=data[col].map(mapping)
    return data
# def encode_column(data,columns):
#     for col in col_list:
#         t=data[col].unique()
#     data=pd.het_dummies(data,columns=colmns,dtype=int)
#     print(data)       