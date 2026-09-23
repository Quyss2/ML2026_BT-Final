import pandas as pd
df = pd.read_csv('../datasets/SalesTransactions.csv',
                 encoding="utf-8",dtype='unicode',
                 sep='\t',
                 low_memory=False)
print(df.head()) #mặc định 5 dòng đầu:
print(df.tail()) # mặc định 5 dòng cuối
print(df)
print(df.shape)
print(df.describe())# dùng cái này để hiện thông tin dùng cho ML

