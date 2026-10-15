# -*- coding: utf-8 -*-
"""
读取并分析 D:/jqxx/data/raw_dataset.csv（外贸指数数据集）
"""
import pandas as pd
import numpy as np

DATA_PATH = r"D:\jqxx\data\raw_dataset.csv"

# 1. 读取数据（自动识别分隔符与编码；低内存模式避免混合类型警告）
df = pd.read_csv(DATA_PATH, low_memory=False)
print("=" * 60)
print("1. 数据概览")
print("=" * 60)
print(f"行数: {df.shape[0]}, 列数: {df.shape[1]}")
print(f"列名: {list(df.columns)}")
print(f"\n各列类型:\n{df.dtypes}")

print("\n" + "=" * 60)
print("2. 前 5 行")
print("=" * 60)
print(df.head().to_string())

print("\n" + "=" * 60)
print("3. 缺失值统计")
print("=" * 60)
missing = df.isna().sum()
print(missing[missing > 0].to_string() if (missing > 0).any() else "无缺失值")

print("\n" + "=" * 60)
print("4. 数值列 Data_value 的描述性统计")
print("=" * 60)
print(df["Data_value"].describe().to_string())

print("\n" + "=" * 60)
print("5. 关键分类列的唯一值数量")
print("=" * 60)
for col in ["Subject", "Group", "STATUS", "UNITS"]:
    print(f"{col}: {df[col].nunique()} 个唯一值")

print("\n" + "=" * 60)
print("6. 时间范围（Period 字段）")
print("=" * 60)
# Period 形如 1971.06，提取为字符串年月
period_str = df["Period"].astype(str)
print(f"最早: {period_str.min()}, 最晚: {period_str.max()}")

print("\n" + "=" * 60)
print("7. 按 Subject 分组的记录数 Top 10")
print("=" * 60)
print(df.groupby("Subject")["Data_value"].count().sort_values(ascending=False).head(10).to_string())

print("\n" + "=" * 60)
print("8. 各 UNITS 类别分布")
print("=" * 60)
print(df["UNITS"].value_counts().to_string())
