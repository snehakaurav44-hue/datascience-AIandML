import numpy as np
import matplotlib.pyplot as plt
class linearregression:
    def __init__(self,x,y):
        self.__x = np.array(x)
        self.__y = np.array(y)
    def cc(self):
        sx=sum(self.__x)
        sy=sum(self.__y)
        sxy=sum(self.__x*self.__y)
        xx=self.__x*self.__x
        yy=self.__y*self.__y
        sxx=sum(xx)
        syy=sum(yy)
        n=len(self.__x)
        r=(n*sox*soy-sox*soy)/np.sqrt((n*sox*x-sox*sox) * (n*soy*y*soy))
        return r

    def fit(self):
        self.b1=sum((self.__x-np.mean(self.__x))*(self.__y-np.mean(self.__y)))/sum((self.__x-np.mean(self.__x))**2)
        print("slope(b1):",self.b1)

        self.b0=np.mean(self.__y)-self.b1*np.mean(self.__x)
        print("intercept(b0):",self.b0)

        n=int(input("enter the bill amount:"))
        y=self.b0+self.b1*n
        # print("predicted tip values:",y)

    def predict(self,input):
            input_array=np.array(input)
            self.new_pred=self.b0+(self.b1*input_array)
            return self.new_pred
           
    def MSE(self):
        diff=self.__y-self.new_pred
        plt.scatter(self.__x,diff)
        plt.axhline(0)
        plt.show()
        sq=diff**2
        mse=sq.sum()
        N=len(self.__x)
        return mse/N
    
    def drawregressionline(self):
        plt.scatter(self.__x,self.__y,label="Regression Line")
        plt.plot(self.__x,self.new_pred,label="Regression Line")
        plt.xlabel('amount')
        plt.ylabel('tip')
        plt.show()