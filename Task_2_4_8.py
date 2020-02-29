#Task 2.4.8

import matplotlib as mpl
import matplotlib.pylab as plt

S={2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j}

s =[(-1j*k)/2 for k in S]
plt.axvline(x=0,color='r')
plt.axhline(y=0,color='r')
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.scatter([i.real for i in s],[i.imag for i in s])
plt.show()
