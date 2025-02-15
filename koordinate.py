import csv
import math as mt
import numpy as np
import matplotlib.pyplot as plt
def koordinate (csvfile,interval):
    with open (csvfile, "r") as file:
        reader=csv.reader(file)
        points=[(0,0)]
        direction=0
        for line in reader:
            if line[0]=="Straight":
                for j in np.arange(0,float(line[1]),interval):
                    points.append((points[-1][0]+interval*np.cos(direction),points[-1][1]+interval*np.sin(direction)))
            elif line[0]=="Left":
                if direction==0:
                    point0=(points[-1][0],points[-1][1])
                    R=float(line[2])
                    xc=point0[0]
                    if point0[0]>points[-2][0]:
                        yc=point0[1]+R
                    else:
                        yc=point0[1]-R
                    theta0=-mt.pi/2 
                    for i in np.arange (0,float(line[1]),interval):
                        theta=theta0+((i)/float(line[2]))
                        points.append((xc+R*np.cos(theta),yc+R*np.sin(theta)))
                    if (points[-1][0]-point0[0])!=0:
                        slope=((points[-1][1]-points[-2][1])/(points[-1][0]-points[-2][0]))
                        direction=np.arctan2(points[-1][1]-points[-2][1],points[-1][0]-points[-2][0])
                    else:
                        direction=0
                else: 
                    point0=(points[-1][0],points[-1][1])
                    R=float(line[2])
                    k=(points[-1][1]-points[-2][1])/(points[-1][0]-points[-2][0])
                    print(point0)
                    print(points[-2])
                    print(k)
                    kperp=-1/k
                    print(kperp)
                    l=point0[1]-kperp*point0[0]
                    xc=(point0[0]-R*np.cos(np.arctan(kperp)))
                    yc=kperp*xc+l
                    theta0=np.arctan2(point0[1]-yc,point0[0]-xc)
                    l2=yc-np.tan(theta0)*xc
                    for i in np.arange (0,float(line[1]),interval):
                        theta=theta0+((i)/float(line[2]))
                        points.append((xc+R*np.cos(theta),yc+R*np.sin(theta)))
                    if (points[-1][0]-point0[0])!=0:
                        slope=((points[-1][1]-points[-2][1])/(points[-1][0]-points[-2][0]))
                        direction=np.arctan2(points[-1][1]-points[-2][1],points[-1][0]-points[-2][0])
                    else:
                        direction=0
            elif line[0]=="Right":
                if direction ==0:
                    point0=(points[-1][0],points[-1][1])
                    R=float(line[2])
                    xc=point0[0]
                    if point0[0]>points[-2][0]:
                        yc=point0[1]-R
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    else:
                        yc=point0[1]+R
                    theta0=mt.pi/2 
                    for i in np.arange (0,float(line[1]),interval):
                        theta=theta0-((i)/float(line[2]))
                        points.append((xc+R*np.cos(theta),yc+R*np.sin(theta)))
                    if (points[-1][0]-point0[0])!=0:
                        slope=((points[-1][1]-points[-2][1])/(points[-1][0]-points[-2][0]))
                        direction=np.arctan2(points[-1][1]-points[-2][1],points[-1][0]-points[-2][0])
                    else:
                        direction=0
                else: 
                    point0=(points[-1][0],points[-1][1])
                    R=float(line[2])
                    k=(points[-1][1]-points[-2][1])/(points[-1][0]-points[-2][0])
                    print(point0)
                    print(points[-2])
                    print(k)
                    kperp=-1/k
                    print(kperp)
                    l=point0[1]-kperp*point0[0]
                    xc=(point0[0]+R*np.cos(np.arctan(kperp)))
                    yc=kperp*xc+l
                    theta0=np.arctan2(point0[1]-yc,point0[0]-xc)
                    l2=yc-np.tan(theta0)*xc
                    for i in np.arange (0,float(line[1]),interval):
                        theta=theta0-((i)/float(line[2]))
                        points.append((xc+R*np.cos(theta),yc+R*np.sin(theta)))
                    if (points[-1][0]-point0[0])!=0:
                        slope=((points[-1][1]-points[-2][1])/(points[-1][0]-points[-2][0]))
                        direction=np.arctan2(points[-1][1]-points[-2][1],points[-1][0]-points[-2][0])
                    else:
                        direction=0
        print (points)
        x=[i[0] for i in points]
        y=[i[1] for i in points]
        plt.scatter(x,y)
        
        plt.show()
        plt.savefig("staza.png")               

    


koordinate("podacistaze.csv",0.25)