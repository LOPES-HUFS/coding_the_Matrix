#Task 2.4.17

import math
import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt

pi = math.pi
e = math.e
n = 20

temp=[np.exp(2*pi*1j/n) for n in range(1,21)]

plt.figure(figsize=(5,5))
plt.axvline(x=0,color='r')
plt.axhline(y=0,color='r')
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.plot([i.real for i in temp],[i.imag for i in temp],"p")
plt.show()