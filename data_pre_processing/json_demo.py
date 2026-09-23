import pandas as pd
df = pd.read_json('../datasets/SalesTransactions.json',
                 encoding="utf-8",dtype='unicode',)
print(df.head()) #mặc định 5 dòng đầu:
print(df.tail()) # mặc định 5 dòng cuối
print(df)
print(df.shape)
print(df.describe())# dùng cái này để hiện thông tin dùng cho ML

