# Code by Abhishek Shetkar
# 23/04/2020
# Released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
import control

#ranging omega
w = np.append(np.linspace(0,0.1,1000),np.linspace(0.1,20,1000)) 
#for unit circle
unici = np.linspace(0 ,2*np.pi, 2000)
val = np.ones((2000,))

#G(s)
s = control.TransferFunction.s
G = 1/((s)*(1+s)*(1+s))                                       

Mag, Ph, W = G.freqresp(w)

#Plotiing polar plot

ax = plt.subplot(111, projection='polar')

ax.plot(Ph.reshape((2000,))[-995:-800],Mag.reshape((2000,))[-995:-800])
ax.plot(unici.reshape((2000,)), val)
#plotting (-1,0)
ax.plot(np.pi,1,'o') 
ax.text(3,2.25,'(-1,0)')

plt.show()


#inverse polar plot G(s) ie. polar plot of 1/G(s)

s = control.TransferFunction.s
iG = (s)*(1+s)*(1+s)                                       

iMag, iPh, iW = iG.freqresp(w)

#Plotiing inverse polar plot

ax = plt.subplot(111, projection='polar')

ax.plot(iPh.reshape((2000,))[-995:-800],iMag.reshape((2000,))[-995:-800])

plt.show()
