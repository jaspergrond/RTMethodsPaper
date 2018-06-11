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

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax2.scatter(taus, rmse, c = "C3", marker = "o")
ax2.plot([1e-8, 1e4],[1e-8/10, 1e4/10], c = 'C3') 
ax1.set_xlabel(r"$\tau_{\rm refine}$")
ax1.set_xscale('log')
ax1.set_xlim(1e-9,1e4)
ax2.set_ylabel(r"${\rm RMS}\left[\left(F_{\tau_{\rm ref}} - F_{10^{-8}}\right)/F_{10^{-8}}\right]$", color = 'C3')
ax2.tick_params('y', colors = 'C3')
ax2.set_yscale('log')
ax2.set_ylim(1e-9,1e-1)
ax1.scatter(taus, cells/N, c = "C0", marker = "s")
ax1.set_ylabel(r"$N_{\rm seg}/N$", color = 'C0')
ax1.tick_params('y', colors = 'C0')
ax1.set_ylim(600,2200)
ax2.text(1e-7, 1e-5, r"${\rm RMS} = \tau_{\rm refine}/10$", rotation = 55, fontsize = 15, color = 'C3')
plt.tight_layout()
plt.savefig("refinement_criteria.pdf")
plt.savefig("refinement_criteria.png")
#plt.show()
plt.close()
