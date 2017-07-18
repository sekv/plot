#!/usr/bin/env python
# coding = utf-8

import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import sys

cluster_num = [5,10,15,20,25]
component_num = [10,20,30]
window_num = [20, 50, 100,200]
dir = 'c1/'
dirpic = 'c1_distlog/'

for a in cluster_num:
	for b in component_num:
		for c in window_num:

			XNUM = 60
			data = np.loadtxt(dir+str(a)+'_'+str(b)+'_'+str(c)+'_'+'train_result.txt')
			data1 = np.loadtxt(dir+str(a)+'_'+str(b)+'_'+str(c)+'_'+'test_result.txt')
			data = data[1500:1700]
			data1 = data1[1500:1700]
			vmin1 = np.ndarray.min(data)
			vmin2 = np.ndarray.min(data1)
			vmax1 = np.ndarray.max(data)
			vmax2 = np.ndarray.max(data1)
			if(vmin1 <= vmin2):
				vmin = vmin1
			else:
				vmin = vmin2
			if(vmax1 > vmax2):
				vmax = vmax1 
			else:
				vmax = vmax2

			dist=[1]*XNUM
			dist1=[1]*XNUM
			for i in range(0,XNUM):
			    dist[i]=0
			    dist1[i]=0
			#print dist

			seg = [1]*XNUM
			for i in range(0,XNUM):
			    seg[i]= vmin + (vmax-vmin)/XNUM*i
			#print seg
			#print seg[0]

			#count the number of data items fall in segment seg[j]
			for i in range(0,data.size):
			    for j in range(0,XNUM):
			        if(data[i]>=seg[XNUM-1-j]):
			          dist[XNUM-1-j] = dist[XNUM-1-j] + 1
			          break

			for i in range(0,data1.size):
			    for j in range(0,XNUM):
			        if(data1[i]>=seg[XNUM-1-j]):
			          dist1[XNUM-1-j] = dist1[XNUM-1-j] + 1
			          break

			distPtrain = [1]*XNUM
			distPtest = [1]*XNUM
			for i in range(0,XNUM):
			    distPtrain[i] = dist[i]*1.0/data.size
			    distPtest[i] = dist1[i]*1.0/data1.size

			FSIZE = 45
			plt.figure(figsize=(16.5,12.5),frameon=True)
			matplotlib.rc('xtick', labelsize=FSIZE-5)
			matplotlib.rc('ytick',labelsize=FSIZE)
			plt.plot(seg,distPtrain,'yx-',label='train',lw=7,markersize=30)
			plt.plot(seg,distPtest,'k.--',label='test',lw=5,markersize=30)
			plt.xlabel('Log Likelihood',fontsize=FSIZE)
			plt.ylabel('Probability',fontsize=FSIZE)
			plt.legend(loc='upper left',numpoints=1,fontsize=FSIZE)
			plt.savefig(dirpic+str(a)+'_'+str(b)+'_'+str(c)+"logdist.png")
			plt.close()