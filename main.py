from ingest_data import IngestData
from dataset_shaping import SplitAndCleanData
from test_case01 import TrainIt
from output import OutputXYZandP
from scorer import plot_hist

import pandas as pd
from configurations import MAP_FILENAME,FILE_ROOT,PRESSURES_FILENAME,LOFS_RAW_FILENAME,STREAMERS_RAW_FILENAME,DATASET_OUTPUT_FILENAME
from configurations import SELECTED_WELL_ID
from configurations import weightColumn, predictColumn, trainingColumns

def IngestShapeTrain(plot = True):
    IngestData()
    SplitAndCleanData()
    regr = TrainIt(plot)
    return regr

if __name__ == "__main__":
    regr = IngestShapeTrain(True)

    print("-----------------------------------------------------")
    datasetDf = pd.read_csv(FILE_ROOT+DATASET_OUTPUT_FILENAME) 

    # theWell = datasetDf[datasetDf["Well"] == SELECTED_WELL_ID]
    theWell = datasetDf
    print(theWell.head())

    predictedPressure = regr.predict(theWell[trainingColumns])


    OutputXYZandP(theWell[["x", "y", "Z", "DeltaCase"]], theWell[predictColumn], "WellsOriginalP.csv")
    OutputXYZandP(theWell[["x", "y", "Z", "DeltaCase"]].reset_index(), predictedPressure, "WellsPredictedP.csv")

    # plot_hist(datasetDf["PTI_TVT"])
    # plot_hist(datasetDf["co"])
    # plot_hist(datasetDf["ai"])


    print("-----------------------------------------------------")
    mapDf = pd.read_csv(FILE_ROOT+MAP_FILENAME) 

    print(mapDf.head())

    predictedPressureMap = regr.predict(mapDf[trainingColumns])

    print(predictedPressureMap)

    OutputXYZandP(mapDf[["x", "y"]], predictedPressureMap, "PressureMap.csv")

