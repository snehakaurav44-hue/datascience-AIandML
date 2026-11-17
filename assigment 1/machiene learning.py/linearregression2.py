import numpy as np
import pandas as pd 
import mllib
class linearregression2:
    def loadfile(self,filename):
        self.data=pd.read_csv(filename)
        print(self.data.columns.tolist())
    def datacleaning(self,categorial,numerical,target):
        self.categorial=categorial
        self.numerical=numerical
        self.target=target

        self.data=mllib.encoder(self.data,categorial)
        self.data=self.data.dropna()
    def fit(self):
        x=self.data[self.categorial+self.numerical] 
        y=self.data[self.target] 
        x_train,y_train,x_test,y_test=mllib.test_train_splits(x,y)  
        x_train=x_train.to_numpy()
        y_train=y_train.to_numpy()

        one=np.ones((len(x_train),1))
        x_train=np.c_[one,x_train]

        result=np.linalg.pinv(x_train.T@x_train)@x_train.T@y_train
        self.intercept=result[0]
        self.slope=result[1:]
        print(result)

        for i,v in enumerate(self.categorial+self.numerical):
            print(v,self.slope[i])
    def predict(self,mydata):
        print(mydata)
        values=mydata.values()
        s=self.intercept
        for i,v in enumerate(values):
            s=s+self.slope[i]*v
            print(s)            

model=linearregression2()
model.loadfile("D:/mumbai_dataset.csv")
num=["area","bedroom_num","bathroom_num","balcony_num","age","total_floors"]
cat=['locality','city','property_type','furnished']
model.datacleaning(cat,num,'price')
model.fit()
mydata={"city":1,"property_type":1,"furnished":0,"area":200,"bedroom_num":3,"balcony_num":2,"bathroom_num":3,"age":2,"total_floors":1}
model.predict(mydata)

