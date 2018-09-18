# -*- coding: utf-8 -*-
"""
@author: dhakk
"""


import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

###PATHS###
FILE_ROOT='C:\\Users\\hakkad\\Documents\\GitHub\\lostin4Dspace\\'

LOFS_RAW_FILENAME='LOFS4D.xlsx'
STREAMERS_RAW_FILENAME='Streamer4D.xlsx'
PRESSURES_FILENAME='PressureTargets.csv'

PRESSURES_TARGET_OUTPUT_FILENAME='Dataset.csv'

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
