import pandas as pd
from CSV_to_PandasDF import ConvertCSVtoPandasDF

class OfficialFacultyTitles:
    def __init__(self, csv_path: str):
        self.csv_path: str = csv_path
        self.df: pd.DataFrame = ConvertCSVtoPandasDF.get_df(csv_path=self.csv_path)
        self.offical_faculty_titles_and_dept_dict: dict[str, str] = {}
        self.mapping_abbr_name_actual: dict[str, str] = {}
        self.construct_official_faculty_titles_and_dept(self.df, self.offical_faculty_titles_and_dept_dict, self.mapping_abbr_name_actual)
        self.official_faculty_titles_set: set[str] = self.construct_official_faculty_titles_set(self.offical_faculty_titles_and_dept_dict)
    
    @staticmethod
    def construct_official_faculty_titles_and_dept(df: pd.DataFrame, data_dict: dict[str,str]) -> None:
        for row in df.itertuples(index=False):
            key = f"{row.lastName}, {row.firstName}"
            if key not in data_dict:
                data_dict[key] = [row.departmentCode]
            else:
                data_dict[key].append(row.departmentCode)
    
    @staticmethod
    def construct_official_faculty_titles_set(data_dict: dict[str, list[str]]) -> set[str]:
        return set(data_dict.keys())
    
    def get_official_faculty_titles_dept(self) -> dict[str, str]:
        return self.offical_faculty_titles_and_dept_dict
        
    def get_official_faculty_titles_set(self) -> set[str]:
        return self.official_faculty_titles_set
    
if __name__ == "__main__":
    of = OfficialFacultyTitles(csv_path="/mnt/linuxlab/home/spresley1/Desktop/425Reset/Rommel-Center-Research/PythonCode/DeducedData/Files/professor_department_dump.csv")
    my_set = of.get_official_faculty_titles_set()
    for item in my_set:
        print(item)

