import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
import pynbody as pyn

s = pyn.load("/home/grondjj/Data/RadTransfer/SineTest/ScalingPlot/SineTest_pDens/128^3/sine_128^3.00001")
qty = "rho"
pyn.plot.sph.image(s.g,qty=qty,width=.95,cmap="magma",log=True)
plt.xlabel('x')
plt.ylabel('y')

ax=plt.gca()
im=ax.images
cb=im[-1].colorbar
cb.remove()
plt.draw()

plt.clim(np.min(s.g[qty]),np.max(s.g[qty]))
cbar = plt.colorbar()
cbar.set_ticklabels([-3,-2,-1,0,1])
cbar.set_label(r"density [code units]")

plt.tight_layout()
plt.savefig("sine_rho.pdf")
plt.savefig("sine_rho.png")
#plt.show()
plt.close()
