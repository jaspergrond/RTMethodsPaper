import pynbody as pyn
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

path = "/home/grondjj/Data/RadTransfer/SineTest/OpeningAngle/"
folders = glob(path+"[0-9].[0-9]")
N = 64**3
rays = []
cells = []
theta = []
rmse = []

t0f = np.array(pyn.load(path+"0.0/sine_064^3.00001").g['radFlux'])

for folder in folders:
	theta.append(float(folder.split('/')[-1]))
	tf = np.array(pyn.load(folder + "/sine_064^3.00001").g['radFlux'])
	rmse.append(np.sqrt(np.sum(((tf - t0f)/t0f)**2)/len(tf)))
	switch = 0
	with open(folder+"/output.txt", 'r') as f:
		for line in f:
			if line[:7] == "nActive":
				if switch == 0:
					cells.append(int(line.split(',')[-2].split(' ')[-1]))
					rays.append(int(line.split(',')[-1].split(' ')[-1]))
					switch += 1

theta = np.array(theta)
rmse = np.array(rmse)
rays = np.array(rays)
cells = np.array(cells)

f, axarr = plt.subplots(2, sharex=True, figsize = (6.3,8.9))
axarr[0].scatter(theta, rays/N)
axarr[0].plot([-0.1,1.1],[N,N],c='k',linestyle='-.', label = r"$N_{\rm source}$")
axarr[0].set_ylim(1e1,1e6)
axarr[0].set_xlim(-0.1,1.1)
axarr[0].set_yscale('log')
axarr[0].legend(loc = 'lower left')
axarr[0].set_ylabel(r"$N_{\rm rays}/N_{\rm sink}$")
axarr[1].scatter(theta, rmse)
axarr[1].set_ylim(1e-4,1e-1)
axarr[1].set_xlim(0,1.1)
axarr[1].set_yscale('log')
#axarr[1].set_xscale('log')
axarr[1].set_ylabel(r"${\rm RMS}\left[\left(F_{\theta_{\rm open}} - F_{0}\right)/F_{0}\right]$")
axarr[1].set_xlabel(r"$\theta_{\rm open}$")

#plt.scatter(rmse, rays/N)
#plt.xscale("log")
#plt.yscale("log")
#plt.xlabel(r"${\rm RMS}\left[\left(F_{\theta} - F_{0}\right)/F_{0}\right]$")
#plt.ylabel(r"$N_{\rm rays}/N_{\rm sink}$")
#plt.xlim(1e-4,8e-2)
#plt.ylim(5e1,4e4)
#for t, e, c in zip(theta, rmse, rays/N):
#	plt.text(e*1.15,c*0.92,str(t))
plt.tight_layout()
plt.savefig("opening_angle.png")
plt.savefig("opening_angle.pdf")
plt.show()
plt.close()
