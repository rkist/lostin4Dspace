
"""
@author: dhakk
"""

import pandas as pd
import random
from configurations import FILE_ROOT,PRESSURES_FILENAME,LOFS_RAW_FILENAME,STREAMERS_RAW_FILENAME,DATASET_OUTPUT_FILENAME
from configurations import TRAIN_DATASET_FILENAME,TEST_DATASET_FILENAME,TRAIN_PARTITION_PCT

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

###PATHS###
######

pressuresDf= pd.read_csv(FILE_ROOT+PRESSURES_FILENAME)

pressuresDf.describe()

lofsDf=pd.read_excel(FILE_ROOT+LOFS_RAW_FILENAME)
lofsDf.columns=[x.replace('_TVT','_') for x in lofsDf.columns]

streamersDf=pd.read_excel(FILE_ROOT+STREAMERS_RAW_FILENAME)
streamersDf.columns=[x.replace('_TVT','_') for x in streamersDf.columns]

datasetDf=pressuresDf.copy()
print("After pressure target, row count:"+str(len(datasetDf.index)))

uniqueCases=datasetDf.DeltaCase.unique()


caseList=[]
for case in uniqueCases:
    if case.startswith('S'):
        #Streamer
        base=case.split('minus')[1]
        monitor=case.split('minus')[0]
        co_columnname='4D CO'+monitor+"-"+base
        ai_columnname='4D AI'+monitor+"-"+base
        
        if co_columnname not in streamersDf.columns:
            print("Column name missing:"+co_columnname)
        if ai_columnname not in streamersDf.columns:
            print("Column name missing:"+co_columnname)
        
        tmpDf=streamersDf[['Well','Z',co_columnname,ai_columnname]]
        tmpDf.columns=['Well','Z','co','ai']
        tmpDf['DeltaCase']=case
        caseList.append(tmpDf)
    elif case.startswith('L'):
        base=case.split('minus')[1]
        monitor=case.split('minus')[0]
        co_columnname='4D CO_'+monitor+"-"+base+"_"
        ai_columnname='4D AI_'+monitor+"-"+base+"_"
        if co_columnname not in lofsDf.columns:
            print("Column name missing:"+co_columnname)
        if ai_columnname not in lofsDf.columns:
            print("Column name missing:"+co_columnname)
        
        tmpDf=lofsDf[['Well','Z',co_columnname,ai_columnname]]
        tmpDf.columns=['Well','Z','co','ai']
        tmpDf['DeltaCase']=case
        caseList.append(tmpDf)
    else:
        raise ValueError('Bad case:'+case)


caseDf=pd.concat(caseList)
datasetDf=pd.merge(datasetDf,caseDf,on=['Well','Z','DeltaCase'])
print("After ai and co features, row count:"+str(len(datasetDf.index)))
datasetDf=pd.merge(datasetDf,streamersDf[['Well','Z','4D qual Fact']], on =['Well','Z'])
print("After quality features, row count:"+str(len(datasetDf.index)))

print("Unique wells: "+ str(len(datasetDf.Well.unique())))

datasetDf.to_csv(FILE_ROOT+DATASET_OUTPUT_FILENAME)

uniqueWells=datasetDf.Well.unique()

random.shuffle(uniqueWells)
trainWells=uniqueWells[range(int(TRAIN_PARTITION_PCT*len(uniqueWells)))]

trainDf=datasetDf[[x in trainWells for x in datasetDf.Well]]
testDf=datasetDf[[x not in trainWells for x in datasetDf.Well]]

trainDf.to_csv(FILE_ROOT+TRAIN_DATASET_FILENAME)
testDf.to_csv(FILE_ROOT+TEST_DATASET_FILENAME)





