import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
import pynbody as pyn
from scipy.interpolate import griddata

s = pyn.load("/home/grondjj/Data/RadTransfer/SineTest/ScalingPlot/SineTest_pDens/128^3/sine_128^3.00001")
s_sl = s[np.fabs(s.g['z']) < s.g['smooth']]

vmin=np.log10(np.min(s_sl.g['rho']))
vmax=np.log10(np.max(s_sl.g['rho']))

x = np.array(s_sl.g['x'])
y = np.array(s_sl.g['y'])
z = np.array(np.log10(s_sl.g['rho']))

xgrid = np.linspace(np.min(x), np.max(x), 1600)
ygrid = np.linspace(np.min(y), np.max(y), 1600)
xgrid, ygrid = np.meshgrid(xgrid, ygrid)
zgrid = griddata((x,y),z, (xgrid, ygrid), method='nearest')

plt.imshow(zgrid, cmap='magma',aspect='equal',interpolation='nearest',vmin=vmin, vmax=vmax,extent=(x.min(), x.max(), x.min(), x.max()))
plt.xlim(-0.46,0.46)
plt.ylim(-0.46,0.46)
plt.xlabel('x')
plt.ylabel('y')

plt.colorbar(label = r"$\log$(density)")
plt.tight_layout()
plt.savefig("sine_rho.pdf")
plt.savefig("sine_rho.png")
plt.show()
plt.close()
