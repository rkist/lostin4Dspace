from configurations import *

from scorer import *
from output import *

def CreateClassifier():
    regr = RandomForestRegressor(max_depth=8, random_state=0)
    return regr

# def CreateClassifier():
#     regr = svm.SVR()
#     return regr


# def CreateClassifier():
#     regr = linear_model.Ridge (alpha = .5)
#     return regr


def RandomForestTheData():
    """run the first stuff"""
    trainDf= pd.read_csv(FILE_ROOT+TRAIN_DATASET_FILENAME)
    testDf= pd.read_csv(FILE_ROOT+TEST_DATASET_FILENAME)

    print(trainDf.head())
    print(trainDf.index)

    print(testDf.head())
    print(testDf.index)


    #define 
    trainingColumns = [ "x", "y", "MD","Z",  "PTI_TVT", "co", "ai"]

    Xtrain = trainDf[trainingColumns]
    Ytrain = trainDf["DeltaPressure"]
    Wtrain = trainDf["4D qual Fact"]

    Xtest = testDf[trainingColumns]
    Ytest = testDf["DeltaPressure"]
    Wtest = testDf["4D qual Fact"]

    print(Xtrain.head())
    print(Ytrain.head())

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
    plot_scatter(Ytest, Ypredicted, Wtest)



