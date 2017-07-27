#!/usr/bin/env python
# coding = utf-8

import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from scipy.interpolate import spline
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from scipy import stats

from os import listdir

caption = ['(a)','(b)']
FSIZE = 20
myfig = plt.figure(figsize=(12,5),frameon=True)
myfig.subplots_adjust(left=0.07,right=0.97,top=0.95,bottom=0.21,hspace=0.2,wspace=0.2)
matplotlib.rc('xtick', labelsize=FSIZE-2)
matplotlib.rc('ytick',labelsize=FSIZE)

x = np.arange(-0.05,0.05,0.005)
y = stats.norm.pdf(x,0,0.01)
y = y/100.

width = 0.002

ax=plt.subplot(121)
y[10]=y[10]+0.16
y[9]=y[9]-0.05
y[11]=y[11]-0.01
y[8]=y[8]-0.03
y[12]=y[12]-0.05
y[7] = y[7] - 0.02
y[13] = y[13]
y[6] = y[6] + 0.01
y[14] = y[14] - 0.01
y[5] = y[5] + 0.01
y[15] = y[15] - 0.01
plt.bar(x,y,width,align='center')
plt.xlabel('$\Delta P_{TI}$\n'+caption[0],fontsize=FSIZE)
plt.ylabel('Probability',fontsize=FSIZE)
plt.ylim(0,0.6)
plt.grid()

ax=plt.subplot(122)

x = np.arange(-0.05,0.05,0.005)
y = stats.norm.pdf(x,0,0.01)
y = y/100.

y[10]=y[10]+0.19
y[9]=y[9]-0.02
y[11]=y[11]-0.06
y[8]=y[8]-0.02
y[12]=y[12]-0.05
y[7] = y[7] - 0.03
y[13] = y[13] - 0.01
y[6] = y[6] - 0.01
y[14] = y[14] + 0.01
y[5] = y[5] - 0.01
y[15] = y[15] + 0.01

plt.bar(x,y,width,align='center')
plt.xlabel('$\Delta P_{TI}$\n'+caption[1],fontsize=FSIZE)
plt.ylabel('Probability',fontsize=FSIZE)
plt.ylim(0,0.6)
plt.grid()

plt.savefig('label/delta.png')

