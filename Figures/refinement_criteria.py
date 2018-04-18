import pynbody as pyn
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

path = "/home/grondjj/Data/RadTransfer/SineTest/RefinementCriteria/"
af = np.array(pyn.load(path+"1e-08/sine_064^3.00001").g["radFlux"])

folders = glob(path + "[0-9]*[.e]*[0-9]/")
N = 64**3

cells = []
taus = []
rmse = []



for f in folders:
	nf = np.array(pyn.load(f+"sine_064^3.00001").g["radFlux"])
	rmse.append(np.sqrt(np.sum(((nf - af)/af)**2)/len(af)))
	taus.append(float(f.split('/')[-2]))
	switch = 0
	with open(f+"/output.txt", 'r') as f:
		for line in f:
			if line[:7] == "nActive":
				if switch == 0:
					cells.append(int(line.split(',')[-2].split(' ')[-1]))
					switch += 1

rmse = np.array(rmse)
cells = np.array(cells)
taus = np.array(taus)

f, axarr = plt.subplots(2, sharex=True, figsize = (6.3,8.9))
axarr[0].scatter(taus, cells/N)
axarr[0].set_xlim(1e-9,1e4)
axarr[0].set_ylim(600,2200)
axarr[0].set_xscale('log')
axarr[0].set_ylabel(r"$N_{\rm cells}/N$")
axarr[1].scatter(taus, rmse)
axarr[1].plot([1e-8, 1e4],[1e-8/10, 1e4/10], c = 'k', alpha = 0.45, label = "$y=x/10$")
axarr[1].set_ylim(1e-9,1e-1)
axarr[1].set_xlim(1e-9,1e4)
axarr[1].set_xscale('log')
axarr[1].set_yscale('log')
axarr[1].minorticks_off()
axarr[1].set_ylabel(r"${\rm RMS}\left[\left(F_{\tau_{\rm ref}} - F_{10^{-8}}\right)/F_{10^{-8}}\right]$")
axarr[1].set_xlabel(r"$\tau_{\rm ref}$")
axarr[1].legend(loc = 'upper left')
plt.tight_layout()
plt.savefig("refinement_criteria.png")
plt.savefig("refinement_criteria.pdf")
#plt.show()
plt.close()
