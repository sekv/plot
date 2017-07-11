#!/usr/bin/env python
# coding = utf-8

import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt

XNUM = 50
data = np.loadtxt('5_10_20_train_result.txt')
data1 = np.loadtxt('5_10_20_test_result.txt')
vmin = np.ndarray.min(data)
vmax = np.ndarray.max(data)

dist=[1]*XNUM
dist1=[1]*XNUM
for i in range(0,XNUM):
    dist[i]=0
    dist1[i]=0
print dist

seg = [1]*XNUM
for i in range(0,XNUM):
    seg[i]= vmin + (vmax-vmin)/XNUM*i
print seg
print seg[0]

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

FSIZE = 25
plt.figure(figsize=(10,8),frameon=True)
matplotlib.rc('xtick', labelsize=FSIZE)
matplotlib.rc('ytick',labelsize=FSIZE)
plt.plot(seg,distPtrain,'ro--',label='train',lw=7,markersize=15)
plt.plot(seg,distPtest,'ys-',label='test',lw=5,markersize=15)
plt.xlabel('Log Likelihood',fontsize=FSIZE)
plt.ylabel('Probability',fontsize=FSIZE)
plt.legend(loc='upper left',numpoints=1,fontsize=FSIZE)
plt.show()
plt.savefig("LikelihoodDistribution.png")