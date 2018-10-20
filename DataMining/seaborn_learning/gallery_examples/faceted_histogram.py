#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
学习使用数据子集来为直方图Histogram进行分格子，
Facetting histogram by subsets of data

FacetGrid应该是seaborn对matplotlib.pyplot的subplots的封装
'''

# 模块导入
# 标准库导入
import ssl
# 第三方库导入
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# seaborn gloabal configuration
sns.set(style="darkgrid")
# urllib's ssl cert configuration
ssl._create_default_https_context = ssl._create_unverified_context

# Load dataset
tips = sns.load_dataset("tips")

# Facetting with subsets of dataset
g = sns.FacetGrid(tips, row="sex", col="time", margin_titles=True)

# 分箱设置bining configuration
bins = np.linspace(0, 60, 13)

g.map(plt.hist, "total_bill", color="steelblue", bins=bins)

plt.show()
