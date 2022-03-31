import numpy as np
import matplotlib.pyplot as plt

def h(w,t):
    delta_t = t - 5
    return 2.0*np.pi/(1.0 + np.exp(-delta_t/w))

t = np.linspace(0,10)
w = 1
y =h(w,t)

plt.plot(t,y)
plt.show()
