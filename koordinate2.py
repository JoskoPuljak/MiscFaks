#importanje librarya
import csv
import math as mt
import numpy as np
import matplotlib.pyplot as plt
#definiranje funkcije
def koordinate (csvfile,interval):
    with open (csvfile, "r") as file: #otvaranje filea
        reader=csv.reader(file)       #saveanje filea ka reader objekt
        points=[(0,0)]                #počinje od 0,0 koordinata
        direction=0                   #kut je 0
        predznak=1                    #varijabla koja ce trebati kasnije
        for line in reader:           #za svaku liniju u file-u
            if line[0]=="Straight":   #ako je u prvom stupcu "Straight"
                for j in np.arange(0,float(line[1]),interval):  #loop koji traje od 0 do duljine segmenta zadane u drugom stupcu filea
                    points.append((points[-1][0]+interval*np.cos(direction),points[-1][1]+interval*np.sin(direction))) #dodaje se tocka koja je za interval udaljena od prošle. x i y koordinate su izračunate pomoću kuta
            elif line[0]=="Left": #ako je u prvom stupcu "Left"
                if direction==0: #mora se provjeriti je li kut 0 jer se računa 1/tangens kuta pa nesmije bit 0
                    point0=(points[-1][0],points[-1][1]) #točka u kojoj počinje skretati
                    R=float(line[2]) #čita radijus krivulje iz drugog stupca filea
                    xc=point0[0]   #središte kružnice po kojoj se kreće ima istu x koordinatu kao i početna točka
                    if point0[0]>points[-2][0]:  #ako se kreće prema desno onda je y koordinata radijus iznad početne točke za R
                        yc=point0[1]+R
                    else:
                        yc=point0[1]-R #u suprotnom je ispod
                    theta0=-mt.pi/2   #početni u kojem se nalazi točka u odnosu na središte (-pi/2 radijana)
                    for i in np.arange (0,float(line[1])+interval,interval): #loop koji traje od 0 do duljine segmenta
                        theta=theta0+((i)/float(line[2])) #dodaje početnom kutu dio kuta ovisno o djelicu kruznog luka
                        points.append((xc+R*np.cos(theta),yc+R*np.sin(theta)))  #dodaje se točka koja je za Rcos(theta) udaljena od središta po x-u i za Rsin(theta) po y-u
                    if (points[-1][0]-point0[0])!=0: #ako se početna točka i konačna točka zavoja ne nalaze na istom x-u onda smjer nije nula
                        direction=np.pi/2+ np.arctan2(points[-1][1]-yc,points[-1][0]-xc) # novi smjer je okomit na normalu kružnice koja prolazi kroz konačnu točku putanje
                    else:
                        direction=0 #inače je smjer 0 stupnjeva
                else: 
                    point0=(points[-1][0],points[-1][1]) #početna točka putanje
                    R=float(line[2])  #čita radijus iz drugog stupca
                    k=(points[-1][1]-points[-2][1])/(points[-1][0]-points[-2][0]) #koeficijent smjera tangentu na krivulju (Pretpostavljeno je da prije zavoja uvijek bude straight) 
                    if np.arctan2(points[-1][1]-points[-2][1],points[-1][0]-points[-2][0])<0: #ako je putanja usmjerena prema donja dva kvadranta
                        predznak=-1  #predznak je drukčiji
                    else:
                        predznak=1 #inače je isti
                    kperp=-1/k  #koeficijent smjera normale na krivulju
                    l=point0[1]-kperp*point0[0] #odsjecak na y osi normale na krivulju
                    xc=(point0[0]-predznak*R*np.cos(np.arctan(kperp))) #centar kružnice koja opisuje zavoj je za Rcos(kut između x osi i normale) lijevo od početne točke zavoja (osim u donja dva kvadranta)
                    yc=kperp*xc+l #y koordinata je izračunata pomoću formule za normalu
                    theta0=np.arctan2(point0[1]-yc,point0[0]-xc) #kut početne točke u odnosu na centar kružnice
                    for i in np.arange (0,float(line[1])+interval,interval): #loop ide od nula do duljine segmenta
                        theta=theta0+((i)/float(line[2])) #dodaje početnom kutu dio kuta ovisno o djelicu kruznog luka
                        points.append((xc+R*np.cos(theta),yc+R*np.sin(theta))) ##dodaje se točka koja je za Rcos(theta) udaljena od središta po x-u i za Rsin(theta) po y-u
                    if (points[-1][0]-xc)!=0: #ako krajnja točka putanje nije na istoj x koordinati kao središte kružnice onda smjer nijenula
                        direction=np.pi/2+ np.arctan2(points[-1][1]-yc,points[-1][0]-xc) # novi smjer je okomit na normalu kružnice koja prolazi kroz konačnu točku putanje
                    else:
                        direction=0 #inače je smjer 0 stupnjeva

            elif line[0]=="Right": #ako je u prvom stupcu desno
                if direction ==0:
                    point0=(points[-1][0],points[-1][1])
                    R=float(line[2])
                    xc=point0[0]
                    if point0[0]>points[-3][0]: #obrnuti su smjerovi središta
                        yc=point0[1]-R
                    else:
                        yc=point0[1]+R
                    theta0=mt.pi/2 
                    for i in np.arange (0,float(line[1])+interval,interval):
                        theta=theta0-((i)/float(line[2]))  #kut se oduzima umjesto dodaje
                        points.append((xc+R*np.cos(theta),yc+R*np.sin(theta)))
                    if (points[-1][0]-point0[0])!=0:
                        direction=-np.pi/2+ np.arctan2(points[-1][1]-yc,points[-1][0]-xc)
                    else:
                        direction=0
                else: 
                    point0=(points[-1][0],points[-1][1])
                    R=float(line[2])
                    k=(points[-1][1]-points[-2][1])/(points[-1][0]-points[-2][0])
                    if np.arctan2(points[-1][1]-points[-2][1],points[-1][0]-points[-2][0])<0: 
                        predznak=-1 #predznak je obrnut
                    else:
                        predznak=1
                    kperp=-1/k
                    l=point0[1]-kperp*point0[0]
                    xc=(point0[0]+predznak*R*np.cos(np.arctan(kperp))) #centar kružnice koja opisuje zavoj je za Rcos(kut između x osi i normale) desno od početne točke zavoja (osim u donja dva kvadranta)
                    yc=kperp*xc+l
                    theta0=np.arctan2(point0[1]-yc,point0[0]-xc)
                    for i in np.arange (0,float(line[1])+interval,interval):
                        theta=theta0-((i)/float(line[2])) #kut se oduzima umjesto dodaje
                        points.append((xc+R*np.cos(theta),yc+R*np.sin(theta)))
                    if (points[-1][0]-xc)!=0: 
                        direction=-np.pi/2+ np.arctan2(points[-1][1]-yc,points[-1][0]-xc)
                    else:
                        direction=0
        print (points) #ispišu se sve točke
        x=[i[0] for i in points]
        y=[i[1] for i in points] 
        plt.scatter(x,y) #plotaju se točke
        plt.xlim(-800,1300)
        plt.ylim(-800,1300)
        
        plt.show()
        plt.savefig("staza.png")               

    


koordinate("Motorland_Aragon2.csv",0.01)