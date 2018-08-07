import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from glob import glob
from scipy.optimize import curve_fit

testFolder = [
              "SineTest_fuRef",
              "SineTest_bSize",
              "SineTest_pDens",
              "SineTest_bSize_0.1",
              "SineTest_pDens_0.1",
              "SineTest_noRef"
             ]

testName = [
            r"full refinement",
            r"const. density, $\tau_{\rm ref}=0.01$",
            r"const. box size, $\tau_{\rm ref}=0.01$",
            r"const. density, $\tau_{\rm ref}=0.1$",
            r"const. box size, $\tau_{\rm ref}=0.1$",
            r"no refinement"
           ]

testColor = [
             "#d62728",
             "#1f77b4",
             "#1f77b4",
             "#ff7f0e",
             "#ff7f0e",
             "#2ca02c"
            ]

testMarker = [
              "o",
              "D",
              "x",
              "D",
              "x",
              "s"
             ]

path = "/home/grondjj/Data/RadTransfer/SineTest/ScalingPlot/"

for tF, tN, tC, tM in zip(testFolder, testName, testColor, testMarker):
    folders = sorted(glob(path+tF+"/[0-9][0-9][0-9]^3"))
    particles = []
    rays = []
    cells = []

    for folder in folders:
        switch = 0
        with open(folder+"/output.txt", 'r') as f:
            for line in f:
                if line[:7] == "nActive":
                    if switch == 0:
                        cells.append(int(line.split(',')[-2].split(' ')[-1]))
                        rays.append(int(line.split(',')[-1].split(' ')[-1]))
                        particles.append(int(folder.split('^')[0].split('/')[-1]))
                        switch += 1
                        

    rays = np.array(rays)
    cells = np.array(cells)
    particles = np.array(particles)**3
   

    if tN == "full refinement":
        def NlogNlogN(particles, C):
            return C*particles*(2./5.*particles)**(1./3.)

        popt, pcov = curve_fit(NlogNlogN, particles, cells, p0 = [10])
        cells_fit = NlogNlogN(particles, popt[0]) 
        plt.plot(np.cbrt(particles), cells_fit/particles, c = tC, linestyle = '-')
 
    if tN == "no refinement":
        def NlogNlogN(particles, C):
            return C*particles*np.log2(2*particles*64./5.)*np.log2(2*particles*64./5.)

        popt, pcov = curve_fit(NlogNlogN, particles, cells, p0 = [10])
        cells_fit = NlogNlogN(particles, popt[0]) 
        plt.plot(np.cbrt(particles), cells_fit/particles, c = tC, linestyle = '-.')

    plt.scatter(np.cbrt(particles), cells/particles, c = tC, marker = tM, s = 50)


h = [
	mlines.Line2D([], [], color='#d62728', label=r"$CN (2N/N_B)^{1/3} \sim O(N^{4/3})$")
	,mlines.Line2D([], [], color='#2ca02c', label=r"$CN\log^2\left(128N/N_B\right) \sim O(N\log^2N)$", linestyle ='-.')
	,mlines.Line2D([], [], color='#d62728', marker='o', label="full refinement", linewidth = 0)
	,mlines.Line2D([], [], color='#2ca02c', marker='s', label=r"no refinement", linewidth = 0)
	,mlines.Line2D([], [], color='k', marker='D', label=r"constant particle density", linewidth = 0)
	,mlines.Line2D([], [], color='k', marker='x', label=r"constant box size", linewidth = 0)
	,mpatches.Patch(color='#1f77b4', label=r"$\tau_{\rm ref} = 0.01$")
	,mpatches.Patch(color='#ff7f0e', label=r"$\tau_{\rm ref} = 0.1$")
]

#plt.plot(np.cbrt(particles), np.cbrt(particles)**(7./3.), c='k', alpha=0.5)
plt.xticks(np.cbrt(particles), fontsize = 12)
plt.yticks(fontsize = 12)
plt.xlabel(r"$N_{\rm 1D}$",fontsize = 22)
plt.ylabel(r"$N_{\rm seg}/N$",fontsize = 22)
plt.legend(loc="upper left", fontsize = 13, frameon=False, handles = h)
plt.xlim(32-5,128+5)
plt.ylim(0,4250)
plt.tight_layout()
#plt.savefig("particle_scaling.png")
plt.savefig("particle_scaling.pdf")
#plt.show()
plt.close()
