#Problem 2.4.6

import matplotlib as mpl
import matplotlib.pylab as plt

fig, ax = plt.subplots()
arrow=mpl.patches.FancyArrowPatch(posA=(0,0), posB=(-3,0),arrowstyle='-|>',mutation_scale=20)
arrow2=mpl.patches.FancyArrowPatch(posA=(-3,0), posB=(-3,3),arrowstyle='-|>',mutation_scale=20)
arrow.set_color("b")
ax.add_patch(arrow)
ax.add_patch(arrow2)
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
plt.axvline(x=0,color='r')
plt.axhline(y=0,color='r')
plt.show()