from ingest_data import IngestData
from dataset_shaping import SplitAndCleanData
from test_case01 import TrainIt
from output import OutputXYZandP

import pandas as pd
from configurations import FILE_ROOT,PRESSURES_FILENAME,LOFS_RAW_FILENAME,STREAMERS_RAW_FILENAME,DATASET_OUTPUT_FILENAME
from configurations import SELECTED_WELL_ID
from configurations import weightColumn, predictColumn, trainingColumns



def IngestShapeTrain(plot = True):
    IngestData()
    SplitAndCleanData()
    regr = TrainIt(plot)
    return regr

if __name__ == "__main__":
    regr = IngestShapeTrain(False)



    print("-----------------------------------------------------")
    datasetDf = pd.read_csv(FILE_ROOT+DATASET_OUTPUT_FILENAME) 

    theWell = datasetDf[datasetDf["Well"] == SELECTED_WELL_ID]
    print(theWell.head())

    predictedPressure = regr.predict(theWell[trainingColumns])

    OutputXYZandP(theWell[["x", "y", "Z", "DeltaCase"]].reset_index(), predictedPressure, "PredictedWell.csv")




