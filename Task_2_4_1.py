#Task 2.4.1

import matplotlib as mpl
import matplotlib.pylab as plt

S={2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j}

plt.axvline(x=0,color='r')
plt.axhline(y=0,color='r')
plt.xlim(-4,4)
plt.ylim(-4,4)
plt.plot([i.real for i in S],[i.imag for i in S],"p")