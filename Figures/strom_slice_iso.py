import sys
import numpy as np
import matplotlib.pyplot as plt
import pynbody as pyn

times = [10,50,100,500,10,50,100,500,10,50,100,500]
Nr = 3
Nc = 4
paths = ["/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom064_iso/strom64_iso.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom064_iso/strom64_iso.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom064_iso/strom64_iso.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom064_iso/strom64_iso.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom128_iso/strom128_iso.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom128_iso/strom128_iso.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom128_iso/strom128_iso.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom128_iso/strom128_iso.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom256_iso/strom256_iso.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom256_iso/strom256_iso.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom256_iso/strom256_iso.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom256_iso/strom256_iso."]

images = []
fig, axes = plt.subplots(Nr,Nc, sharex=True, sharey=True, figsize = (7.3,5))
count = 0
for ax, time, path in zip(axes.flat, times, paths):
	count+=1
	fname = path + str(time).zfill(5)
	data = pyn.load(fname)
	data.properties['a']
	data.physical_units()
	data['pos'].convert_units("kpc")
	data.g['rho'].convert_units("m_p cm^-3")
	data.g["HII"] = 1-data.g["HI"]
	im = pyn.plot.sph.image(data.g,qty="HII",vmin=1e-3,vmax=1.0,width=16,ret_im=True,subplot=ax)
	ax.set_xlim(-7,7)
	ax.set_ylim(-7,7)
	if count < 5:
		ax.text(-3.7,7.8,str(time).zfill(3) + " Myr", fontsize = 15)
	res_fc = "white"
	res_fs = 15
	res_x = -6
	res_y = 4.7
	if count == 1: 
		 ax.text(res_x,res_y,"$64^3$",color = res_fc, fontsize = res_fs)
	elif count == 5:
		 ax.text(res_x,res_y,"$128^3$",color = res_fc, fontsize = res_fs)
	elif count == 9:
		 ax.text(res_x,res_y,"$256^3$",color = res_fc, fontsize = res_fs)
	
	
	rs = 5.38
	trecomb = 125
	r = rs*(1 - np.exp(-time/trecomb))**(1/3.)

	circle = plt.Circle((0.03, 0), r, color='red', fill=False, linestyle = ':')
	ax.add_artist(circle)


fig.text(0.5, 0.025, 'X [kpc]', ha='center', fontsize = 22)
fig.text(0.01, 0.5, 'Y [kpc]', va='center', rotation='vertical', fontsize = 22)

fig.subplots_adjust(left = 0.09, right = 0.82, bottom = 0.125, top = 0.925, wspace=0, hspace=0)# right=.84)
# x,y,w,h
cbar_ax = fig.add_axes([0.83, 0.125, 0.05, 0.8])
cbar = fig.colorbar(im, cax=cbar_ax)
cbar.ax.set_ylabel('Ionized Fraction', rotation=270, labelpad = 25)
plt.savefig("strom_slice_iso.pdf")
plt.savefig("strom_slice_iso.png")
#plt.show()
plt.close()
