import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

fig, ax = plt.subplots(figsize=(5,3))

ax.yaxis.grid(which="major", color='r', linestyle='-', linewidth=2)

ml = MultipleLocator(0.02)
ax.xaxis.set_minor_locator(ml)
ax.xaxis.grid(which="minor", color='k', linestyle='-.', linewidth=0.7)

plt.show()
