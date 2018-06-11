import numpy as np
import pynbody as pyn
import matplotlib.pyplot as plt
import matplotlib.cm as cm

path = "/home/grondjj/Data/RadTransfer/Isothemal_Spheres/CellPlot/"
data = pyn.load(path + "balls.00001")
data_sl = data.g[np.where(np.fabs(data.g['z']) < data.g['smooth'])]
xmin, xmax, ymin, ymax = np.loadtxt(path + "cell.dat",usecols=(3,4,5,6),unpack=True)
pid = 2067852

Nr = 1
Nc = 2
cm = plt.cm.get_cmap('rainbow')
vmax = 0
vmin = -2
bpos = [(0.75 - 1.3**(-4)), (0.75 - 1.3**(-3)), (0.75 - 1.3**(-2)), (0.75 - 1.3**(-1))]
images = []

fig, axs = plt.subplots(Nr,Nc,figsize = (12.5,6))

axs[0].scatter(data_sl.g['x'], data_sl.g['y'], c = np.log10(np.fabs(data_sl.g['radFlux'])), s = 1, marker = '.', cmap = cm, vmin=vmin, vmax=vmax)

for xmi, xma, ymi, yma in zip(xmin, xmax, ymin, ymax):
    axs[0].plot([xmi,xmi],[ymi,yma],c='k')
    axs[0].plot([xma,xma],[ymi,yma],c='k')
    axs[0].plot([xmi,xma],[ymi,ymi],c='k')
    axs[0].plot([xmi,xma],[yma,yma],c='k')

axs[0].plot([-0.49,data.g['x'][pid]],[bpos[0],data.g['y'][pid]],c='r')

axs[0].scatter(data.s['x'], data.s['y'], c = 'k', marker = '*', s=100, zorder = 1000000)

circles = [0]*len(bpos)
for i in range(len(bpos)):
	circles[i] = plt.Circle((0, bpos[i]), 0.05, color='black', fill=False, alpha=0.5)
for circle in circles:
	axs[0].add_artist(circle)

axs[0].set_xlim(-0.5,0.5)
axs[0].set_ylim(-0.5,0.5)
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')

axs[1].scatter(data_sl.g['x'], data_sl.g['y'], c = np.log10(np.fabs(data_sl.g['radFlux'])), s = 10, marker = '.', cmap = cm, vmin=vmin, vmax=vmax)

for xmi, xma, ymi, yma in zip(xmin, xmax, ymin, ymax):
    axs[1].plot([xmi,xmi],[ymi,yma],c='k')
    axs[1].plot([xma,xma],[ymi,yma],c='k')
    axs[1].plot([xmi,xma],[ymi,ymi],c='k')
    axs[1].plot([xmi,xma],[yma,yma],c='k')

axs[0].plot([-0.49,data.g['x'][pid]],[bpos[0],data.g['y'][pid]],c='r')

circles = [0]*len(bpos)
for i in range(len(bpos)):
	circles[i] = plt.Circle((0, bpos[i]), 0.05, color='black', fill=False, alpha=0.5)
for circle in circles:
	axs[1].add_artist(circle)

axs[1].plot([-0.49,data.g['x'][pid]],[bpos[0],data.g['y'][pid]],c='r')

axs[1].set_xlim(-0.075,0.075)
axs[1].set_ylim(bpos[2]-0.075,bpos[2]+0.075)
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')

plt.tight_layout()
plt.savefig("cellplot.pdf")
plt.savefig("cellplot.png")
#plt.show()
plt.close()
