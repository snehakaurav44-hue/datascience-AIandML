import numpy as np
import matplotlib.pyplot as plt
color=["r","b"]
class kmean:
    def __init__(self,k):
        self.k=k
        self.centroid=None
        self.clusters=None
    def fit(self,data):
    
        data=np.array(data,float)
        self.centroid=data[:self.k]
        for i in range(100):
             clusters=[[] for i in range(self.k)]    
             for v in data:
                distance=[]
                for c in self.centroid:
                     dis=np.sqrt(np.sum((v-c)**2))
                     distance.append(dis)
                cluster_index=distance.index(min(distance))
                clusters[cluster_index].append(v)  
             print(clusters)
             nc=[]
             for cluster in clusters:
               if (len(cluster)>0):
                   nc.append(sum(cluster)/len(cluster))
               else:
                   nc.append(0)
             print(nc)       
             if np.array_equal(nc,self.clusters):
                 break
             self.centroid=nc
             self.clusters=clusters
    def show(self):
        print('clusters:')
        print(self.clusters)
        print('centroid:')
        print(self.centroid)    
    def  predict(self,value):
        distance=[]
        for centroid in self.centroid:
            dis=abs(value-centroid)
            distance.append(dis)
        return distance.index(min(distance))

    def showplot(self):
        for i in range(self.k):

          plt.scatter(self.clusters[i],[i+1]*len(model.clusters[i]),c=color[i])
          plt.scatter(self.centroid,range(1,self.k+1),c="g",s=100,marker="*")
          plt.yticks([1,2])
        plt.show()              


model=kmean(2)
data=[[2,4],[10,12],[3,20],[30,11],[25,10],[21,9],[60,14],[30,22],[33,21],[23,10]]
model.fit(data) 
model.show()
value=25
model.showplot()
p=model.predict(value)
print(value,"belongs to cluster",model.clusters[p])   
