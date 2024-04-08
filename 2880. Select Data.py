import pandas as pd
import numpy as np

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    ind = np.where(students['student_id'] == 101)
    return (students.loc[[i[0] for i in ind], ["name", "age"]])
