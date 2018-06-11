import sys
import numpy as np
import matplotlib.pyplot as plt
import pynbody as pyn

times = [10,50,100,500,10,50,100,500,10,50,100,500]
Nr = 3
Nc = 4
paths = ["/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom064/strom64.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom064/strom64.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom064/strom64.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom064/strom64.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom128/strom128.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom128/strom128.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom128/strom128.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom128/strom128.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom256/strom256.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom256/strom256.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom256/strom256.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom256/strom256."]

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

fig.text(0.5, 0.025, 'X [kpc]', ha='center', fontsize = 22)
fig.text(0.01, 0.5, 'Y [kpc]', va='center', rotation='vertical', fontsize = 22)

fig.subplots_adjust(left = 0.09, right = 0.82, bottom = 0.125, top = 0.925, wspace=0, hspace=0)# right=.84)
# x,y,w,h
cbar_ax = fig.add_axes([0.83, 0.125, 0.05, 0.8])
cbar = fig.colorbar(im, cax=cbar_ax)
cbar.ax.set_ylabel('Ionized Fraction', rotation=270, labelpad = 25)
plt.savefig("strom_slice.pdf")
plt.savefig("strom_slice.png")
#plt.show()
plt.close()
