#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
学习使用seaborn的热图heatmap
Annotated heatmaps
'''

# 模块导入
# 标准库导入
import ssl
# 第三方库导入
import matplotlib.pyplot as plt
import seaborn as sns

# seaborn global settings
sns.set()
# urllib's ssl cert settings
ssl._create_default_https_context = ssl._create_unverified_context

# Load the example flights dataset and conver to long-form
flights_long = sns.load_dataset("flights")
flights = flights_long.pivot("month", "year", "passengers")

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(flights, annot=True, fmt="d", linewidth=.5, ax=ax)

plt.show()
