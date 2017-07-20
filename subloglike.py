#!/usr/bin/env python
# coding = utf-8

import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import sys

from scipy.interpolate import spline
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

fname = ['5_20_50','5_30_100','10_20_100','10_30_50']
caption = ['(a)','(b)','(c)','(d)']

FSIZE = 120
myfig = plt.figure(figsize=(80,70),frameon=True)
myfig.subplots_adjust(left=0.1,right=0.95,top=0.95, bottom=0.1)
matplotlib.rc('xtick', labelsize=FSIZE)
matplotlib.rc('ytick',labelsize=FSIZE)

dir = 'label/'
k=1
for fdata in fname:
	data = np.loadtxt('c1/'+fdata+'_train_result.txt')
	data1 = np.loadtxt('c1/'+fdata+'_test_result.txt')

	plt.subplot(2,2,k)
	
	plt.plot(data[400:2400],'y-',label='train',lw=10,markersize=30)
	plt.plot(data1[400:2400],'k-',label='test',lw=10,markersize=30)

	plt.xlabel('Elapsed time\n'+caption[k-1],fontsize=FSIZE)
	plt.ylabel('Log Likelihood',fontsize=FSIZE)
	plt.legend(loc='lower left',fontsize=FSIZE)
	k = k+1
plt.savefig(dir+'subloglike.png')  