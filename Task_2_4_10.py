#Task 2.4.10

from PIL import Image
import numpy as np

im=Image.open('image/img01.png')
temp=plt.imshow(im)
temp=np.array(im)

pts=[{"y":y,"x":x}  for y,value in enumerate(data_temp) for x,k in enumerate(value) if k < 120]
pts_i=[i['x']+i['y']*1j for i in pts]

plt.figure(figsize=(7,7))
plt.xlim(-200,200)
plt.ylim(-200,200)
plt.axvline(x=0,color='r')
plt.axhline(y=0,color='r')
plt.scatter([i.real for i in pts_i],[i.imag for i in pts_i])
plt.show()