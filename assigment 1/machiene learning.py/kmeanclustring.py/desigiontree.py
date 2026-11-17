
import math
class DT:
    def fit(self,x,y):
       self.x=x
       self.y=y
       self.classes = list(set(y))
       yes=y.count("yes")
       no=y.count("no")
       total=len(y)
       print(self.classes)
       print("yes:",yes)
       print("no:",no)
       print("total:",total)
       self.data={}
  
    def entropy(self,x,y):
        positive=[]
        negative=[]
      # sunny    
        for i in range (len(x)):
            if x[i][0]=="sunny":
               if y[i]=="yes":
                positive.append(x[i])
               elif y[i]=="no":
                 negative.append(x[i])
        
        print("positive count:",len(positive))
        print("negative count:",len(negative))

        # overcast 
        positive=[]
        negative=[]
        for i in range (len(x)):
           if x[i][0]=="overcast":
               if y[i]=="yes":
                positive.append(x[i])
               elif y[i]=="no":
                 negative.append(x[i])
        
        print("positive count:",len(positive))
        print("negative count:",len(negative))
      #  rain 
        positive=[]
        negative=[]
        for i in range (len(x)):
           if x[i][0]=="rain":
               if y[i]=="yes":
                positive.append(x[i])
               elif y[i]=="no":
                 negative.append(x[i])
        
        print("positive count:",len(positive))
        print("negative count:",len(negative))

# formula

        # p=0
        # n=0
        # for p,n in enumerate (s):
        #   s = -(p)log2(p)-(n)*log2(n)
      


x=[["sunny","hot","high","weak"],      
  ["sunny","hot","high","weak"],   
  ["overcast","hot","high","weak"],   
  ["rain","mild","high","weak"],   
  ["rain","cool","normal","weak"],   
  ["rain","cool","normal","strong"],
  ["overcast","cool","normal","strong"],
  ["sunny","mild","high","weak"],
  ["sunny","cool","normal","weak"],
  ["rain","mild","normal","weak"],
  ["sunny","mild","normal","strong"],
  ["overcast","mild","high","strong"],
  ["overcast","hot","normal","weak"],
  ["rain","mild","high","strong"]]


y=["no","no","yes","yes","yes","no","yes","no","yes","yes","yes","yes","yes","no"]


model=DT()
model.fit(x,y)
model.entropy(x,y)

