from IPython import display
import matplotlib.pyplot as plt
import numpy as np
import math as mt
import matplotlib.animation as ani

class TripleOscilator:
    def __init__(self,k,m,x10,x20,x30,v10,v20,v30):
        self.k=k
        self.m=m
        self.x1=[x10]
        self.x2=[x20]
        self.x3=[x30]
        self.v1=[v10]
        self.v2=[v20]
        self.v3=[v30]
        self.a1=[(self.k/self.m)*(self.x2[0]-2*self.x1[0])]
        self.a2=[(self.k/self.m)*(self.x3[0]-2*self.x2[0]+self.x1[0])]
        self.a3=[-(self.k/self.m)*(2*self.x3[0]-self.x1[0])]
    def reset(self):
        self.k=k
        self.m=m
        self.x1=[self.x1[0]]
        self.x2=[self.x2[0]]
        self.x3=[self.x3[0]]
        self.v1=[self.v1[0]]
        self.v2=[self.v2[0]]
        self.v3=[self.v3[0]]
    def oscilate(self,t,dt):
        for i in np.arange(0,t,dt):
            self.v1.append(self.v1[-1]+self.a1[-1]*dt)
            self.v2.append(self.v2[-1]+self.a2[-1]*dt)
            self.v3.append(self.v3[-1]+self.a3[-1]*dt)
            self.x1.append(self.x1[-1]+self.x1[-1]*dt)
            self.x2.append(self.x2[-1]+self.x2[-1]*dt)
            self.x3.append(self.x3[-1]+self.x3[-1]*dt)
            self.a1.append((self.k/self.m)*(self.x2[-1]-2*self.x1[-1]))
            self.a2=[(self.k/self.m)*(self.x3[-1]-2*self.x2[-1]+self.x1[-1])]
            self.a3=[-(self.k/self.m)*(2*self.x3[-1]-self.x1[-1])]
    def plot_trajectory(self,Save=True):
          plt.rcParams["figure.figsize"] = [5, 5]
          plt.rcParams["figure.autolayout"] = True
          fig=plt.figure()
          ax=plt.axes(xlim=(-0.1,0.1),ylim=(-0.12,0.1))
         
        
          line,=ax.plot([],[],"o",color="blue")
          line2,=ax.plot([],[],"o",color="red")
          line3,=ax.plot([],[],"o",color="yellow")
        
          def init():
            line.set_data([],[])
            line2.set_data([],[])
            line3.set_data([],[])
            return line,line2,line3
          def animate(i):
            x_1=self.x1[i]
            line.set_data(x_1,0)
            x_2=self.x2[i]
            line2.set_data(x_2,0)
            x_3=self.x3[i]
            line3.set_data(x_3,0)
            
    
            return line3,line,line2
          anim = ani.FuncAnimation(fig, animate, init_func=init, frames=667, interval=20, blit=True)
          plt.show()
          if Save:
            writer=ani.FFMpegWriter(fps=30)
            anim.save("test1.gif",writer=writer)
    
Jim=TripleOscilator(10,0.1,3,6,10,0,0,0)
Jim.oscilate(5,0.001)
Jim.plot_trajectory()