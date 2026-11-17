class NB:
    def fit(self,x,y):
       self.x=x
       self.y=y
       self.classes = list(set(y))
       print(self.classes)
       self.data={}
       for c in self.classes:
        self.data[c]=[x[i] for i in range(len(y)) if(c==y[i])]
        print(self.data)
        self.prob={}
        for c in self.data:
            self.prob[c]=(len(self.data[c]))/len(y) 
        print(self.prob)  

    def predict (self,x):
         for c in self.classes:
            rows=self.data[c]  
            p=self.prob[c]
            for j in range (len(x)):
              count=sum(x[i] for row in rows)
              values=len(set(row[j] for row in self.x))
              p*=(count+1)/(len(row)+values)
              result[c]=p
            print("evidence:")
            print(result)
            evidence=sum(result.values)
            for r in result:
               result[r]=result[r]/evidence
               print(result)
               print(max(result,key=result.get))  

x=[["sunny","hot","weak"],      
  ["sunny","hot","weak"],   
  ["sunny","hot","weak"],   
  ["sunny","hot","weak"],   
  ["sunny","hot","weak"],   
  ["sunny","hot","weak"]]


y=["no","no","yes","yes","yes","yes"]

model=NB()
model.fit(x,y)
# model.predict("sunny","cool","weak")