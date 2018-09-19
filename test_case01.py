from configurations import *

from scorer import *
from output import *

def CreateClassifier():
    regr = RandomForestRegressor(bootstrap=True, max_depth=8,
           max_features='auto', max_leaf_nodes=None,
           min_impurity_decrease=0.0, min_impurity_split=None,
           min_samples_leaf=1, min_samples_split=2,
           min_weight_fraction_leaf=0.0, n_estimators=20, n_jobs=10,
           oob_score=False, random_state=0, verbose=1, warm_start=False)
    # regr = RandomForestRegressor(max_depth=8, random_state=0)
    return regr

# def CreateClassifier():
#     regr = svm.SVR(C=1e2, cache_size=200, coef0=0.0, degree=3, epsilon=0.01, gamma="auto", 
#         kernel='poly', max_iter=1e7, shrinking=True, tol=0.001, verbose=True)
#     return regr


# def CreateClassifier():
#     regr = linear_model.Ridge (alpha = .5)
#     return regr


def TrainIt(showPlots = True):
    """run the first stuff"""
    trainDf= pd.read_csv(FILE_ROOT+TRAIN_DATASET_FILENAME)
    testDf= pd.read_csv(FILE_ROOT+TEST_DATASET_FILENAME)

    print(trainDf.head())
    print(trainDf.index)

    print(testDf.head())
    print(testDf.index)


    #define 
    Xtrain = trainDf[trainingColumns]
    Ytrain = trainDf[predictColumn]
    Wtrain = trainDf[weightColumn]

    Xtest = testDf[trainingColumns]
    Ytest = testDf[predictColumn]
    Wtest = testDf[weightColumn]

    print(Xtrain.head())
    print(Ytrain.head())



    scaler = preprocessing.StandardScaler().fit(Xtrain)

    Xtrain = scaler.transform(Xtrain) 
    Xtest = scaler.transform(Xtest) 


    regr = CreateClassifier()
    regr.fit(Xtrain, Ytrain, sample_weight=Wtrain)
    # regr.fit(Xtrain, Ytrain)


    Ypredicted = regr.predict(Xtest)

    print('{} == {}'.format(len(Ypredicted), len(Ytest)))


    OutputPredictedVsTest(Ypredicted, Ytest, PREDICTED_AND_TEST_FILENAME)

    OutputXYZandP(trainDf[["x", "y", "Z", "DeltaCase"]], Ytrain, "pTrain.csv")

    OutputXYZandP(testDf[["x", "y", "Z", "DeltaCase"]], Ytest, "pTest.csv")
    OutputXYZandP(testDf[["x", "y", "Z", "DeltaCase"]], Ypredicted, "pPredict.csv")   



    #score
    # print(regr.score(Xtest, Ytest))
    print(regr.score(Xtest, Ytest, sample_weight=Wtest))

    print(score_medium(Ytest, Ypredicted))
    if (showPlots):
        plot_scatter(Ytrain, regr.predict(Xtrain), Wtrain)
        plot_scatter(Ytest, Ypredicted, Wtest)

    return regr

