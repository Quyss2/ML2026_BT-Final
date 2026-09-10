from review_models.product import Product
import pandas as pd
products = []
p1 = Product("p1","Vinamilk",100,80,0.5,0,"c3")
p2 = Product("p2","Bia 333",120,20,0.2,0,"c2")
p3 = Product("p3","Coca",40,10,0.4,0,"c1")
p4 = Product("p4","Pepsi",70,50,0.1,0,"c1")
p5 = Product("p5","Tiger",230,40,0.01,0,"c2")
p6 = Product("p6","Milo",200,20,0.8,0,"c1")
products.extend([p1,p2,p3,p4,p5,p6])
#Xuất danh sách
for p in products:
    print(p)
# convert DataFrame
df = pd.DataFrame([vars(p) for p in products])
df["Total_price"]=df["Quantity"]*df["Price"]
print(df)
print("Tổng trị giá khoa hàng = ",df["Total_price"].sum())

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Giả sử products là danh sách các Product object đã có sẵn
# products = [Product(...), Product(...), ...]

# Đếm số lượng sản phẩm theo từng cate_id
cate_counter = Counter(p.cate_id for p in products)

# Tạo DataFrame thống kê
df_stats = pd.DataFrame({
    'cate_id': list(cate_counter.keys()),
    'so_luong_san_pham': list(cate_counter.values())
})

# Tính tỉ lệ phần trăm
df_stats['ty_le_%'] = (df_stats['so_luong_san_pham'] / df_stats['so_luong_san_pham'].sum() * 100).round(2)

# Sắp xếp giảm dần theo số lượng
df_stats = df_stats.sort_values(by='so_luong_san_pham', ascending=False).reset_index(drop=True)

print(df_stats)

# Vẽ pie chart
plt.figure(figsize=(8, 8))
plt.pie(
    df_stats['so_luong_san_pham'],
    labels=df_stats['cate_id'],
    autopct='%1.1f%%',
    startangle=90,
    textprops={'fontsize': 10}
)
plt.title('Tỉ lệ phân bố sản phẩm theo danh mục (cate_id)')
plt.axis('equal')  # đảm bảo hình tròn không bị méo
plt.tight_layout()
plt.show()