import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(1,100,10000)

modGjw = 1/(w*(1+w*w))

phase = -(np.pi/2) - 2*np.arctan(w)
x = modGjw*np.cos(phase)
y = modGjw*np.sin(phase)
plt.grid()
plt.plot(x,y)
plt.show()

