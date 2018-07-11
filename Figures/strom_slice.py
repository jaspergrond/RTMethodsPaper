import sys
import numpy as np
import matplotlib.pyplot as plt
import pynbody as pyn
from scipy.interpolate import griddata
import pylab as m

time = 30
ress = [64,128,256]
Nr = 1
Nc = 3
V = [10**-3.5,1e-3,10**-2.5,1e-2,10**-1.5,1e-1,5e-1,9e-1]

cdict = {
'red'  : ((0,0.06,0.06),(0.10,0.30,0.30),(0.20,0.25,0.25),(0.30,0.27,0.27),(0.40,0.48,0.48),(0.50,0.40,0.40),(0.60,0.39,0.39),(0.70,0.68,0.68),(0.75,0.94,0.94),(0.80,0.98,0.98),(0.90,0.93,0.93),(0.95,0.93,0.93),(1.00,1.00,1.00)),
'green': ((0,0.06,0.06),(0.10,0.14,0.14),(0.20,0.28,0.28),(0.30,0.40,0.40),(0.40,0.83,0.83),(0.50,0.78,0.78),(0.60,0.77,0.77),(0.70,0.85,0.85),(0.75,0.93,0.93),(0.80,0.66,0.66),(0.90,0.15,0.15),(0.95,0.12,0.12),(1.00,1.00,1.00)),
'blue' : ((0,0.05,0.05),(0.10,0.45,0.45),(0.20,0.65,0.65),(0.30,0.73,0.73),(0.40,0.87,0.87),(0.50,0.27,0.27),(0.60,0.19,0.19),(0.70,0.10,0.10),(0.75,0.06,0.06),(0.80,0.05,0.05),(0.90,0.13,0.13),(0.95,0.14,0.14),(1.00,1.00,1.00))
}

my_cmap = m.matplotlib.colors.LinearSegmentedColormap('my_colormap', cdict, 1024)

paths = ["/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom064_iso/strom64_iso.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom128_iso/strom128_iso.",
		 "/home/grondjj/Data/RadTransfer/Stromgren/runs/bigboys/strom256_iso/strom256_iso."]



fig, axes = plt.subplots(Nr,Nc, sharex=True, sharey=True, figsize = (6.3,2.07), squeeze = False)

for ax, path, res in zip(axes.flat, paths, ress):
	fname = path + str(time*2).zfill(5)
	data = pyn.load(fname)
	data.properties['a']
	data.physical_units()
	data['pos'].convert_units("kpc")
	data.g['rho'].convert_units("m_p cm^-3")
	im = pyn.plot.sph.image(data.g,qty="HI",width=16,ret_im=True,subplot=ax, cmap = my_cmap ,vmin = 1e-5, vmax = 1e0)
	x = np.array(data.g['x'][data.g['smooth']>np.fabs(data.g['z'])]) 
	y = np.array(data.g['y'][data.g['smooth']>np.fabs(data.g['z'])]) 
	z = np.array(data.g['HI'][data.g['smooth']>np.fabs(data.g['z'])]) 

	xgrid = np.linspace(np.min(x), np.max(x), res**2/10)
	ygrid = np.linspace(np.min(y), np.max(y), res**2/10)
	xgrid, ygrid = np.meshgrid(xgrid, ygrid)
	zgrid = griddata((x,y),z, (xgrid, ygrid), method='nearest')

	ax.contour(xgrid, ygrid, zgrid, V, colors='k',linewidths=0.5)#, colors = C)

	res_fc = "k"
	res_fs = 15
	res_x = -4.6
	res_y = 3.7
	ax.text(res_x, res_y, r"$\mathbf{" + str(res) + "^3}$", fontsize = res_fs, color = res_fc)
		
	rs = 5.38
	trecomb = 125
	r = rs*(1 - np.exp(-time/trecomb))**(1/3.)

	circle = plt.Circle((0.03, 0), r, color='white', fill=False, linestyle = ':',linewidth = 2, zorder=1e9)
	ax.add_artist(circle)
	lim =5 
	ax.tick_params(direction='in') 
	ax.set_xticks([-4,-2,0,2,4])
	ax.set_yticks([-4,-2,0,2,4])
	ax.set_xticklabels([])
	ax.set_yticklabels([])
	ax.set_xlim(-lim,lim)
	ax.set_ylim(-lim,lim)


fig.subplots_adjust(left = 0.05, right = 0.95, bottom = 0.05, top = 0.95, wspace=0, hspace=0)
plt.savefig("strom_slice_iso_030.pdf")
plt.savefig("strom_slice_iso_030.png")
#plt.show()
plt.close()

time = 500
fig, axes = plt.subplots(Nr,Nc, sharex=True, sharey=True, figsize = (6.3,2.07), squeeze = False)

for ax, path, res in zip(axes.flat, paths, ress):
	fname = path + str(time*2).zfill(5)
	data = pyn.load(fname)
	data.properties['a']
	data.physical_units()
	data['pos'].convert_units("kpc")
	data.g['rho'].convert_units("m_p cm^-3")
	im = pyn.plot.sph.image(data.g,qty="HI",width=16,ret_im=True,subplot=ax, cmap = my_cmap, vmin = 1e-5, vmax = 1e0)

	x = np.array(data.g['x'][data.g['smooth']>np.fabs(data.g['z'])]) 
	y = np.array(data.g['y'][data.g['smooth']>np.fabs(data.g['z'])]) 
	z = np.array(data.g['HI'][data.g['smooth']>np.fabs(data.g['z'])]) 

	xgrid = np.linspace(np.min(x), np.max(x), res**2/10)
	ygrid = np.linspace(np.min(y), np.max(y), res**2/10)
	xgrid, ygrid = np.meshgrid(xgrid, ygrid)
	zgrid = griddata((x,y),z, (xgrid, ygrid), method='nearest')

	ax.contour(xgrid, ygrid, zgrid, V,colors='k',linewidths=.5)

	res_fc = "k"
	res_fs = 15
	res_x = -6.4
	res_y = 5.3
	ax.text(res_x, res_y, r"$\mathbf{" + str(res) + "^3}$", fontsize = res_fs, color = res_fc)
		
	rs = 5.38
	trecomb = 125
	r = rs*(1 - np.exp(-time/trecomb))**(1/3.)

	circle = plt.Circle((0.03, 0), r, color='white', fill=False, linestyle = ':', linewidth = 2, zorder = 1e9)
	ax.add_artist(circle)
	lim = 7
	ax.tick_params(direction='in') 
	ax.set_xticks([-8,-6,-4,-2,0,2,4,6,8])
	ax.set_yticks([-8,-6,-4,-2,0,2,4,6,8])
	ax.set_xticklabels([])
	ax.set_yticklabels([])
	ax.set_xlim(-lim,lim)
	ax.set_ylim(-lim,lim)


fig.subplots_adjust(left = 0.05, right = 0.95, bottom = 0.05, top = 0.95, wspace=0, hspace=0)
plt.savefig("strom_slice_iso_500.pdf")
plt.savefig("strom_slice_iso_500.png")
#plt.show()
plt.close()
