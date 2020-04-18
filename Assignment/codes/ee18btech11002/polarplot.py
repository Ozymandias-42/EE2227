# Code by Abhishek Shetkar
# 16/04/2020
# Released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
import control

w = np.linspace(-20,20,2001) #ranging omega

#G(s)
s = control.TransferFunction.s
G = 1/((s)*(1+s)*(1+s))                                       

Mag, Ph, W = G.freqresp(w)

#Plotiing polar plot

ax = plt.subplot(111, projection='polar')

ax.plot(Ph.reshape((2001,))[-995:-800],Mag.reshape((2001,))[-995:-800])

plt.show()


#inverse polar plot G(s) ie. polar plot of 1/G(s)

s = control.TransferFunction.s
iG = (s)*(1+s)*(1+s)                                       

iMag, iPh, iW = iG.freqresp(w)

#Plotiing inverse polar plot

ax = plt.subplot(111, projection='polar')

ax.plot(iPh.reshape((2001,))[-995:-800],iMag.reshape((2001,))[-995:-800])

plt.show()
