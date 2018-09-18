from configurations import *


trainDf= pd.read_csv(FILE_ROOT+TRAIN_DATASET_FILENAME)
# targetDf= pd.read_csv(FILE_ROOT+PRESSURES_TARGET_OUTPUT_FILENAME)

print(trainDf.head())
# print(targetDf.head())

print(trainDf.index)
# print(targetDf.index)


#define 
regr = RandomForestRegressor(max_depth=4, random_state=0, n_estimators=100, verbose=1, criterion='mse')

X = trainDf[[ "PTI_TVT", "co", "ai", "4D qual Fact"]]
Y = trainDf["DeltaPressure"]

print(X.head())
print(Y.head())

regr.fit(X, Y)

# RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=2,
#            max_features='auto', max_leaf_nodes=None,
#            min_impurity_decrease=0.0, min_impurity_split=None,
#            min_samples_leaf=1, min_samples_split=2,
#            min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
#            oob_score=False, random_state=0, verbose=0, warm_start=False)


print(regr.feature_importances_)



testDf= pd.read_csv(FILE_ROOT+TEST_DATASET_FILENAME)

X = testDf[[ "PTI_TVT", "co", "ai", "4D qual Fact"]]
Y = testDf["DeltaPressure"]

#score
print(regr.score(X, Y))




