#Task 2.4.20

import matplotlib as mpl
import matplotlib.pylab as plt
from PIL import Image
import numpy as np

im=Image.open('image/img01.png')
temp=np.array(im)

pts=[{"y":y,"x":x}  for y,value in enumerate(data_temp) for x,k in enumerate(value) if k < 120]
pts_i=[(i['x']+i['y']*1j) for i in pts]

plt.figure(figsize=(7,7))
pts_45 =[k*np.exp(pi/4*1j)/2 for k in pts_i]
plt.xlim(-100,100)
plt.ylim(-100,100)
plt.axvline(x=1,color='r')
plt.axhline(y=1,color='r')
plt.scatter([i.real for i in pts_45],[i.imag-50 for i in pts_45])
plt.show()