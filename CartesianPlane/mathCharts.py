import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
x = np.linspace(0, 10, 160)
y = 2 * np.sin(2 * x) - 2

# plot
fig, ax = plt.subplots()
ax.xaxis.label.set_fontsize('x-large')
ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(0, 11), xticks=np.arange(-1, 10),
       ylim=(-4, 1), yticks=np.arange(-4, 1))

plt.show()