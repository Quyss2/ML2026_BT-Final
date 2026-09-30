import pandas as pd
import numpy as np


def check_dataset(df):
    print("=" * 60)
    print("1. THÔNG TIN DATASET")
    print("=" * 60)

    print(f"Số dòng      : {df.shape[0]:,}")
    print(f"Số cột       : {df.shape[1]:,}")
    print(f"Dung lượng    : {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

    print("\nCác cột:")
    print(df.columns.tolist())

    # --------------------------------------------------
    print("\n" + "=" * 60)
    print("2. KIỂU DỮ LIỆU")
    print("=" * 60)

    print(df.dtypes)

    # --------------------------------------------------
    print("\n" + "=" * 60)
    print("3. MISSING VALUES")
    print("=" * 60)

    missing = pd.DataFrame({
        "missing_count": df.isna().sum(),
        "missing_percent": df.isna().mean() * 100
    })

    missing = missing[missing["missing_count"] > 0]
    missing = missing.sort_values("missing_percent", ascending=False)

    if missing.empty:
        print("Không có missing values.")
    else:
        print(missing)

    # --------------------------------------------------
    print("\n" + "=" * 60)
    print("4. DUPLICATE")
    print("=" * 60)

    duplicate_count = df.duplicated().sum()
    duplicate_percent = duplicate_count / len(df) * 100

    print(f"Số dòng duplicate : {duplicate_count:,}")
    print(f"Tỷ lệ duplicate   : {duplicate_percent:.2f}%")

    # --------------------------------------------------
    print("\n" + "=" * 60)
    print("5. UNIQUE VALUES")
    print("=" * 60)

    unique_info = pd.DataFrame({
        "unique_count": df.nunique(dropna=False),
        "unique_percent": df.nunique(dropna=False) / len(df) * 100
    })

    print(unique_info)

    # --------------------------------------------------
    print("\n" + "=" * 60)
    print("6. THỐNG KÊ NUMERIC")
    print("=" * 60)

    numeric_cols = df.select_dtypes(include=np.number).columns

    if len(numeric_cols) > 0:
        print(df[numeric_cols].describe().T)

    # --------------------------------------------------
    print("\n" + "=" * 60)
    print("7. CATEGORICAL COLUMNS")
    print("=" * 60)

    categorical_cols = df.select_dtypes(
        include=["object", "category", "bool"]
    ).columns

    for col in categorical_cols:
        print(f"\n[{col}]")
        print(f"Số unique: {df[col].nunique(dropna=False)}")
        print(df[col].value_counts(dropna=False).head(10))

    # --------------------------------------------------
    print("\n" + "=" * 60)
    print("8. KIỂM TRA INF")
    print("=" * 60)

    if len(numeric_cols) > 0:
        inf_count = np.isinf(df[numeric_cols]).sum()

        if inf_count.sum() == 0:
            print("Không có giá trị inf/-inf.")
        else:
            print(inf_count[inf_count > 0])

    # --------------------------------------------------
    print("\n" + "=" * 60)
    print("9. KIỂM TRA CỘT HẰNG")
    print("=" * 60)

    constant_cols = [
        col for col in df.columns
        if df[col].nunique(dropna=False) <= 1
    ]

    if constant_cols:
        print("Các cột chỉ có 1 giá trị:")
        print(constant_cols)
    else:
        print("Không có cột hằng.")

    # --------------------------------------------------
    print("\n" + "=" * 60)
    print("10. KIỂM TRA OUTLIER - IQR")
    print("=" * 60)

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        outliers = ((df[col] < lower) | (df[col] > upper)).sum()

        print(
            f"{col}: "
            f"{outliers:,} outliers "
            f"({outliers / len(df) * 100:.2f}%)"
        )


# ======================================================
# SỬ DỤNG
# ======================================================

df = pd.read_csv("databases/Final_Data/2019-Oct.csv")

check_dataset(df)