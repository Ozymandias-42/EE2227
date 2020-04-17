# Code by Abhishek Shetkar
# 16/04/2020
# Released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt

w = np.append(np.linspace(0.001,1,100),np.linspace(1,10,1000)) #ranging omega

#|G(jw)|
modGjw = 1/(w*(1+w*w))                                        

# Phase G(jw)
phase = -(np.pi/2) - 2*np.arctan(w)                            

#x-coordinate in polar plot is |G(jw)|*cos(Phase)
x = modGjw*np.cos(phase)
#y-coordinate in polar plot is |G(jw)|*sin(Phase)                                       
y = modGjw*np.sin(phase)									   

plt.grid()
plt.plot(x,y)
plt.xlim([-0.6,0.1])
plt.ylim([-0.01,0.1])

plt.show()
#for inverse plot, we plot 1/(G(w)) with varying w, therefore inversephase is -(phase)
invphase = (np.pi/2) + 2*np.arctan(w)              
            
x2 = np.cos(invphase)/modGjw
y2 = np.sin(invphase)/modGjw

plt.grid()
plt.plot(x2,y2)
plt.show()
