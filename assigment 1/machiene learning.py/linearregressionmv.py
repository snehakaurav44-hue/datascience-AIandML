import pandas as pd 
import numpy as np
import mllib
class linearregressionmv:
    def loadfile(self,filename):
        self.data=pd.read_csv(filename)
        self.data=self.data.dropna()
        self.actual_data=self.data.copy()
    def datacleaning(self,categorial,numerical,target):
        self.categorial=categorial
        self.numerical=numerical
        self.target=target
        self.data=mllib.encoder(self.data,categorial)
        if(len(categorial)>0):
            data_encode,self.encoder_columns=mllib.encoder(self.data,categorial)
            self.data=pd.concat([self.data[numerical],data_encode],axis=1)
            self.columns=numerical+list(self.encoder_columns)
        print(self.data)
    def fit():
        x=self.data[self.categorial+self.numerical]
        y=self.data[self.target]
        x_train,Y_train,x_test,y_test=mllib.test_train_splits(x,y)
        x_train=x_tain.to_numpy()
        y_train=y_train.to_numpy()
        result=np.linalg.pinv(x_train.t@x_train)@x_train.t@y_train
        print(result)
model=linearregressionmv()
model.loadfile("D:/mumbai_dataset.csv")      
column=['locality','city','property_type','furnished']
model.datacleaning(cat,'num','price')
model.fit()