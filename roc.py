#!/usr/bin/env python
# coding = utf-8

import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from scipy.interpolate import spline

def roc(data,TP,FP,TN,FN,TPR,FPR,vmin,vmax):

    # vmin = np.ndarray.min(data)
    # vmax = np.ndarray.max(data)

    k=0
    for i in range(int(vmin),int(vmax),1):
        TP[k] = 0
        FP[k] = 0
        TN[k] = 0
        FN[k] = 0
        k = k+1

    k=0
    for i in range(int(vmin),int(vmax),1):
        for j in range(0,data.size/2):
            if data[j][0] < i and data[j][1] == 1:
               TP[k] = TP[k] +1
            elif data[j][0] < i and data[j][1] == 0:
               FP[k] = FP[k] + 1
            elif data[j][0] > i and data[j][1] == 0:
               TN[k] = TN[k] +1
            elif data[j][0] > i and data[j][1] == 1:
               FN[k] = FN[k] +1
        k = k+1
    k=0
    for i in range(int(vmin),int(vmax),1):
        TPR[k] = TP[k]*1.0/(TP[k]+FN[k])
        FPR[k] = FP[k]*1.0/(FP[k]+TN[k])
        k = k+1

data = np.loadtxt('label.txt')
data1 = np.loadtxt('label1.txt')

vmin = np.ndarray.min(data)
vmax = np.ndarray.max(data)
TP = [1]*(vmax-vmin+1)
FP = [1]*(vmax-vmin+1)
TN = [1]*(vmax-vmin+1)
FN = [1]*(vmax-vmin+1)

vmin1 = np.ndarray.min(data1)
vmax1 = np.ndarray.max(data1)
TP1 = [1]*(vmax1-vmin1+1)
FP1 = [1]*(vmax1-vmin1+1)
TN1 = [1]*(vmax1-vmin1+1)
FN1 = [1]*(vmax1-vmin1+1)

TPR =[1]*(vmax-vmin) 
FPR =[1]*(vmax-vmin) 
TPR1 =[1]*(vmax1-vmin1) 
FPR1 =[1]*(vmax1-vmin1)

roc(data,TP,FP,TN,FN,TPR,FPR,vmin,vmax)
roc(data1,TP1,FP1,TN1,FN1,TPR1,FPR1,vmin1,vmax1)

FSIZE = 25
plt.figure(figsize=(10,8),frameon=True)
matplotlib.rc('xtick', labelsize=FSIZE)
matplotlib.rc('ytick',labelsize=FSIZE)

plt.plot(FPR,TPR, 'ro--',label='vrouter',lw=3,markersize=10)
plt.plot(FPR1,TPR1, 'ys-',label='vfirewall',lw=3,markersize=10)
plt.ylim(0.6,1)
plt.xlim(0,0.2)
plt.xlabel('FPR',fontsize=FSIZE)
plt.ylabel('TPR',fontsize=FSIZE)
plt.legend(loc='lower right',numpoints=1,fontsize=FSIZE)
plt.show()
plt.savefig("roc.png")