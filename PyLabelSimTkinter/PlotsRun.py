#import pandas as pd
#import glob as gb
#import os
import matplotlib.pyplot as pp
#import numpy as np
import matplotlib.cm as cm
#import random as rnd
Folders=[]
print(FolderName)
os.chdir(FolderName)

print(FolderName)

for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        Folders.append(os.path.join(dirname, subdirname))

FolderGood=[]
for kat in Folders:
    if kat.find('Render')==-1:
       #if kat.find('Bundle')==-1:
        FolderGood.append(kat)
Folders=FolderGood

for kat in range(len(Folders)):
    print(Folders[kat])
    os.chdir(Folders[kat])
    FileNames=gb.glob('Filament*.csv')
    for katN in FileNames:
        print(katN)
        Data=pd.DataFrame.from_csv(katN)
        LenIdx = len(Data.index)
        colors = cm.rainbow(np.linspace(0, 1, LenIdx))
        pp.clf()
        ColPos=np.arange(LenIdx)
        rnd.shuffle(ColPos)
        if  katN.find('TS_like')==-1:
            for katIdx in range(len(Data.index)):
                XY=np.squeeze(Data.iloc[[katIdx]].values)  
                XY=XY[~np.isnan(XY)]
                X0=XY[0]
                Y0=XY[1]
                Xi=np.arange(2,len(XY),2)
                Yi=np.arange(3,len(XY),2)
                pp.plot(X0,Y0,'k*')
                pp.plot(XY[Xi],XY[Yi],color=colors[ColPos[katIdx]],marker='o',linestyle=' ')
        else:
            X=Data['X'].values
            Y=Data['Y'].values
            X=X[~np.isnan(X)]
            Y=Y[~np.isnan(Y)]
            pp.plot(X,Y,'or',linestyle=' ')

            
        pp.axis([0.5,1.5,-0.1,0.1])
        pp.savefig(katN[0:len(katN)-4]+'.png')
    os.chdir(FolderName)

os.chdir('/home/yipgroup/image_store/Scripts/PyLabelSim/')
