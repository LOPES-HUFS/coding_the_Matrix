#Task 2.4.18

import matplotlib as mpl
import matplotlib.pylab as plt

S={2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j}

plt.figure(figsize=(5,5))
pi_4_s =[np.exp(pi/4*1j)*k for k in S]
plt.axvline(x=0,color='r')
plt.axhline(y=0,color='r')
plt.xlim(-4,4)
plt.ylim(-4,4)
plt.scatter([i.real for i in pi_4_s],[i.imag for i in pi_4_s])
plt.show()
