import numpy as np
import pandas as pd

from configurations import FILE_ROOT, PREDICTED_AND_TEST_FILENAME

def OutputPredictedVsTest(Ypredicted, Ytest, filename):
    predictedVsTest = pd.concat([pd.DataFrame(Ypredicted), pd.DataFrame(Ytest)], axis=1, sort=False)
    predictedVsTest.to_csv(FILE_ROOT+filename)


def OutputXYZandP(xyz, p, filename):
    XYZandP = pd.concat([pd.DataFrame(xyz), pd.DataFrame(p)], axis=1, sort=False)
    XYZandP.to_csv(FILE_ROOT+filename)
