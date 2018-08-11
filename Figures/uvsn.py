import numpy as np
import matplotlib.pyplot as plt
import os

path = "/home/grondjj/Data/Starburst99/Paper/Chabrier/output/"

# load in my spectrum
spec = np.loadtxt(path+"Chabrier.spectrum1", skiprows = 6)

#constants
c = 2.99792458e8
h = 6.62606957e-34
hErg = 6.62606957e-27
eV2J = 1.60217657e-19
m2A = 1e10
A2m = 1e-10
# bands of interest
Band = ['Total','FUV', 'EUV'] # Filter Names
LS = ['-', '-.', '--']
BandW = [(91, 1600000), (1000,2000), (100,1000)] #filter bnds, Angstrom 1e-10m 

for i in range(len(Band)):
     # open output file & write header
    f = open('./'+Band[i]+'.dat','w')
    f.write('t [yrs]         L [Ergs s^-1]\n')

    # slice up data into bands
    band = spec[(spec[:,1]<=BandW[i][1])&(spec[:,1]>=BandW[i][0])]
    
    # slice up into time steps
    tSeg = band[:,0].searchsorted(np.unique(band[:,0]))
    
    # array of *Logged* times
    t = band[:,0][tSeg]
    
    # array of integration limits
    lim = np.append(tSeg,len(band[:,0]))
    
    # array to be populated with integrals
    intErg = np.zeros(len(lim)-1)
    
    # unlog dL/dW data
    band[:,2] = 10**band[:,2]
    for j in range(1,len(lim)):
            intErg[j-1] = np.trapz(band[lim[j-1]:lim[j],2], \
            band[lim[j-1]:lim[j],1])
    
    # log integrated luminosities
    intErg = np.log10(intErg)
    for j in range(len(t)):
        f.write("%14.11f\t%02.11f\n" % (t[j], intErg[j]))
    f.close()

for i,j in zip(Band, LS):
    data = np.loadtxt(i+'.dat',skiprows = 1)
    dataTot = np.trapz(10**data[:,1], data[:,0]*365*24*60*60)
    plt.loglog(data[:,0], 10**data[:,1], label = i + ', ' + '$E=' + \
               str(dataTot)[0:4]+r"\times 10^{"+str(dataTot)[-2:] + \
               r"}{\rm \frac{erg}{M_\odot}}$", ls = j)

sn = np.loadtxt(path+'Chabrier.snr1', skiprows = 7)
snTot = np.trapz(10**sn[:,2], sn[:,0]*365*24*60*60)
plt.loglog(sn[:,0], 10**sn[:,2], label = r"SNe, " + '$E=' + str(snTot)[0:4] + \
           r"\times 10^{"+str(snTot)[-2:] + \
           r"}{\rm \frac{erg}{M_\odot}}$", ls = ':') 

wind = np.loadtxt(path+'Chabrier.power1', skiprows = 7)
windTot = np.trapz(10**wind[:,1], wind[:,0]*365*24*60*60)
plt.loglog(wind[:,0], 10**wind[:,1], label = r"Winds, " + "$E="+ \
           str(windTot)[0:4]+r"\times 10^{"+str(windTot)[-2:]+ \
           r"}{\rm \frac{erg}{M_\odot}}$", ls = '-')

plt.xlabel(r"age $[\rm yrs]$")
plt.ylabel(r"Luminosity $[\rm erg/ s /{M_\odot}]$")
plt.xlim(1e5,1e10)
plt.ylim(1e30,1e38)
plt.legend(loc = 'upper right', frameon = 0, fontsize = 11)
plt.tight_layout()
plt.savefig('./uvsn.pdf')
#plt.savefig('./uvsn.png', dpi = 300)
#plt.show()
plt.close()

for i in Band:
    os.system('rm -f ' + i +'.dat' )
