#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
学习使用seaborn的分组音符图Grouped violinplots,
Grouped violinplots with split violins
'''

# 模块导入
# 标准库导入
import ssl
# 第三方库导入
import seaborn as sns
import matplotlib.pyplot as plt

# seaborn global configuration
sns.set(style="whitegrid", palette="pastel", color_codes=True)
# urllib's ssl cert configuration
ssl._create_default_https_context = ssl._create_unverified_context

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Draw a nested violinplot and split the violins for easier comparison
sns.violinplot(x="day", y="total_bill", hue="smoker",
               split=True, inner="quart",
               palette={"Yes": "y", "No": "b"},
               data=tips)
sns.despine(left=True)

plt.show()
