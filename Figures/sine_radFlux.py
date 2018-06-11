import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
import pynbody as pyn

s = pyn.load("/home/grondjj/Data/RadTransfer/SineTest/ScalingPlot/SineTest_pDens/128^3/sine_128^3.00001")
qty = "radFlux"
#qty = "rho"
pyn.plot.sph.image(s.g,qty=qty,width=.95,cmap="magma",log=True)
plt.xlabel('x')
plt.ylabel('y')

ax=plt.gca()
im=ax.images
cb=im[-1].colorbar
cb.remove()
plt.draw()

plt.clim(1e5,1e6)
cbar = plt.colorbar()
cbar.set_ticks([1e5,2e5,3e5,4e5,5e5,6e5,7e5,8e5,9e5,1e6])
cbar.set_ticklabels(["$10^5$",'','','','','','','','',"$10^6$"])
cbar.set_label(r"flux [code units]")

plt.tight_layout()
plt.savefig("sine_radFlux.pdf")
plt.savefig("sine_radFlux.png")
#plt.show()
plt.close()
