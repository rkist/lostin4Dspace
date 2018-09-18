from configurations import *


def RandomForestTheData():
    """run the first stuff"""
    trainDf= pd.read_csv(FILE_ROOT+TRAIN_DATASET_FILENAME)
    testDf= pd.read_csv(FILE_ROOT+TEST_DATASET_FILENAME)

    print(trainDf.head())
    print(trainDf.index)

    print(testDf.head())
    print(testDf.index)


    #define 
    regr = RandomForestRegressor(max_depth=4, random_state=0)

    trainingColumns = [ "x", "y", "MD","Z",  "PTI_TVT", "co", "ai"]

    Xtrain = trainDf[trainingColumns]
    Ytrain = trainDf["DeltaPressure"]
    Wtrain = trainDf["4D qual Fact"]

    Xtest = testDf[trainingColumns]
    Ytest = testDf["DeltaPressure"]
    Wtest = testDf["4D qual Fact"]

    print(Xtrain.head())
    print(Ytrain.head())

    regr.fit(Xtrain, Ytrain, sample_weight=Wtrain)

    # RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=2,
    #            max_features='auto', max_leaf_nodes=None,
    #            min_impurity_decrease=0.0, min_impurity_split=None,
    #            min_samples_leaf=1, min_samples_split=2,
    #            min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
    #            oob_score=False, random_state=0, verbose=0, warm_start=False)

    Ypredicted = regr.predict(Xtest)

    print(len(Ypredicted))
    print(len(Ytest))


    #score
    print(regr.score(Xtest, Ytest, sample_weight=Wtest))

    print(score_medium(Ytest, Ypredicted))
    plot_scatter(Ytest, Ypredicted, Wtest)

    

