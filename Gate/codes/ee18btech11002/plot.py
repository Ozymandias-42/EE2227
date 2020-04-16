import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,6,1000)
y = 1-(np.exp(-x))-(x*np.exp(-x))
plt.plot(4.52218,0.94,'o')
plt.text(3.4,0.95,'(4.52,0.94)')
plt.grid()
plt.plot(x,y)
plt.show()
