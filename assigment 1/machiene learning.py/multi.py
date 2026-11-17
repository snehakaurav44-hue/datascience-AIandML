import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import Linearregression
from sklearn.metrics import mean_absolute_error,mean_squared_error
df=pd.read_csv("D:/mumbai_dataset.csv")

num=["area","bedroom_num","bathroom_num","balcony_num","age","total_floor"]
cat=["locality","property_type","furnished"]
target=["price"]
required_columns=(num + cat + target)
df=df.drpna(subset = required_columns)
x=df[num + cat]
y=df["price"]
pre=columnTransformer([("cat",onehotencoder,)],cat,)
x=pre.fit_transform(x)
x_train,x_test,y_train,y_test=train_test_split(data_x,data_y)
model = Linearregression(fit(x_train,y_train))