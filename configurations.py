from scorer import *

import numpy as np
import pandas as pd
from sklearn import svm
import cloudpickle

from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression

from sklearn.model_selection import cross_validate
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import make_scorer




pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

###PATHS###
FILE_ROOT='D:\\git\\github\\lostin4Dspace\\'

PRESSURES_RAW_FILENAME='Pressures.xlsx'
XY_RAW_FILENAME='Locations.xlsx'

PRESSURES_TARGET_OUTPUT_FILENAME='PressureTargets.csv'


###PATHS###
LOFS_RAW_FILENAME='LOFS4D.xlsx'
STREAMERS_RAW_FILENAME='Streamer4D.xlsx'
PRESSURES_FILENAME='PressureTargets.csv'

DATASET_OUTPUT_FILENAME='DatasetMaster.csv'

TRAIN_DATASET_FILENAME='Train.csv'
TEST_DATASET_FILENAME='Test.csv'
TRAIN_PARTITION_PCT=0.8