import pandas as pd

class ConvertCSVtoPandasDF:
    @staticmethod
    def get_df(csv_path: str = None):
        if (csv_path is None):
            raise ValueError("CSV Path is None, provide a CSV path via the argument csv_path={\path/to/file.csv}")
        df = pd.read_csv(csv_path)
        return df

