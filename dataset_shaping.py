# -*- coding: utf-8 -*-
"""
@author: dhakk
"""

from configurations import *

######

pressuresDf= pd.read_csv(FILE_ROOT+PRESSURES_FILENAME)
lofsDf=pd.read_excel(FILE_ROOT+STREAMERS_RAW_FILENAME)
lofsDf.columns=[x.replace('_TVT','_') for x in lofsDf.columns]

streamersDf=pd.read_excel(FILE_ROOT+STREAMERS_RAW_FILENAME)
streamersDf.columns=[x.replace('_TVT','_') for x in streamersDf.columns]

datasetDf=pressuresDf.copy()
print("After pressure target, row count:"+str(len(datasetDf.index)))

uniqueCases=datasetDf.DeltaCase.unique()

for case in uniqueCases:
    if case.startswith('S'):
        #Streamer
        pass
        base=case.split('minus')[1]
        monitor=case.split('minus')[0]
        co_columnname='4D CO'+monitor+"-"+base
        if co_columnname not in lofsDf.columns:
            print("Column name missing:"+co_columnname)

        
        
    elif case.startswith('L'):
        #Lofs
        pass
    else:
        raise ValueError('Bad case:'+case)
