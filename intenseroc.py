#!/usr/bin/env python
# coding = utf-8

import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from scipy.interpolate import spline
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from os import listdir

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


fname = ['10_20_50','5_30_100','10_20_100','10_30_50']
caption = ['(a)','(b)','(c)','(d)']
dir = 'c1_label/'
index = [0,2]
k=1
FSIZE = 35
myfig=plt.figure(figsize=(20,16),frameon=True)
myfig.subplots_adjust(left=0.1,right=0.95,top=0.95,bottom=0.1,hspace=0.32, wspace=0.23)
matplotlib.rc('xtick', labelsize=FSIZE)
matplotlib.rc('ytick',labelsize=FSIZE)

flabel = ['10_30_100','5_10_50','15_10_50','5_20_100','10_30_50','5_10_100',
          '5_10_50','5_30_100','15_30_100','10_30_50','10_10_100','20_20_100',
           '5_20_100','10_10_100','10_20_100','10_30_50','10_30_100','5_20_50',
          '15_10_100','5_20_100','5_10_100','5_30_100','15_10_200','10_10_100',]
cn = 6
data = [1]*cn
vmin = [1]*cn
vmax = [1]*cn
TP = [[0 for col in range(1)] for row in range(cn)]
FP = [[0 for col in range(1)] for row in range(cn)]
TN = [[0 for col in range(1)] for row in range(cn)]
FN = [[0 for col in range(1)] for row in range(cn)]
TPR = [[0 for col in range(1)] for row in range(cn)]
FPR = [[0 for col in range(1)] for row in range(cn)]

for i in range(0,len(flabel),cn):
    for j in range(0,cn):
        data[j] = np.loadtxt(dir+flabel[i+j]+'_label.txt')
        data[j] = data[j][400:2400]

        vmin[j] = np.ndarray.min(data[j])
        vmax[j] = np.ndarray.max(data[j])
        TP[j] = [1]*(vmax[j]-vmin[j]+1)
        FP[j] = [1]*(vmax[j]-vmin[j]+1)
        TN[j] = [1]*(vmax[j]-vmin[j]+1)
        FN[j] = [1]*(vmax[j]-vmin[j]+1)

        TPR[j] =[1]*(vmax[j]-vmin[j]) 
        FPR[j] =[1]*(vmax[j]-vmin[j]) 

        roc(data[j],TP[j],FP[j],TN[j],FN[j],TPR[j],FPR[j],vmin[j],vmax[j])
        
    ax=plt.subplot(2,2,k)

    xmajorLocator = MultipleLocator(0.03)
    ax.xaxis.set_major_locator(xmajorLocator)
    
    mymark = ['+-','.-','3-','4-','x-','*-']
    myc = ['g','k','r','b','c','y']
    mylegend = ['ANSP 100%', 'ANSP 80%','ANSP 60%','ACRU 100%','ACRU 80%','ACRU 60%']
    mylegend1 = ['ANSP 40%', 'ANSP 20%','ANSP 10%','ACRU 40%','ACRU 20%','ACRU 10%']
    
    for j in range(0,cn):
        if k<=2:
            plt.plot(FPR[j],TPR[j],mymark[j],color=myc[j],mec=myc[j],label=mylegend[j],lw=3,ms=18,mew=3,markevery=10)
        else:
            plt.plot(FPR[j],TPR[j],mymark[j],color=myc[j],mec=myc[j],label=mylegend1[j],lw=3,ms=18,mew=3,markevery=5)
    
    plt.ylim(0.7,1)
    plt.xlim(0,0.15)
    plt.xlabel('FPR\n'+caption[k-1],fontsize=FSIZE)
    plt.ylabel('TPR',fontsize=FSIZE)
    plt.legend(loc='lower right',numpoints=1,fontsize=FSIZE-10)
    plt.grid('--',lw=1)   
    k = k+1

plt.savefig('label/'+"roc6.png")
plt.close()