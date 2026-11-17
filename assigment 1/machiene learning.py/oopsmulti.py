import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
class MultiplelinearRegression:
    def __init__(self,x1,x2,y):
        self.__x1=np.array(x1)
        self.__x2=np.array(x2)
        self.__y=np.array(y)
    
    def calculate(self):
        one=np.ones((len(self.__x1),1),dtype=int)
        print(one)

        # matrix:  
        self.x=np.c_[one,self.__x1,self.__x2]
        print("matrix:",self.x)
        
        # transpose:
        self.T=self.x.T
        print("Transpose:",self.T)
        
        self.multiply=self.T@self.x
        print(self.multiply)
        
        self.inv=np.linalg.pinv(self.multiply)
        print(np.round(self.inv,2))
        
        self.inv_m=self.inv@self.T
        print(np.round(self.inv_m,2))
        
        self.invm_y=self.inv_m@self.__y
        print(self.invm_y)

    def predict(self):
        a0=self.invm_y[0]
        a1=self.invm_y[1]
        a2=self.invm_y[2]
        y_pred=a0+(a1*self.__x1)+(a2*self.__x2)
        print(y_pred)
        return y_pred
    
    def drawregressionline(self):
        a0=self.invm_y[0]
        a1=self.invm_y[1]
        a2=self.invm_y[2]

        x1_grid,x2_grid=np.meshgrid(
            np.linspace(self.__x1.min(),self.__x1.max(),20),
            np.linspace(self.__x2.min(),self.__x2.max(),20))

        y_grid=a0+(a1*x1_grid)+(a2*x2_grid)

        fig=plt.figure()
        fig1=plt.figure()
        plt.scatter(self.__x1,self.__y)
        plt.plot(self.__x1,a0+(a1*self.__x1)+(a2*self.__x2))
        plt.xlabel("x1")
        plt.ylabel("y")
        plt.title("x1 vs y")



        ax=fig.add_subplot(111,projection='3d')

       
        ax.scatter(self.__x1,self.__x2,self.__y)
        ax.plot_surface(x1_grid,x2_grid,y_grid,alpha=0.5)
        ax.set_xlabel('x1')
        ax.set_ylabel('x2')
        ax.set_zlabel('y')
        return fig

    def streamlit(self):
        st.title("Multiple linear Regression") 
        st.write("Enter x1,x2 and y values")
        x1_input=st.text_input("Enter x1 values","1,2,3,4,5")   
        x2_input=st.text_input("Enter x2 values","2,4,6,8,10")
        y_input=st.text_input("Enter y values","10,20,30,40,50")
        if st.button("calculate"):
            try:
                x1=[float(i) for i in x1_input.split(",")]
                x2=[float(i) for i in x2_input.split(",")]
                y=[float(i) for i in y_input.split(",")]
                
                if len(x1)!=len(x2)or len(x1)!=len(y):
                    st.error("x1,x2 and y values must have same length")
                else:
                    model= MultiplelinearRegression(x1,x2,y)
                    model.calculate()
                    y_pred=model.predict()
                    st.write("predicted values:")
                    st.write(y_pred)
                    fig=model.drawregressionline()
                    st.pyplot(fig)
            except Exception as e:
                st.error(f"error:{e}")         