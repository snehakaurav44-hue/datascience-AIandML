from oopsmulti import MultiplelinearRegression
import numpy as np

x1=np.array([1,2,3,4])
x2=np.array([4,5,8,2])
y=np.array([1,6,8,12])
obj=MultiplelinearRegression(x1,x2,y)
obj.calculate()
obj.predict()
obj.drawregressionline()
obj.streamlit()


