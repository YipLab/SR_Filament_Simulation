#def RndNm(Nms,Bdm):
#    FNr=rnd.sample(Nms,Bdm)
#    return FNr;


#import pandas as pd
#import glob as gb
#import os
#import matplotlib.pyplot as pp
#import numpy as np
#import matplotlib.cm as cm
#import random as rnd
Folders=[]
FolderBund='Bundle/'
#BundleSpcing=0.005
#BundleNum=50
FoldOut=os.getcwd()
os.chdir(FolderName)
print(FolderName)
for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        Folders.append(os.path.join(dirname, subdirname))
       
FolderGood=[]
for kat in Folders:
    print(kat)
    if kat.find('Render')==-1:
        FolderGood.append(kat)
Folders=FolderGood
print(Folders)

for kat in range(len(Folders)):
    print(Folders[kat])
    os.chdir(Folders[kat])
    os.mkdir(FolderBund)
    FileNames=gb.glob('Filament*.csv')
    for katN in FileNames:
        DataRoot=pd.read_csv(katN,header=None)
        BundleIds=rnd.sample(FileNames,BundleNum-1)
        print(katN)
        Count=1
        for katNbd in BundleIds: 
            #Data=pd.DataFrame.from_csv(katNbd,header=None)
            Data=pd.read_csv(katNbd,header=None)
            #katkat
            Cols=Data.columns
            MaxCol=Cols.max()##max((Data.columns.values).astype(int))
            ColArr=np.arange(3,int(MaxCol),2)
            #print('Columns: '+ str(ColArr))
            #print('ColumnsMax: '+ str(MaxCol))
            #print('ColumnsSize: '+ str(ColArr.shape))
            #print('BundlID: '+katNbd)#
            #print('Bundles: '+str(BundleSpcing*Count))
            #print('DataShape: '+str(Data.iloc[:,ColArr]))
            #Data.iloc[:,ColArr]=Data.iloc[:,ColArr]+BundleSpcing*Count
            Data.loc[:,Cols[ColArr]]+=BundleSpcing*Count
            Count+=1
            DataRoot=DataRoot.append(Data)
        Col2=DataRoot.columns.values
        print('Columns2: ')
        print(Col2)
        '''print('Columns2: ')
        print(Col2.shape)
        print(Col2[0])
        print(Col2.sort())#df.sort_index(inplace=True)
        Col2=Col2.sort()'''
        #Col2.sort(key=float)
        #Col2.astype(str)
        #print('Columns2: '+ str(Col2))
        DataRoot.to_csv(FolderBund+katN[0:len(katN)-4]+'_Bundle.csv',index=False,header=None)#,columns = Col2
    os.chdir('../')


os.chdir(FoldOut)
