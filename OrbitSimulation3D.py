#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 21:32:21 2020

@author: santi
"""
#Pakete
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
#Konstanten
G = 6.67430e-11 #in m3/kg*s2
m_sonne = 1.989e30 #in kg
m_erde = 5.972e24 #in kg (wird in dieser Lösung vernachlässigt, da die Sonne als stationär im Punkt (x,y,z)=(0,0,0) angenohmen wird)
#Startparameter von Merkur
y0_merkur = 0.58e11
x0_merkur = 0
z0_merkur = 0
v_x0_merkur=-47.87e3 #negativ die Rotation in Richtung gegen den Uhrzeigersinn laufen zu lassen
v_y0_merkur=0
v_z0_merkur= 0
#Startparameter von Venus
y0_venus = 1.08e11
x0_venus = 0
z0_venus = 0
v_x0_venus=-35.02e3 #negativ die Rotation in Richtung gegen den Uhrzeigersinn laufen zu lassen
v_y0_venus=0
v_z0_venus = 0
#Startparameter der Erde
y0_erde = 1.496e11 #in m
x0_erde = 0
z0_erde = 0
v_x0_erde=-29.78e3 #in m/s #negativ die Rotation in Richtung gegen den Uhrzeigersinn laufen zu lassen
v_y0_erde=0
v_z0_erde = 0
#Startparameter von Mars
y0_mars = 2.28e11
x0_mars = 0
z0_mars = 0
v_x0_mars=-24.13e3 #negativ die Rotation in Richtung gegen den Uhrzeigersinn laufen zu lassen
v_y0_mars=0
v_z0_mars = 0
#Startparameter von Jupiter
y0_jupiter = 7.78e11 
x0_jupiter = 0
z0_jupiter = 0
v_x0_jupiter=-13.07e3 #negativ die Rotation in Richtung gegen den Uhrzeigersinn laufen zu lassen
v_y0_jupiter=0
v_z0_jupiter = 0
#Startparameter von Saturn
y0_saturn = 14.33e11
x0_saturn = 0
z0_saturn = 0
v_x0_saturn=-9.69e3 #negativ die Rotation in Richtung gegen den Uhrzeigersinn laufen zu lassen
v_y0_saturn=0
v_z0_saturn = 0
#Startparameter von Uranus
y0_uranus = 28.72e11
x0_uranus = 0
z0_uranus = 0
v_x0_uranus=-6.81e3 #negativ die Rotation in Richtung gegen den Uhrzeigersinn laufen zu lassen
v_y0_uranus=0
v_z0_uranus = 0
#Startparameter von Neptun
y0_neptun = 44.95e11
x0_neptun = 0
z0_neptun = 0
v_x0_neptun=-5.43e3 #negativ die Rotation in Richtung gegen den Uhrzeigersinn laufen zu lassen
v_y0_neptun=0
v_z0_neptun = 0
#Differentialgleichung in 3D
def dgl_umlauf_sonne(i, t):
    x, y, z, v_x, v_y, v_z = i #Input für die Startparameter 
    g = G*m_sonne/np.sqrt(x**2+y**2)**3; #der angreifende Parameter an jedem Punkt x,y
    return [v_x, v_y, v_z, -x*g, -y*g, -z*g];
#Integration der DGL für Merkur
t = np.linspace(0, 31536000*100, 10000) #in SI-Einheiten ist die Angabe für ein Jahr auf Sekunden umgestellt 
startparameter_merkur = [x0_merkur, y0_merkur, z0_merkur, v_x0_merkur, v_y0_merkur, v_z0_merkur]
s_t_merkur = integrate.odeint(dgl_umlauf_sonne, startparameter_merkur, t, rtol=1e-8)
x_merkur,y_merkur,z_merkur,_,_,_ = s_t_merkur.T
#Integration der DGL für Venus
t = np.linspace(0, 31536000*100, 10000) #in SI-Einheiten ist die Angabe für ein Jahr auf Sekunden umgestellt 
startparameter_venus = [x0_venus, y0_venus, z0_venus, v_x0_venus, v_y0_venus, v_z0_venus]
s_t_venus = integrate.odeint(dgl_umlauf_sonne, startparameter_venus, t, rtol=1e-8)
x_venus,y_venus,z_venus,_,_,_ = s_t_venus.T
#Integration der DGL für die Erde
t = np.linspace(0, 31536000*100, 10000) #in SI-Einheiten ist die Angabe für ein Jahr auf Sekunden umgestellt 
startparameter_erde = [x0_erde, y0_erde, z0_erde, v_x0_erde, v_y0_erde, v_z0_erde]
s_t_erde = integrate.odeint(dgl_umlauf_sonne, startparameter_erde, t, rtol=1e-8)
x_erde,y_erde,z_erde,_,_,_ = s_t_erde.T
#Integration der DGL für Mars
t = np.linspace(0, 31536000*100, 10000) #in SI-Einheiten ist die Angabe für ein Jahr auf Sekunden umgestellt 
startparameter_mars = [x0_mars, y0_mars, z0_mars, v_x0_mars, v_y0_mars, v_z0_mars]
s_t_mars = integrate.odeint(dgl_umlauf_sonne, startparameter_mars, t, rtol=1e-8)
x_mars,y_mars,z_mars,_,_,_ = s_t_mars.T
#Integration der DGL für Jupiter
t = np.linspace(0, 31536000*10000, 10000) #in SI-Einheiten ist die Angabe für ein Jahr auf Sekunden umgestellt 
startparameter_jupiter = [x0_jupiter, y0_jupiter, z0_jupiter, v_x0_jupiter, v_y0_jupiter, v_z0_jupiter]
s_t_jupiter = integrate.odeint(dgl_umlauf_sonne, startparameter_jupiter, t, rtol=1e-8)
x_jupiter,y_jupiter,z_jupiter,_,_,_ = s_t_jupiter.T
#Integration der DGL für Saturn
t = np.linspace(0, 31536000*10000, 10000) #in SI-Einheiten ist die Angabe für ein Jahr auf Sekunden umgestellt 
startparameter_saturn = [x0_saturn, y0_saturn, z0_saturn, v_x0_saturn, v_y0_saturn, v_z0_saturn]
s_t_saturn = integrate.odeint(dgl_umlauf_sonne, startparameter_saturn, t, rtol=1e-8)
x_saturn,y_saturn,z_saturn,_,_,_ = s_t_saturn.T
#Integration der DGL für Uranus
t = np.linspace(0, 31536000*10000, 10000) #in SI-Einheiten ist die Angabe für ein Jahr auf Sekunden umgestellt 
startparameter_uranus = [x0_uranus, y0_uranus, z0_uranus, v_x0_uranus, v_y0_uranus, v_z0_uranus]
s_t_uranus = integrate.odeint(dgl_umlauf_sonne, startparameter_uranus, t, rtol=1e-8)
x_uranus,y_uranus,z_uranus,_,_,_ = s_t_uranus.T
#Integration der DGL für Neptun
t = np.linspace(0, 31536000*10000, 10000) #in SI-Einheiten ist die Angabe für ein Jahr auf Sekunden umgestellt 
startparameter_neptun = [x0_neptun, y0_neptun, z0_neptun, v_x0_neptun, v_y0_neptun, v_z0_neptun]
s_t_neptun = integrate.odeint(dgl_umlauf_sonne, startparameter_neptun, t, rtol=1e-8)
x_neptun,y_neptun,z_neptun,_,_,_ = s_t_neptun.T
#Plot-Rahmen 
fig1 = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlim3d(-3e11,3e11)
ax.set_ylim3d(-3e11,3e11)
ax.set_zlim3d(-3e11,3e11)
#Für den Plot der Sonne im Koordinatenursprung
r_s=6.96342e8
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x_s = np.cos(u)*np.sin(v)*r_s
y_s = np.sin(u)*np.sin(v)*r_s
z_s = np.cos(v)*r_s
ax.plot_wireframe(x_s, y_s, z_s, color="r",label='Sonne')
#Plot der inneren Umlaufbahnen
ax.plot3D(x_merkur,y_merkur,z_merkur, 'brown',label='Umlaufbahn von Merkur')
ax.plot3D(x_venus,y_venus,z_venus, 'orange',label='Umlaufbahn von Venus')
ax.plot3D(x_erde, y_erde, z_erde, 'blue',label='Erdumlaufbahn')
ax.plot3D(x_mars,y_mars,z_mars, 'red',label='Umlaufbahn von Mars')
#Plot-Rahmen 
fig2 = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlim3d(-50e11,50e11)
ax.set_ylim3d(-50e11,50e11)
ax.set_zlim3d(-50e11,50e11)
#Für den Plot der Sonne im Koordinatenursprung
r_s=6.96342e8
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x_s = np.cos(u)*np.sin(v)*r_s
y_s = np.sin(u)*np.sin(v)*r_s
z_s = np.cos(v)*r_s
ax.plot_wireframe(x_s, y_s, z_s, color="r",label='Sonne')
#Plot der äußeren Umlaufbahnen
ax.plot3D(x_jupiter,y_jupiter,z_jupiter, 'brown',label='Umlaufbahn von Jupiter')
ax.plot3D(x_saturn,y_saturn,z_saturn, 'orange',label='Umlaufbahn von Saturn')
ax.plot3D(x_uranus,y_uranus,z_uranus, 'cyan',label='Umlaufbahn von Uranus')
ax.plot3D(x_neptun,y_neptun,z_neptun, 'blue',label='Umlaufbahn von Neptun')
plt.show()
