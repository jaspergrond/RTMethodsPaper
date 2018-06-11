import numpy as np
import pynbody as pyn
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator
from glob import glob

path = "/home/grondjj/Data/RadTransfer/Isothemal_Spheres/"
folders = glob(path + "Test/[0-9]*[.e]*[0-9]/")
iCut = np.load(path + "Soln/inShadowsAndBalls.npy")
af = np.array(pyn.load(path+"Test/1e-08/balls.00001").g["radFlux"])
af_cut = np.array(pyn.load(path+"Test/1e-08/balls.00001").g["radFlux"])[iCut]
N = len(af)

cells = []
taus = []
rmse = []
rmse_cut = []

for f in folders:
	nf = np.array(pyn.load(f+"balls.00001").g["radFlux"])
	nf_cut = np.array(pyn.load(f+"balls.00001").g["radFlux"])[iCut]
	rmse.append(np.sqrt(np.sum(((nf - af)/af)**2)/len(af)))
	rmse_cut.append(np.sqrt(np.sum(((nf_cut - af_cut)/af_cut)**2)/len(af_cut)))
	taus.append(float(f.split('/')[-2]))
	switch = 0
	with open(f+"/output.txt", 'r') as f:
		for line in f:
			if line[:7] == "nActive":
				if switch == 0:
					cells.append(int(line.split(',')[-2].split(' ')[-1]))
					switch += 1

cells = np.array(cells)
taus = np.array(taus)
rmse = np.array(rmse)
rmse_cut = np.array(rmse_cut)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax2.scatter(taus, rmse, c = "C3", marker = "o", label = "all particles")
ax2.scatter(taus, rmse_cut, c = "C3", marker = "s", label = "in shadow")
ax2.plot([1e-9, 1e4],[1e-8/10, 1e4/10], c = 'C3') 
ax1.set_xlabel(r"$\tau_{\rm refine}$")
ax1.set_xscale('log')
ax1.set_xlim(1e-9,1e4)
ax2.set_ylabel(r"${\rm RMS}\left[\left(F_{\tau_{\rm ref}} - F_{10^{-8}}\right)/F_{10^{-8}}\right]$", color = 'C3')
ax2.tick_params('y', colors = 'C3')
ax2.set_yscale('log')
ax2.set_ylim(1e-8,1e1)
ax1.scatter(taus, cells/N, c = "C0", marker = "s")
ax1.set_ylabel(r"$N_{\rm seg}/N$", color = 'C0')
ax1.tick_params('y', colors = 'C0')
ax1.set_ylim(0,120)
ax2.text(3e-9, 5e-6, r"${\rm RMS} = \tau_{\rm refine}/10$", rotation = 48, fontsize = 15, color = 'C3')
ax2.set_yticks([1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2,1e-1,1e0,1e1])
ax2.minorticks_off()
ax2.legend(loc = (0.6,0.13))
plt.tight_layout()
plt.savefig('isothermal_spheres.pdf')
plt.savefig('isothermal_spheres.png')
#plt.show()
plt.close()
