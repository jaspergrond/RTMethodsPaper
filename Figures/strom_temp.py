import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import pynbody as pyn
from scipy import stats

acro = "TREVR"

path = "/home/grondjj/Data/RadTransfer/Stromgren/"

i128_path = '/home/grondjj/Data/RadTransfer/Stromgren/tau_0.01/strom128/'
i064_path = '/home/grondjj/Data/RadTransfer/Stromgren/tau_0.01/strom64/'

i128_010 = pyn.load(i128_path + 'strom128.00020')
i064_010 = pyn.load(i064_path + 'strom64.00020')
i128_100 = pyn.load(i128_path + 'strom128.00200')
i064_100 = pyn.load(i064_path + 'strom64.00200')
i128_500 = pyn.load(i128_path + 'strom128.01000')
i064_500 = pyn.load(i064_path + 'strom64.01000')

f, (ax1, ax2, ax3) = plt.subplots(1,3, sharey=True, figsize = (20,6.3))

f_500 = glob(path+"T_500/*.csv")
f_100 = glob(path+"T_100/*.csv")
f_010 = glob(path+"T_010/*.csv")

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

for i in f_010:
	x, y = np.loadtxt(i, unpack = True)
	name = i.split('/')[-1].split('.')[0]
	ax1.plot(x,y, alpha=0.7, c = colors[name],linestyle = lines[name])


for i in f_100:
	x, y = np.loadtxt(i, unpack = True)
	name = i.split('/')[-1].split('.')[0]
	ax2.plot(x,y,alpha=0.7, c = colors[name],linestyle = lines[name])


for i in f_500:
	x, y = np.loadtxt(i, unpack = True)
	name = i.split('/')[-1].split('.')[0]
	ax3.plot(x,y,alpha=0.7, c = colors[name],linestyle = lines[name], label = labels[name])

nbins = 100
L = 6.6

T_064, bins_064, binN = stats.binned_statistic(i064_010.g['r'], i064_010.g['temp'], 'mean', bins=nbins)
bins_064 = (bins_064[:-1]+bins_064[1:])/2

T_128, bins_128, binN = stats.binned_statistic(i128_010.g['r'], i128_010.g['temp'], 'mean', bins=nbins)
bins_128 = (bins_128[:-1]+bins_128[1:])/2

ax1.plot(bins_064/L, T_064, c='k', ls='-.') 
ax1.plot(bins_128/L, T_128, c='k', ls='-')

T_064, bins_064, binN = stats.binned_statistic(i064_100.g['r'], i064_100.g['temp'], 'mean', bins=nbins)
bins_064 = (bins_064[:-1]+bins_064[1:])/2

T_128, bins_128, binN = stats.binned_statistic(i128_100.g['r'], i128_100.g['temp'], 'mean', bins=nbins)
bins_128 = (bins_128[:-1]+bins_128[1:])/2

ax2.plot(bins_064/L, T_064, c='k', ls='-.') 
ax2.plot(bins_128/L, T_128, c='k', ls='-')


T_064, bins_064, binN = stats.binned_statistic(i064_500.g['r'], i064_500.g['temp'], 'mean', bins=nbins)
bins_064 = (bins_064[:-1]+bins_064[1:])/2

T_128, bins_128, binN = stats.binned_statistic(i128_500.g['r'], i128_500.g['temp'], 'mean', bins=nbins)
bins_128 = (bins_128[:-1]+bins_128[1:])/2

ax3.plot(bins_128/L, T_128, c='k', ls='-', label = acro)
ax3.plot(bins_064/L, T_064, c='k', ls='-.', label = acro + ' $32^3$') 

ax1.text(0.83,3.44e4,"010 Myr", fontsize = 20)
ax2.text(0.83,3.44e4,"100 Myr", fontsize = 20)
ax3.text(0.83,3.44e4,"500 Myr", fontsize = 20)

ax1.set_xlim(0,1.0)
ax2.set_xlim(0,1.0)
ax3.set_xlim(0,1.0)
ax1.set_ylim(3e3,4e4)
ax1.set_yscale("log")
ax1.set_xlabel(r"$r/L_{\rm box}$")
ax2.set_xlabel(r"$r/L_{\rm box}$")
ax3.set_xlabel(r"$r/L_{\rm box}$")
ax1.set_ylabel("T [K]")
ax3.legend(loc = "lower center", fontsize = 17, ncol = 2)
plt.tight_layout()
plt.savefig("strom_temp.png")
plt.savefig("strom_temp.pdf")
#plt.show()
plt.close()
