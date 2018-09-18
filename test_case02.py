from configurations import *

import matplotlib.pyplot as plt

trainDf= pd.read_csv(FILE_ROOT+TRAIN_DATASET_FILENAME)
testDf= pd.read_csv(FILE_ROOT+TEST_DATASET_FILENAME)

print(trainDf.head())
print(trainDf.index)

print(testDf.head())
print(testDf.index)


#define 
regr = RandomForestRegressor(max_depth=4, random_state=0, n_estimators=100, verbose=1, criterion='mse')


X = trainDf[[ "PTI_TVT", "co", "ai", "4D qual Fact"]]
Y = trainDf["DeltaPressure"]
trainingColumns = [ "x", "y", "MD","Z",  "PTI_TVT", "co", "ai", "4D qual Fact"]

Xtrain = trainDf[trainingColumns]
Ytrain = trainDf["DeltaPressure"]

Xtest = testDf[trainingColumns]
Ytest = testDf["DeltaPressure"]

print(Xtrain.head())
print(Ytrain.head())

regr.fit(Xtrain, Ytrain)

# RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=2,
#            max_features='auto', max_leaf_nodes=None,
#            min_impurity_decrease=0.0, min_impurity_split=None,
#            min_samples_leaf=1, min_samples_split=2,
#            min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
#            oob_score=False, random_state=0, verbose=0, warm_start=False)

y = regr.predict(Xtest)

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 07:32:07 2018

@author: hakkad
"""




plt.scatter(Ytest,y)




