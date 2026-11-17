import numpy as np
import matplotlib.pyplot as plt

class SVM:
    def __init__(self):
        self.w=np.zeros(2)
        self.b=0

    def fit(self,X,Y,lr=0.01,epoch=1000):
        # The learning rate controls how big a step the model takes when updating
        
        for j in range(epoch):
            for i in range(len(X)):
                score=np.dot(self.w, X[i]) +self.b
                # negative for cat/positive for dog/0 is hyperplane
            
                # check SVM margin(for mis/classification)
                '''
                remember these three points:
                score =0-hyperplaney[i]
                y[i]*score>=1-margin requirement satisfied
                y[i]*score<1-update weights and bias in our simpified a 
                '''
                if Y[i] * score < 1:
                    self.w=self.w+lr*Y[i]*X[i]
                    self.b=self.b+lr*Y[i]
        
    def predict(self,X):
        score = np.dot(self.w,X) + self.b 
        if score > 0:
            return "Dog"
        else:
            return "Cat"

    def plot(self,X,Y):
        # plot cats
        plt.scatter(X[Y==-1,0],X[Y==-1,1],color="blue",label="Cat")
        # plotDogs
        plt.scatter(X[Y==1,0], X[Y==1,1],color="red",marker="s",label="Dog")

        plt.title("SVM: Cat vs Dog")
        plt.xlim(0,30)
        plt.ylim(0,75)
        plt.legend()
        plt.grid(True)
        plt.show()



# weight and height scaled between 0 and 1
X=np.array([
    [2,20],
    [3,25],
    [4,30], 
    [15,50],
    [20,60],
    [25,70]
])

# cat =-1,dog=+1
Y=np.array([-1,-1,-1,1,1,1])

model=SVM()
model.fit(X,Y)

# test a new animal
new_animal=np.array([5,25])

print("prediction:", model.predict(new_animal))
print("weights:",model.w)
print("Bias:",model.b)
model.plot(X,Y)