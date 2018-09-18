# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 02:45:17 2018

@author: hakkad
"""

import pandas as pd

###PATHS###
FILE_ROOT='C:\\Users\\hakkad\\ForceHackathon\\'

PRESSURES_RAW_FILENAME='Pressures.xlsx'

######

pressures=pd.read_excel(FILE_ROOT+PRESSURES_RAW_FILENAME)
pressuresStreamer=pressures[['Well','MD','Z','PTI_TVT','S92','S02','S12']]
pressuresLOFS=pressures[['Well','MD','Z','PTI_TVT','L1','L6','L12','L14','L16','L18']]

