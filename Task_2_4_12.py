#Task 2.4.12

im=Image.open('img01.png')
temp=np.array(im)

pts=[{"y":y,"x":x}  for y,value in enumerate(data_temp) for x,k in enumerate(value) if k < 120]
pts_i=[(i['x']+i['y']*-1j)/2 for i in pts]

plt.axvline(x=0,color='r')
plt.axhline(y=0,color='r')
plt.xlim(-100,100)
plt.ylim(-100,100)
plt.scatter([i.real for i in pts_i],[i.imag for i in pts_i])
plt.show()