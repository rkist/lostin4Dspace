from configurations import *

import matplotlib.pyplot as plt
import sklearn
import numpy as np

#for cases in ['S','L']:
case='L'
if True:
   
    trainDf= pd.read_csv(FILE_ROOT+TRAIN_DATASET_FILENAME)
    testDf= pd.read_csv(FILE_ROOT+TEST_DATASET_FILENAME)
    
    trainDf=trainDf[[True if x.startswith(case) else False for x in trainDf.DeltaCase ]]
    testDf=testDf[[True if x.startswith(case) else False for x in testDf.DeltaCase ]]
    
    print(trainDf.head())
    print(len(trainDf.index))
    
    print(testDf.head())
    print(len(testDf.index))
    
    from sklearn.model_selection import RandomizedSearchCV
    # Number of trees in random forest
    n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
    # Number of features to consider at every split
    max_features = ['auto', 'sqrt']
    # Maximum number of levels in tree
    max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
    max_depth.append(None)
    # Minimum number of samples required to split a node
    min_samples_split = [2, 5, 10]
    # Minimum number of samples required at each leaf node
    min_samples_leaf = [1, 2, 4]
    # Method of selecting samples for training each tree
    bootstrap = [True, False]
    # Create the random grid
    random_grid = {'n_estimators': n_estimators,
                   'max_features': max_features,
                   'max_depth': max_depth,
                   'min_samples_split': min_samples_split,
                   'min_samples_leaf': min_samples_leaf,
                   'bootstrap': bootstrap}
    
    
    rf = sklearn.ensemble.ExtraTreesRegressor(random_state = 0)
    rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)
    # Fit the random search model
    
    X = trainDf[[ "PTI_TVT", "co", "ai", "4D qual Fact"]]
    Y = trainDf["DeltaPressure"]
    trainingColumns = [ "PTI_TVT", "co", "ai"]
    
    Xtrain = trainDf[trainingColumns]
    Ytrain = trainDf["DeltaPressure"]
    
    Xtest = testDf[trainingColumns]
    Ytest = testDf["DeltaPressure"]
    
    print(Xtrain.head())
    print(Ytrain.head())
    
    rf_random.fit(Xtrain, Ytrain)
    regr = rf_random.best_estimator_
    #define 
    #regr = RandomForestRegressor(random_state=0, max_depth=8, n_estimators=300,verbose=1, criterion='mse')
    
    
    
    
    # RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=2,
    #            max_features='auto', max_leaf_nodes=None,
    #            min_impurity_decrease=0.0, min_impurity_split=None,
    #            min_samples_leaf=1, min_samples_split=2,
    #            min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
    #            oob_score=False, random_state=0, verbose=0, warm_start=False)
    
    
    y = regr.predict(Xtrain)
    plt.figure(figsize=(10,10))
    plt.scatter(Ytrain,y,c=trainDf["4D qual Fact"])
    plt.colorbar()
    plt.ylim(-3000,0)
    plt.xlim(-3000,0)
    
    
    y = regr.predict(Xtest)
    
    
    
    
    plt.figure(figsize=(10,10))
    plt.scatter(Ytest,y,c=testDf["4D qual Fact"])
    plt.colorbar()
    plt.ylim(-3000,0)
    plt.xlim(-3000,0)
    
    print("R2 score:"+str(sklearn.metrics.r2_score(Ytest,y)))
    

trainDf= pd.read_csv(FILE_ROOT+TRAIN_DATASET_FILENAME)
testDf= pd.read_csv(FILE_ROOT+TEST_DATASET_FILENAME)
trainDf=trainDf[[True if x.startswith(case) else False for x in trainDf.DeltaCase ]]
testDf=testDf[[True if x.startswith(case) else False for x in testDf.DeltaCase ]]
    

importanceList=[]

metricsDictionary={'r2':[],'mse':[],'mae':[]}
for i in range(500):
    #define 
    regr = RandomForestRegressor(random_state=i, n_estimators=30, verbose=1, criterion='mse')
    
    
    X = trainDf[[ "PTI_TVT", "co", "ai", "4D qual Fact"]]
    Y = trainDf["DeltaPressure"]
    trainingColumns = [ "PTI_TVT", "co", "ai"]
    
    Xtrain = trainDf[trainingColumns]
    Ytrain = trainDf["DeltaPressure"]
    
    Xtest = testDf[trainingColumns]
    Ytest = testDf["DeltaPressure"]
    
    regr.fit(Xtrain, Ytrain, trainDf["4D qual Fact"])
    importanceList.append(regr.feature_importances_)
    # RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=2,
    #            max_features='auto', max_leaf_nodes=None,
    #            min_impurity_decrease=0.0, min_impurity_split=None,
    #            min_samples_leaf=1, min_samples_split=2,
    #            min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
    #            oob_score=False, random_state=0, verbose=0, warm_start=False)
    
    y = regr.predict(Xtest)
    
    
    metricsDictionary['r2'].append(sklearn.metrics.r2_score(Ytest,y))    
    metricsDictionary['mse'].append(sklearn.metrics.mean_squared_error(Ytest,y))
    metricsDictionary['mae'].append(sklearn.metrics.mean_absolute_error(Ytest,y))    


importanceDict={}
for i in range(len(trainingColumns)):
     col=trainingColumns[i]
     importanceDict[col]=[x[i] for x in importanceList]

importanceDf=pd.DataFrame(importanceDict)
     