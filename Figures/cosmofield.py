import numpy as np
import pynbody as pyn
import matplotlib.pyplot as plt

s = pyn.load("/home/grondjj//Data/RadTransfer/Cosmo_Field/background.00001")
s.physical_units()

def F_r(r, R):
    L = 4*np.pi*R**2
    F = np.zeros(len(r))
    for i in range(len(r)):
        if r[i] == R:
            F[i] = F[i-1];
        else:
            F[i] = L / (8 * np.pi * R * r[i]) * np.log(np.fabs((R + r[i]) 
                / (R - r[i])))
    return F

fig = plt.figure()
ax1 = fig.add_subplot(111)
r = np.linspace(0.0001,1,10000)
flux = F_r(r, 0.5)
rSim = s.g['r']
fluxSim = s.g['radFlux']
plt.scatter(rSim,fluxSim, label = 'simulation', c = '#ff7f0e', rasterized = True)
plt.plot(r, flux, label = 'solution', c = 'k')
plt.plot([0.5,0.5], [1e-1,1e2], linestyle = ':', label = r'$\frac{1}{2}$box-width', c = 'k')
plt.plot([0.5,0.5], [3.5e0,1e2], c = 'k')
plt.plot([0,1], [1,1], linestyle = '--', label = 'central flux = 1', c = 'k')
ax1.set_xlabel("radius from box centre")
ax1.set_ylabel("flux (code units)")
ax1.legend(loc = 'upper right')
ax1.set_xlim(0,1)
ax1.set_ylim(1e-1,1e2)
ax1.set_yscale('log')
plt.tight_layout()
plt.savefig('cosmofield.pdf')
plt.savefig('cosmofield.png')
#plt.show()
plt.close()
