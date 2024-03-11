from GeneralUtilities.tracing.tracer import trace
from GeneralUtilities.file_ops.file_ops import read_csv
import pandas as pd
import csv

class ProfessorDumpToPandas:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path
    
    def read_csv(self):
        return pd.read_csv(self.csv_path)
