import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import pynbody as pyn

acro = "TREVR"

path = "/home/grondjj/Data/RadTransfer/Stromgren/"

i064_path = path + 'runs/bigboys/strom064_iso/'
i128_path = path + 'runs/bigboys/strom128_iso/'
i256_path = path + 'runs/bigboys/strom256_iso/'

i064_030 = pyn.load(i064_path + 'strom64_iso.00060')
i128_030 = pyn.load(i128_path + 'strom128_iso.00060')
i256_030 = pyn.load(i256_path + 'strom256_iso.00060')
i064_500 = pyn.load(i064_path + 'strom64_iso.01000')
i128_500 = pyn.load(i128_path + 'strom128_iso.01000')
i256_500 = pyn.load(i256_path + 'strom256_iso.01000')

f, (ax1, ax2) = plt.subplots(1,2, sharey=True, figsize = (13,6.3))

f_500 = glob(path+"ISO_500/*.csv")
f_500_ = glob(path+"ISO_500_1-x/*.csv")
f_030 = glob(path+"ISO_030/*.csv")
f_030_ = glob(path+"ISO_030_1-x/*.csv")

colors = {
			 "C_2-Ray"  :  "#ff2828",
			 "OTVET"    :  "#3939ff",
			 "CRASH"    :  "#22ff22",
			 "RSPH"     :  "#434343",
			 "ART"      :  "#1effff",
			 "FTTE"     :  "#ff41ff",
			 "SimpleX"  :  "#733d1a",
			 "Zeus-MP"  :  "#7ad37a",
			 "FLASH-HC" :  "#ff9f9f",
			 "IFT"      :  "#14a1cf" 
		 }

lines = {
			 "C_2-Ray"  :  "-",
			 "OTVET"    :  "--",
			 "CRASH"    :  "--",
			 "RSPH"     :  ":",
			 "ART"      :  "-.",
			 "FTTE"     :  "-.",
			 "SimpleX"  :  "-.",
			 "Zeus-MP"  :  ":",
			 "FLASH-HC" :  "--",
			 "IFT"      :  "-." 
		 }

labels = {
			 "C_2-Ray"  :  "C$^2$-Ray" ,
			 "OTVET"    :  "OTVET"   ,
			 "CRASH"    :  "CRASH"   ,
			 "RSPH"     :  "RSPH"    ,
			 "ART"      :  "ART"     ,
			 "FTTE"     :  "FTTE"    ,
			 "SimpleX"  :  "SimpleX" ,
			 "Zeus-MP"  :  "Zeus-MP" ,
			 "FLASH-HC" :  "FLASH-HC",
			 "IFT"      :  "IFT"     , 
		 }

a = 0.5

for i,j in zip(f_030, f_030_):
	x, y = np.loadtxt(i, unpack = True)
	x_, y_ = np.loadtxt(j, unpack = True, delimiter=',')	
	name = i.split('/')[-1].split('.')[0]
	ax1.plot(x,y, alpha=a, c = colors[name],linestyle = lines[name])
	ax1.plot(x_,y_, alpha=a, c = colors[name],linestyle = lines[name])


for i,j in zip(f_500, f_500_):
	x, y = np.loadtxt(i, unpack = True)
	x_, y_ = np.loadtxt(j, unpack = True, delimiter=',')
	name = j.split('/')[-1].split('.')[0]
	ax2.plot(x,y,alpha=a, c = colors[name],linestyle = lines[name], label = labels[name])
	ax2.plot(x_,y_,alpha=a, c = colors[name],linestyle = lines[name])

nbins = 100
L = 6.6

HI_064, bins_064 = np.histogram(i064_030.g['r'], weights = i064_030.g['HI'],
    bins = nbins)
counts_064, bins_064 = np.histogram(i064_030.g['r'], bins = nbins)
bins_064 = (bins_064[:-1]+bins_064[1:])/2
HI_064 /= counts_064
HII_064 = 1-HI_064

HI_128, bins_128 = np.histogram(i128_030.g['r'], weights = i128_030.g['HI'],
    bins = nbins)
counts_128, bins_128 = np.histogram(i128_030.g['r'], bins = nbins)
bins_128 = (bins_128[:-1]+bins_128[1:])/2
HI_128 /= counts_128
HII_128 = 1-HI_128

HI_256, bins_256 = np.histogram(i256_030.g['r'], weights = i256_030.g['HI'],
    bins = nbins)
counts_256, bins_256 = np.histogram(i256_030.g['r'], bins = nbins)
bins_256 = (bins_256[:-1]+bins_256[1:])/2
HI_256 /= counts_256
HII_256 = 1-HI_256


ax1.plot(bins_064/L, HI_064, c='k', ls='-.') 
ax1.plot(bins_128/L, HI_128, c='k', ls='--')
ax1.plot(bins_256/L, HI_256, c='k', ls='-')
ax1.plot(bins_064/L, 1-HI_064, c='k', ls='-.') 
ax1.plot(bins_128/L, 1-HI_128, c='k', ls='--')
ax1.plot(bins_256/L, 1-HI_256, c='k', ls='-')

HI_064, bins_064 = np.histogram(i064_500.g['r'], weights = i064_500.g['HI'],
    bins = nbins)
counts_064, bins_064 = np.histogram(i064_500.g['r'], bins = nbins)
bins_064 = (bins_064[:-1]+bins_064[1:])/2
HI_064 /= counts_064
HII_064 = 1-HI_064

HI_128, bins_128 = np.histogram(i128_500.g['r'], weights = i128_500.g['HI'],
    bins = nbins)
counts_128, bins_128 = np.histogram(i128_500.g['r'], bins = nbins)
bins_128 = (bins_128[:-1]+bins_128[1:])/2
HI_128 /= counts_128
HII_128 = 1-HI_128

HI_256, bins_256 = np.histogram(i256_500.g['r'], weights = i256_500.g['HI'],
    bins = nbins)
counts_256, bins_256 = np.histogram(i256_500.g['r'], bins = nbins)
bins_256 = (bins_256[:-1]+bins_256[1:])/2
HI_256 /= counts_256
HII_256 = 1-HI_256

ax2.plot(bins_064/L, HI_064, c='k', ls='-.', label = acro + " $64^3$")
ax2.plot(bins_128/L, HI_128, c='k', ls='--', label = acro + " $128^3$")
ax2.plot(bins_256/L, HI_256, c='k', ls='-', label = acro + " $256^3$")
ax2.plot(bins_064/L, 1-HI_064, c='k', ls='-.')
ax2.plot(bins_128/L, 1-HI_128, c='k', ls='--')
ax2.plot(bins_256/L, 1-HI_256, c='k', ls='-')

rs = 5.38
trecomb = 125
r030 = rs*(1 - np.exp(-30./trecomb))**(1/3.)/L
r500 = rs*(1 - np.exp(-500./trecomb))**(1/3.)/L
ax1.text(r030+0.02,2, "$R_S$", color = 'r', fontsize = 20)
ax2.text(r500+0.02,2, "$R_S$", color = 'r', fontsize = 20)
ax1.plot( [r030,r030], [1e-5,1e1], linestyle = ":", c = 'r')
ax2.plot( [r500,r500], [1e-5,1e1], linestyle = ":", c = 'r')

ax1.text(0.83,5,"030 Myr", fontsize = 20)
ax2.text(0.83,5,"500 Myr", fontsize = 20)

ax1.set_xlim(0,1.0)
ax2.set_xlim(0,1.0)
ax1.set_ylim(1e-5,1e1)
ax1.set_yscale("log")
ax1.set_xlabel(r"$r/R_{\rm box}$")
ax2.set_xlabel(r"$r/R_{\rm box}$")
ax1.set_ylabel("x, 1-x")
ax2.legend(loc = "lower center", fontsize = 13, ncol = 2)
plt.tight_layout()
#plt.savefig("strom_iso_fraction.png")
plt.savefig("strom_iso_fraction.pdf")
#plt.show()
plt.close()
