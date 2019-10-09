import pandas as pd
import numpy as np

# 读取整个csv文件
csv_data = pd.read_csv('Requirements.csv')
# print(csv_data)
print(csv_data.groupby("Rid")["Aid"].nunique())
print(csv_data.groupby("Rid")["Aid"].nunique().describe())
print(csv_data["Rid"].nunique())
print(csv_data["Aid"].nunique())