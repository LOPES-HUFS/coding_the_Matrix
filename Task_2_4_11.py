#Task 2.4.11

S={2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j}

def f(z):
    return [-i for i in z]

new_s=f(S)
plt.axvline(x=0,color='r')
plt.axhline(y=0,color='r')
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.scatter([i.real for i in new_s],[i.imag for i in new_s])
plt.show()
