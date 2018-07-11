import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import pynbody as pyn

acro = "TREVR"

path = "/home/grondjj/Data/RadTransfer/Stromgren/"

i064_path = path+'runs/bigboys/strom064/'
i128_path = path+'runs/bigboys/strom128/'
i256_path = path+'runs/bigboys/strom256/'

i064_010 = pyn.load(i064_path + 'strom64.00020')
i128_010 = pyn.load(i128_path + 'strom128.00020')
i256_010 = pyn.load(i256_path + 'strom256.00020')
i064_100 = pyn.load(i064_path + 'strom64.00200')
i128_100 = pyn.load(i128_path + 'strom128.00200')
i256_100 = pyn.load(i256_path + 'strom256.00200')
i064_500 = pyn.load(i064_path + 'strom64.01000')
i128_500 = pyn.load(i128_path + 'strom128.01000')
i256_500 = pyn.load(i256_path + 'strom256.01000')

f, (ax1, ax2, ax3) = plt.subplots(1,3, sharey=True, figsize = (13+6.5,6.3))

f_010 = glob(path+"010/*.csv")
f_010_ = glob(path+"010_1-x/*.csv")
f_100 = glob(path+"100/*.csv")
f_100_ = glob(path+"100_1-x/*.csv")
f_500 = glob(path+"500/*.csv")
f_500_ = glob(path+"500_1-x/*.csv")

colors = {
			 "C_2-Ray"  :  "#ff2828",
			 "OTVET"    :  "#3939ff",
			 "CRASH"    :  "#22ff22",
			 "RSPH"     :  "#434343",
			 "ART"      :  "#1effff",
			 "FTTE"     :  "#ff41ff",
			 "Zeus-MP"  :  "#7ad37a",
			 "IFT"      :  "#14a1cf" 
		 }

lines = {
			 "C_2-Ray"  :  "-",
			 "OTVET"    :  "--",
			 "CRASH"    :  "--",
			 "RSPH"     :  ":",
			 "ART"      :  "-.",
			 "FTTE"     :  "-.",
			 "Zeus-MP"  :  ":",
			 "IFT"      :  "-." 
		 }

labels = {
			 "C_2-Ray"  :  "C$^2$-Ray" ,
			 "OTVET"    :  "OTVET"   ,
			 "CRASH"    :  "CRASH"   ,
			 "RSPH"     :  "RSPH"    ,
			 "ART"      :  "ART"     ,
			 "FTTE"     :  "FTTE"    ,
			 "Zeus-MP"  :  "Zeus-MP" ,
			 "IFT"      :  "IFT"     , 
		 }


for i, j in zip(f_010, f_010_):
	x, y = np.loadtxt(i, unpack = True)
	x_, y_ = np.loadtxt(j, unpack = True, delimiter=',')
	name = i.split('/')[-1].split('.')[0]
	ax1.plot(x,y, alpha=0.7, c = colors[name],linestyle = lines[name])
	ax1.plot(x_,y_, alpha=0.7, c = colors[name],linestyle = lines[name])


for i, j in zip(f_100, f_100_):
	x, y = np.loadtxt(i, unpack = True)
	x_, y_ = np.loadtxt(j, unpack = True, delimiter=',')
	name = i.split('/')[-1].split('.')[0]
	ax2.plot(x,y,alpha=0.7, c = colors[name],linestyle = lines[name])
	ax2.plot(x_,y_,alpha=0.7, c = colors[name],linestyle = lines[name])


for i, j in zip(f_500, f_500_):
	x, y = np.loadtxt(i, unpack = True)
	x_, y_ = np.loadtxt(j, unpack = True, delimiter=',')
	name = i.split('/')[-1].split('.')[0]
	ax3.plot(x,y,alpha=0.7, c = colors[name],linestyle = lines[name], label = labels[name])
	ax3.plot(x_,y_,alpha=0.7, c = colors[name],linestyle = lines[name])

nbins = 100
L = 6.6

HI_064, bins_064 = np.histogram(i064_010.g['r'], weights = i064_010.g['HI'],
    bins = nbins)
counts_064, bins_064 = np.histogram(i064_010.g['r'], bins = nbins)
bins_064 = (bins_064[:-1]+bins_064[1:])/2
HI_064 /= counts_064

HI_128, bins_128 = np.histogram(i128_010.g['r'], weights = i128_010.g['HI'],
    bins = nbins)
counts_128, bins_128 = np.histogram(i128_010.g['r'], bins = nbins)
bins_128 = (bins_128[:-1]+bins_128[1:])/2
HI_128 /= counts_128

HI_256, bins_256 = np.histogram(i256_010.g['r'], weights = i256_010.g['HI'],
    bins = nbins)
counts_256, bins_256 = np.histogram(i256_010.g['r'], bins = nbins)
bins_256 = (bins_256[:-1]+bins_256[1:])/2
HI_256 /= counts_256

ax1.plot(bins_064/L, HI_064, c='k', ls='-.') 
ax1.plot(bins_128/L, HI_128, c='k', ls='--')
ax1.plot(bins_256/L, HI_256, c='k', ls='-')
ax1.plot(bins_064/L, 1-HI_064, c='k', ls='-.') 
ax1.plot(bins_128/L, 1-HI_128, c='k', ls='--')
ax1.plot(bins_256/L, 1-HI_256, c='k', ls='-')

HI_064, bins_064 = np.histogram(i064_100.g['r'], weights = i064_100.g['HI'],
    bins = nbins)
counts_064, bins_064 = np.histogram(i064_500.g['r'], bins = nbins)
bins_064 = (bins_064[:-1]+bins_064[1:])/2
HI_064 /= counts_064

HI_128, bins_128 = np.histogram(i128_100.g['r'], weights = i128_100.g['HI'],
    bins = nbins)
counts_128, bins_128 = np.histogram(i128_100.g['r'], bins = nbins)
bins_128 = (bins_128[:-1]+bins_128[1:])/2
HI_128 /= counts_128

HI_256, bins_256 = np.histogram(i256_100.g['r'], weights = i256_100.g['HI'],
    bins = nbins)
counts_256, bins_256 = np.histogram(i256_100.g['r'], bins = nbins)
bins_256 = (bins_256[:-1]+bins_256[1:])/2
HI_256 /= counts_256

ax2.plot(bins_064/L, HI_064, c='k', ls='-.')
ax2.plot(bins_128/L, HI_128, c='k', ls='--')
ax2.plot(bins_256/L, HI_256, c='k', ls='-')
ax2.plot(bins_064/L, 1-HI_064, c='k', ls='-.')
ax2.plot(bins_128/L, 1-HI_128, c='k', ls='--')
ax2.plot(bins_256/L, 1-HI_256, c='k', ls='-')

HI_064, bins_064 = np.histogram(i064_500.g['r'], weights = i064_500.g['HI'],
    bins = nbins)
counts_064, bins_064 = np.histogram(i064_500.g['r'], bins = nbins)
bins_064 = (bins_064[:-1]+bins_064[1:])/2
HI_064 /= counts_064

HI_128, bins_128 = np.histogram(i128_500.g['r'], weights = i128_500.g['HI'],
    bins = nbins)
counts_128, bins_128 = np.histogram(i128_500.g['r'], bins = nbins)
bins_128 = (bins_128[:-1]+bins_128[1:])/2
HI_128 /= counts_128

HI_256, bins_256 = np.histogram(i256_500.g['r'], weights = i256_500.g['HI'],
    bins = nbins)
counts_256, bins_256 = np.histogram(i256_500.g['r'], bins = nbins)
bins_256 = (bins_256[:-1]+bins_256[1:])/2
HI_256 /= counts_256

ax3.plot(bins_064/L, HI_064, c='k', ls='-.', label = acro+' $64^3$')
ax3.plot(bins_128/L, HI_128, c='k', ls='--', label = acro+' $128^3$')
ax3.plot(bins_256/L, HI_256, c='k', ls='-', label = acro+' $256^3$')
ax3.plot(bins_064/L, 1-HI_064, c='k', ls='-.')
ax3.plot(bins_128/L, 1-HI_128, c='k', ls='--')
ax3.plot(bins_256/L, 1-HI_256, c='k', ls='-')

ax1.text(0.83,5,"010 Myr", fontsize = 20)
ax2.text(0.83,5,"100 Myr", fontsize = 20)
ax3.text(0.83,5,"500 Myr", fontsize = 20)

ax1.set_xlim(0,1.0)
ax2.set_xlim(0,1.0)
ax3.set_xlim(0,1.0)
ax1.set_ylim(1e-5,1e1)
ax1.set_yscale("log")
ax1.set_xlabel(r"$r/R_{\rm box}$")
ax2.set_xlabel(r"$r/R_{\rm box}$")
ax3.set_xlabel(r"$r/R_{\rm box}$")
ax1.set_ylabel("x, 1-x")
ax3.legend(loc = "lower center", fontsize=17, ncol = 2)
plt.tight_layout()
plt.savefig("strom_fraction.png")
plt.savefig("strom_fraction.pdf")
#plt.show()
plt.close()
