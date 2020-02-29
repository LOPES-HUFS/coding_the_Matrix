#Task 2.4.9

import matplotlib as mpl
import matplotlib.pylab as plt

s =[(-1j*k)/2 for k in S]
plt.axvline(x=0,color='r')
plt.axhline(y=0,color='r')
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.scatter([i.real+2 for i in s],[i.imag-1 for i in s])
plt.show()
