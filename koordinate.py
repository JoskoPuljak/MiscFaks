import csv
import math as mt
import numpy as np
import matplotlib.pyplot as plt
def koordinate (csvfile,interval):
    with open (csvfile, "r") as file:
        reader=csv.reader(file)
        points=[(0,0)]
        angle=0
        direction=0
        for line in reader:
            if line[0]=="Straight":
                for j in np.arange(0,float(line[1]),interval):
                    points.append((points[-1][0]+interval*np.cos(direction),points[-1][1]+interval*np.sin(direction)))
                angle=np.arctan2(points[-1][1],points[-1][0])
                direction=0
            elif line[0]=="Left":
                if angle ==0:
                    point0=(points[-1][0],points[-1][1])
                    R=float(line[2])
                    theta0=-mt.pi/2 
                    for i in np.arange (0,float(line[1]),interval):
                        theta=theta0+((i)/float(line[2]))
                        points.append((point0[0]+R*np.cos(theta),point0[1]+R+R*np.sin(theta)))
                    angle=np.arctan2(points[-1][1],points[-1][0])
                    if (points[-1][0]-point0[0])!=0:
                        print(points[-1])
                        print(points[-1][0]-point0[0])
                        slope=-1/((points[-1][1]-R)/(points[-1][0]-point0[0]))
                        direction=np.pi-np.arctan(slope)
                    else:
                        direction=0
                else: 
                    point0=(points[-1][0],points[-1][1])
                    R=float(line[2])
                    k=np.tan(point0[1]/point0[0])
                    kperp=-1/k
                    l=point0[1]-kperp*point0[0]
                    x=((-2*kperp*l)-np.sqrt(4*kperp**2*l**2-4*(l**2-R**2)*(1+k**2)))/(2*(1+k**2))
                    y=k*x+l
                    theta0=np.arctan2(point0[1]-y,point0[0]-x)
                    for i in np.arange (0,float(line[1]),interval):
                        theta=theta0+((i)/float(line[2]))
                        points.append((x+point0[0]+R*np.cos(theta),point0[1]+y+R*np.sin(theta)))
                    angle=np.arctan2(points[-1][1],points[-1][0])
                   
        print (points)
        x=[i[0] for i in points]
        y=[i[1] for i in points]
        plt.scatter(x,y)
        plt.show()
        plt.savefig("staza.png")               

    


koordinate("podacistaze.csv",0.005)