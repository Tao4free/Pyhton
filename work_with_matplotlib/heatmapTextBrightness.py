# https://stackoverflow.com/questions/25071968/heatmap-with-text-in-each-cell-with-matplotlibs-pyplot

import numpy as np
import matplotlib.pyplot as plt    

title = "ROC's AUC"
xlabel= "Timeshift"
ylabel="Scales"
data =  np.random.rand(8,12)


plt.figure(figsize=(12, 6))
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
c = plt.pcolor(data, edgecolors='k', linewidths=4, cmap='RdBu', vmin=0.0, vmax=1.0)

def show_values(pc, fmt="%.2f", **kw):
    pc.update_scalarmappable()
    for p, color, value in zip(pc.get_paths(), pc.get_facecolors(), pc.get_array()):
        x, y = p.vertices[:-2, :].mean(0)
        if np.all(color[:3] > 0.5):
            color = (0.0, 0.0, 0.0)
        else:
            color = (1.0, 1.0, 1.0)
        plt.text(x, y, fmt % value, ha="center", va="center", color=color, **kw)

show_values(c)

plt.colorbar(c)

plt.show()
