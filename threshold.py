#!/usr/bin/env python
# coding = utf-8

import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from scipy.interpolate import spline

fname = ['10_20_50','5_30_100','10_20_100','10_30_50']
dir = 'label/'
for flabel in fname:

    data = np.loadtxt(dir+flabel+'.txt')
    data = data[400:2400]
    vmin = np.ndarray.min(data)
    vmax = np.ndarray.max(data)

    TP = [1]*(vmax-vmin+1)
    FP = [1]*(vmax-vmin+1)
    TN = [1]*(vmax-vmin+1)
    FN = [1]*(vmax-vmin+1)

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
    TPR =[1]*(vmax-vmin) 
    FPR =[1]*(vmax-vmin) 
    Youden = [1]*(vmax-vmin)
    discretLog = [1]*(vmax-vmin)

    k=0
    for i in range(int(vmin),int(vmax),1):
        TPR[k] = TP[k]*1.0/(TP[k]+FN[k])
        FPR[k] = FP[k]*1.0/(FP[k]+TN[k])
        Youden[k] = TPR[k]-FPR[k]
        discretLog[k] = i
        k = k+1

    maxY = Youden[0]
    maxL = 0
    k=0
    for i in range(int(vmin),int(vmax),1):
        if maxY < Youden[k]:
            maxY = Youden[k]
            maxL = discretLog[k]
        k = k+1

    x = [maxL,maxL]
    y = [0,1]

    FSIZE = 45
    plt.figure(figsize=(14,12),frameon=True)
    matplotlib.rc('xtick', labelsize=FSIZE-10)
    matplotlib.rc('ytick',labelsize=FSIZE)
    plt.plot(discretLog, TPR, 'yx-', label='TPR',lw=8,markersize=30)
    plt.plot(discretLog, FPR, 'k.-', label='FPR',lw=8,markersize=30)
    plt.plot(discretLog, Youden, 'c^-', label='Youden',lw=5,markersize=15)
    plt.plot(x,y,'b',lw=8)

    #xnew = np.linspace(np.array(discretLog).min(),np.array(discretLog).max(),500)
    #smooth_TPR = spline(discretLog,TPR,xnew)
    #smooth_FPR = spline(discretLog,FPR,xnew)
    #smooth_Youden = spline(discretLog,Youden,xnew)
    #plt.plot(xnew,smooth_TPR,lw=3)
    #plt.plot(xnew,smooth_FPR,lw=3)
    #plt.plot(xnew,smooth_Youden,lw=3)
    plt.ylim(0,1)
    plt.xlabel('Log Likelihood',fontsize=FSIZE)
    plt.ylabel('TPR,FPR,Youden index',fontsize=FSIZE)
    plt.legend(loc='best',numpoints=1,fontsize=FSIZE-15)
    plt.show()
    plt.savefig(dir+flabel+".png")
