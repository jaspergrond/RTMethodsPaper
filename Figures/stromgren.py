import numpy as np
import pynbody as pyn
import matplotlib.pyplot as plt

i128_path = '/home/grondjj/Data/RadTransfer/Stromgren/strom128_iso/'
i064_path = '/home/grondjj/Data/RadTransfer/Stromgren/strom64_iso/'
n128_path = '/home/grondjj/Data/RadTransfer/Stromgren/strom128/'
n064_path = '/home/grondjj/Data/RadTransfer/Stromgren/strom64/'
ittt_path = '/home/grondjj/Data/RadTransfer/Stromgren/strom64_iso_1e4/'
nttt_path = '/home/grondjj/Data/RadTransfer/Stromgren/strom64_1e4/'

i128 = pyn.load(i128_path + 'strom128_iso.01000') 
i064 = pyn.load(i064_path + 'strom64_iso.01000')
n128 = pyn.load(n128_path + 'strom128.01000')
n064 = pyn.load(n064_path + 'strom64.01000')
ittt = pyn.load(ittt_path + 'strom64_iso.10000')
nttt = pyn.load(nttt_path + 'strom64.10000')


################ HI fraction isothermal ################

plt.ylim([1e-5,5])
plt.xlim([0,1.2])
plt.yscale("log")
plt.ylabel("Ionization Fraction")
plt.xlabel(r"Radius/L$_{\rm box}$")

nbins = 100

HI_064, bins_064 = np.histogram(i064.g['r'], weights = i064.g['HI'], 
    bins = nbins)
counts_064, bins_064 = np.histogram(i064.g['r'], bins = nbins)
bins_064 = (bins_064[:-1]+bins_064[1:])/2
HI_064 /= counts_064
HII_064 = 1-HI_064

HI_128, bins_128 = np.histogram(i128.g['r'], weights = i128.g['HI'], 
    bins = nbins)
counts_128, bins_128 = np.histogram(i128.g['r'], bins = nbins)
bins_128 = (bins_128[:-1]+bins_128[1:])/2
HI_128 /= counts_128
HII_128 = 1-HI_128


HI_ttt, bins_ttt = np.histogram(ittt.g['r'], weights = ittt.g['HI'], 
    bins = nbins)
counts_ttt, bins_ttt = np.histogram(ittt.g['r'], bins = nbins)
bins_ttt = (bins_ttt[:-1]+bins_ttt[1:])/2
HI_ttt /= counts_ttt
HII_ttt = 1-HI_ttt

plt.plot(bins_064/6.6, HI_064, c = '#1f77b4', ls = '-', label = 'FAHRT 64')
plt.plot(bins_064/6.6, HII_064, c = '#1f77b4', ls = '-')
plt.plot(bins_128/6.6, HI_128, c = '#1f77b4', ls = '-.', label = 'FAHRT 128')
plt.plot(bins_128/6.6, HII_128, c = '#1f77b4', ls = '-.')
plt.plot(bins_ttt/6.6, HI_ttt, c = '#1f77b4', ls = ':', label = 'FAHRT 10000 time steps')
plt.plot(bins_ttt/6.6, HII_ttt, c = '#1f77b4', ls = ':')

C2I = np.loadtxt("C2ray1.dat")
C2II = np.loadtxt("C2ray2.dat")
ZI = np.loadtxt("Zeus1.dat")
ZII = np.loadtxt("Zeus2.dat")

plt.plot(C2I[:,0], 10**C2I[:,1], c = '#ff7f0e', ls = '--', 
    label = r'$\rm C^2$ray')
plt.plot(C2II[:,0], 10**C2II[:,1], c = '#ff7f0e', ls = '--')
plt.plot(ZI[:,0], 10**ZI[:,1], c = '#2ca02c', ls = ':', label = 'ZEUS-2D')
plt.plot(ZII[:,0], 10**ZII[:,1], c = '#2ca02c', ls = ':')

plt.legend(loc=(0.075,0.03))
plt.savefig("stromHIiso.png")
plt.savefig("stromHIiso.pdf")
plt.show()
plt.close()


################ HI fraction non-isothermal ################

#files128 = [n128_path + "strom128.00020", n128_path + "strom128.00200",
#    n128_path  + "strom128.01000"]
#files064 = [n064_path + "strom64.00020", n064_path + "strom64.00200", 
#    n064_path + "strom64.01000"]
#
#nbins = 100
#
#
#colors=['#1f77b4','#ff7f0e','#2ca02c']
#plt.ylim([1e-5,5])
#plt.xlim([0,1.3])
#plt.yscale("log")
#plt.ylabel("HI Fraction")
#plt.xlabel(r"Radius/L$_{\rm box}$")
#plt.plot([0],[0], label = '10 Myrs',  c = colors[0])
#plt.plot([0],[0], label = '100 Myrs', c = colors[1])
#plt.plot([0],[0], label = '500 Myrs', c = colors[2])
#
#i = 0
#for file in sorted(files128):
#    n128 = pyn.load(file)
#    HI_128, bins_128 = np.histogram(n128.g['r'], weights = n128.g['HI'], 
#        bins = nbins)
#    counts_128, bins_128 = np.histogram(n128.g['r'], bins = nbins)
#    bins_128 = (bins_128[:-1]+bins_128[1:])/2
#    HI_128 /= counts_128
#    HII_128 = 1-HI_128
#    plt.plot(bins_128/6.6, HI_128, c = [i], ls = '-')
#    plt.plot(bins_128/6.6, HII_128, c = [i], ls = '-')
#    i+=1
#
#i = 0
#for file in sorted(files064):
#    n064 = pyn.load(file)
#    HI_064, bins_064 = np.histogram(n064.g['r'], weights = n064.g['HI'], 
#        bins = nbins)
#    counts_064, bins_064 = np.histogram(n064.g['r'], bins = nbins)
#    bins_064 = (bins_064[:-1]+bins_064[1:])/2
#    HI_064 /= counts_064
#    HII_064 = 1-HI_064
#    plt.plot(bins_064/6.6, HI_064, c = [i], ls = ':')
#    plt.plot(bins_064/6.6, HII_064, c = [i], ls = ':')
#    i+=1
#
#plt.legend(loc = "lower left")
##plt.savefig('stromthermHI.svg')
#plt.show()
#plt.close()
#
