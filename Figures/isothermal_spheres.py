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
f, axarr = plt.subplots(2, sharex=True, figsize = (6.3,8.9))
axarr[0].scatter(taus, cells/N)
axarr[0].set_xlim(1e-9,1e4)
axarr[0].set_ylim(0,120)
axarr[0].set_xscale('log')
axarr[0].set_ylabel(r"$N_{\rm cells}/N$")
axarr[1].scatter(taus, rmse, label = "all particles")
axarr[1].scatter(taus, rmse_cut, label = "excluding background")
axarr[1].plot([1e-8, 1e4],[1e-8, 1e4], c = 'k', alpha = 0.45, label = "$y=x$")
axarr[1].set_ylim(1e-8,1e1)
axarr[1].set_xlim(1e-9,1e4)
axarr[1].set_xscale('log')
axarr[1].set_yscale('log')
axarr[1].set_yticks([1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2,1e-1,1e0,1e1])
axarr[1].minorticks_off()
axarr[1].set_ylabel(r"${\rm RMS}\left[\left(F_{\tau_{\rm ref}} - F_{10^{-8}}\right)/F_{10^{-8}}\right]$")
axarr[1].set_xlabel(r"$\tau_{\rm ref}$")
axarr[1].legend(loc = 'upper left')
plt.tight_layout()
plt.savefig('isothermal_spheres.pdf')
plt.savefig('isothermal_spheres.png')
#plt.show()
plt.close()
