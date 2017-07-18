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
dirpic = 'c1_log/'
for i in cluster_num:
	for j in component_num:
		for k in window_num:
			data = np.loadtxt(dir+str(i)+'_'+str(j)+'_'+str(k)+'_'+'train_result.txt')
			data1 = np.loadtxt(dir+str(i)+'_'+str(j)+'_'+str(k)+'_'+'test_result.txt')

			FSIZE = 45
			plt.figure(figsize=(19,12.5),frameon=True)
			matplotlib.rc('xtick', labelsize=FSIZE)
			matplotlib.rc('ytick',labelsize=FSIZE)
			plt.plot(data[400:2400],'y-',label='train',lw=3,markersize=5)
			plt.plot(data1[400:2400],'k-',label='test',lw=3,markersize=5)

			plt.xlabel('Elapsed time',fontsize=FSIZE)
			plt.ylabel('Log Likelihood',fontsize=FSIZE)
			plt.legend(loc='lower left',numpoints=1,fontsize=FSIZE)
			plt.savefig(dirpic+str(i)+'_'+str(j)+'_'+str(k)+'_'+"loglike.png")
			plt.close()