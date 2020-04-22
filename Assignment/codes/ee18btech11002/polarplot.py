# Code by Abhishek Shetkar
# 22/04/2020
# Released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
import control

w = np.append(np.linspace(0,0.1,1000),np.linspace(0.1,20,1000)) #ranging omega

unici = np.linspace(0 ,2*np.pi, 2000)
val = np.ones((2000,))
#phi = -PHASE.reshape((2001,))[idx]
#G(s)
s = control.TransferFunction.s
G = 1/((s)*(1+s)*(1+s))                                       

Mag, Ph, W = G.freqresp(w)

#Plotiing polar plot

ax = plt.subplot(111, projection='polar')

ax.plot(Ph.reshape((2000,))[-995:-800],Mag.reshape((2000,))[-995:-800])
ax.plot(unici.reshape((2000,)), val) 
#ax.plot(phi, 1, 'o', label = '$\omega_{gc}$' )
plt.show()


#inverse polar plot G(s) ie. polar plot of 1/G(s)

s = control.TransferFunction.s
iG = (s)*(1+s)*(1+s)                                       

iMag, iPh, iW = iG.freqresp(w)

#Plotiing inverse polar plot

ax = plt.subplot(111, projection='polar')

ax.plot(iPh.reshape((2000,))[-995:-800],iMag.reshape((2000,))[-995:-800])

plt.show()
