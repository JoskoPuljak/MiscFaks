import numpy as np
import matplotlib.pyplot as plt

class Dinamički_bicikl: #klasa cijelog vozila koja pamti karakteristike vozila, trenutne kinematičke veličine i ima svoje metode
    def __init__ (self,m,Cr,Cf,lr,lf,Iz,vlon,vlat,psidot,steer): #osnovni parametri i liste/polja
        self.m=m #masa vozila
        self.Cr=Cr #koeficijent lateralnog trenja stražnjeg kola
        self.Cf=Cf #koeficijent lateralnog trenja prednjeg kola
        self.lr=lr #duljina wheelbasea iza centra mase
        self.lf=lf #duljina wheelbasea ispred centra mase
        self.Iz=Iz #moment inercije vozila 
        self.vlon=vlon #longitudalna brzina- konstantna u zavoju
        self.vlat=[vlat] #matrica lateralnih brzina 
        self.psidot=[psidot] #matrica yaw ratea tojest kutnih brzina
        self.alat=[0] #matrica lateralnih ubrzanja/akceleracija
        self.omegadot=[0] #matrica kutne akceleracije/yaw akceleracije
        self.steer=steer #steer angle
        self.xlat=[0] #matrica lateralnih pomaka
        self.psi=[0] #matrica kutnih pomaka
        self.alphar=[0] #matrica slip anglea stražnjeg kola
        self.alphaf=[0] #matrica sip anglea prednjeg kola
        self.oveersteer=[]
    def reset(self): #metoda koja resetira sve liste/polja/matrice
        self.alat=[0] 
        self.omegadot=[0]
        self.vlat=[self.vlat[0]]
        self.psidot=[self.psidot[0]]
        self.xlat=[0]
        self.psi=[0]
        self.alphar=[0]
        self.alphaf=[0]
    def move(self,dt): #metoda koja pomice diferencijalne jednadžbe za jedan korak
        self.alat.append((-self.Cr-self.Cf)/(self.m*self.vlon)*self.vlat[-1]+(((self.Cr-self.Cf)/(self.m*self.vlon))-self.vlon)*self.psidot[-1]+(self.Cf/self.m)*self.steer)
        self.omegadot.append(((self.lr*self.Cr-self.lf*self.Cf)/(self.Iz*self.vlon))*self.vlat[-1]+((-self.lf**2*self.Cf+self.lr**2*self.Cr)/(self.Iz*self.vlon))*self.psidot[-1]+(self.Cf/self.Iz)*self.steer)
        self.vlat.append(self.vlat[-1]+self.alat[-1]*dt)
        self.psidot.append(self.psidot[-1]+self.omegadot[-1]*dt)
        self.xlat.append(self.xlat[-1]+self.vlat[-1]*dt)
        self.psi.append(self.psi[-1]+self.psidot[-1]*dt)
        self.alphar.append((self.vlat[-1]-self.psidot[-1]*self.lr)/(self.vlon))
        self.alphaf.append((-self.vlon*self.steer)/(self.vlon+(self.vlat[-1]+self.psidot[-1]*self.lf)*self.steer))
    def test(self,t,dt): #testiranje za n koraka
        self.reset()
        for i in np.arange(0,t,dt):
            self.move(dt)
        print(self.alat)
        print(self.omegadot)
        print(self.vlat)
        print(self.psidot)
        print(self.xlat)
        print(self.psi)
    def oversteertest(self): #stvaranje matrice koja testira za oversteer/understeer
        for i in range(len(self.alphar)):
            ackermannkin=self.steer #kinetički ackermann kut je jednak steer angleu
            ackermanndin=self.steer-self.alphaf[i]+self.alphar[i] # dinamički ackermann kut
            if ackermannkin>ackermanndin: # testiranje za oversteer
                self.oveersteer.append("Oversteer")
            elif ackermannkin<ackermanndin: #testiranje za understeer
                self.oveersteer.append("Understeer")
            else:
                self.oveersteer.append("Neutral steering")
        print(self.oveersteer)