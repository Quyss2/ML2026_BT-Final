import pandas as pd

def find_top_n_orders(df, n):
    order_totals = df.groupby('OrderID').apply(lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum())
    top_n_orders = order_totals.sort_values(
        ascending=False
    ).head(n)

    result = top_n_orders.reset_index()
    result.columns = ['OrderID', 'Sum']

    return result

df = pd.read_csv('../datasets/SalesTransactions.csv')

n = int(input("Nhập n: "))

result = find_top_n_orders(df, n)

print("Top", n, "hóa đơn có tổng giá trị lớn nhất:")
print(result)