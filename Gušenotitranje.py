
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as ani

#klasa
def sgn(number):
    if number<=0:
        return(-1)
    else:
        return(1)
class HarmonicOscillator:
    #početni uvjeti
    def __init__(self,k,m,v0,x0,C1,C2):
        self.C2=C2
        self.C1=C1
        self.k=k
        self.m=m
        self.t1=[0]
        self.x1=[x0]
        self.v1=[v0]
        self.t2=[0]
        self.x2=[x0]
        self.v2=[v0]
        self.a1=[-(self.k/self.m)*x0-(self.C1*self.v1[0])/self.m]
        self.a2=[-(self.k/self.m)*x0-(self.C1*self.v2[0])/self.m-(1*sgn(self.v2[0])*self.C2*(self.v2[0]**2))/self.m]
    #resetiranje lista
    def reset(self):
        self.t1=[self.t1[0]]
        self.x1=[self.x1[0]]
        self.v1=[self.v1[0]]
        self.a1=[self.a1[0]]
        self.t2=[self.t2[0]]
        self.x2=[self.x2[0]]
        self.v2=[self.v2[0]]
        self.a2=[self.a2[0]]
    #punjenje lista
    def oscillate1(self,t,dt):
        for i in np.arange(0,t,dt):
            self.t1.append(self.t1[-1]+dt)
           
            self.v1.append(self.v1[-1]+(self.a1[-1]*dt))
            self.x1.append(self.x1[-1]+(self.v1[-1]*dt))
            self.a1.append(-(self.k/self.m*self.x1[-1])-(self.C1*self.v1[-1])/self.m)
            
    def oscillate2(self,t,dt):
        for i in np.arange(0,t,dt):
            self.t2.append(self.t2[-1]+dt)
            
            self.v2.append(self.v2[-1]+(self.a2[-1]*dt))
            self.x2.append(self.x2[-1]+(self.v2[-1]*dt))
            self.a2.append(-(self.k/self.m)*self.x2[-1]-(self.C1*self.v2[-1])/self.m-(1*sgn(self.v2[-1])*self.C2*(self.v2[-1]**2))/self.m)
    #crtanje        
    def plot_trajectory(self):
        plt.subplot(3,1,1)
        plt.plot(self.t1,self.x1,color="purple")
        plt.plot(self.t2,self.x2,color="green")
        plt.subplot(3,1,2)
        plt.plot(self.t1,self.v1,color="purple")
        plt.plot(self.t2,self.v2,color="green")
        
        plt.subplot(3,1,3)
        plt.plot(self.t1,self.a1,color="purple")
        
        plt.plot(self.t2,self.a2,color="green")
     
        plt.show()
        plt.savefig("graf.png")
    def plot_x(self,colour,size=30):
        plt.scatter(self.t1,self.x1,color=colour,s=size)

    
    
      
             
             