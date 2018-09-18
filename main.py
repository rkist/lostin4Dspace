from ingest_data import IngestData
from dataset_shaping import SplitAndCleanData
from test_case01 import RandomForestTheData

if __name__ == "__main__":
    IngestData()
    SplitAndCleanData()
    RandomForestTheData()