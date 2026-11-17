import numpy as np
import matplotlib.pyplot as plt

class SVM:
    def __init__(self):
        self.w = np.zeros(2)
        self.b = 0

    def fit(self,X,Y,lr=0.01,epoch=1000):
    # the learning rate control how big a step the model takes when updating its weight and bais
       
      for j in range(epoch): 
       for i in range(len(X)):
           score = np.dot(self.w,X[i]) + self.b     #negative for cat/posittive for dog/0 is hypothesis

           # check SVM margin (for mis/calssification)
           '''
           remember these threee points

           score = 0 -> Hyperplane

           y[i] * score >= 1 -> margin requirement satisfied

           y[i] * score < 1 -> update weight and bias in our simplifier a 
           
           '''
           if Y[i] * score < 1:

               self.w = self.w + lr * Y[i] * X[i]
               self.b = self.b + lr * Y[i]

    def predict(self, X):

        score = np.dot(self.w, X) + self.b 

        if score > 0:
            return "Dog"
        else :
            return "Cat"

    def plot(self, X ,Y):

        # plot Cats
        plt.scatter(X[Y == -1,0], X[Y == -1, 1],color = "blue", label="Cat")  

        # plot Dogs
        plt.scatter(X[Y == 1,0], X[Y == 1,1],color = "red", marker="s",label="Dog")

        plt.title("SVM: Cat vs Dog")
        plt.xlim(0,30)
        plt.ylim(0,75)
        plt.legend()
        plt.grid(True)
        plt.show()

# weight and height scaled between  0 and 1

X = np.array([
    [2,20],      #Cat
    [3,25],       #Cat
    [4,30],        #Cat
    [15,50],        #Dog
    [20,60],       #Dog 
    [25,70]        #Dog
])

#  Cat = -1, Dog = +1

Y = np.array([-1,-1,-1,1,1,1])

model = SVM()

model.fit(X,Y)

new_animal = np.array([5,25])

print("prediction:", model.predict(new_animal))
print("Weight:", model.w)
print("Bias:", model.b)
model.plot(X,Y)