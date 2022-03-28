import pandas as pd
import json


read_file = pd.read_csv (r'test.csv')
read_file.to_excel(r'test.xlsx', index = None, header=True)

