# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 02:45:17 2018

@author: hakkad
"""

import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

###PATHS###
FILE_ROOT='C:\\Users\\hakkad\\Documents\\GitHub\\lostin4Dspace\\'

PRESSURES_RAW_FILENAME='Pressures.xlsx'
XY_RAW_FILENAME='Locations.xlsx'

PRESSURES_TARGET_OUTPUT_FILENAME='PressureTargets.csv'

######

pressures=pd.read_excel(FILE_ROOT+PRESSURES_RAW_FILENAME)
pressuresStreamer=pressures[['Well','MD','Z','PTI_TVT','S92','S02','S12']]
pressuresLOFS=pressures[['Well','MD','Z','PTI_TVT','L1','L6','L12','L14','L16','L18']]

streamColumns=['S92','S02','S12']
lofsColumns=['L1','L6','L12','L14','L16','L18']



streamDeltaCols=[]
for i in range(len(streamColumns)):
    for j in range(len(streamColumns)):
        if i>=j:
            continue
        name=streamColumns[j]+"minus"+streamColumns[i]
       #print(name)
        streamDeltaCols.append(name)
        pressuresStreamer[name]=pressuresStreamer[streamColumns[j]]-pressuresStreamer[streamColumns[i]]
        

pressuresStreamer.describe()

lofsDeltaCols=[]

for i in range(len(lofsColumns)):
    for j in range(len(lofsColumns)):
        if i>=j:
            continue
        name=lofsColumns[j]+"minus"+lofsColumns[i]
        lofsDeltaCols.append(name)
        pressuresLOFS[name]=pressuresLOFS[lofsColumns[j]]-pressuresLOFS[lofsColumns[i]]
        
        
#pd.melt(df, id_vars=['A'], value_vars=['B'])

pressureTargets=pd.melt(pressuresStreamer,id_vars=['Well','MD','Z','PTI_TVT'],value_vars=streamDeltaCols)
pressureTargets.columns=['Well','MD','Z','PTI_TVT','DeltaCase','DeltaPressure']

lofsTargets=pd.melt(pressuresLOFS,id_vars=['Well','MD','Z','PTI_TVT'],value_vars=lofsDeltaCols)
lofsTargets.columns=['Well','MD','Z','PTI_TVT','DeltaCase','DeltaPressure']

targetsDf=pd.concat([pressureTargets,lofsTargets])
targetsDf.to_csv(FILE_ROOT+PRESSURES_TARGET_OUTPUT_FILENAME,header=True,index=False)
print(len(targetsDf.index)) 
       
xylocDf=pd.read_excel(FILE_ROOT+XY_RAW_FILENAME)
targetsDf=pd.merge(xylocDf,targetsDf,how='inner',on='Well')
print(len(targetsDf.index))
targetsDf.to_csv(FILE_ROOT+PRESSURES_TARGET_OUTPUT_FILENAME,header=True,index=False)
        