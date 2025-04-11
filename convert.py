import pandas as pd
import json

# /Users/uyn/learning_python/mapping.xlsx


def read_file(sheetname: str):
    df = pd.read_excel('/Users/uyn/learning_python/mapping.xlsx', sheet_name=sheetname, header=None)
    return df

df = read_file(sheetname="chung khoan")
print(df)

def convert(df: pd.DataFrame):
    dict_data = dict(zip(df[1],df[0]))
    return dict_data

dict_data = convert(df)
print(dict_data)

with open('chung_khoan.json','w') as outfile:
    json.dump(dict_data, outfile, ensure_ascii=False, indent=4)

