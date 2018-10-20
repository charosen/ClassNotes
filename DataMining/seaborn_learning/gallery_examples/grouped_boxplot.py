#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
学习使用seaborn分组盒图Group boxplots。
'''
# 模块导入
# 标准库导入
import ssl
# 第三方库导入
import seaborn as sns
import matplotlib.pyplot as plt

# seaborn global configuration
sns.set(style="ticks", palette="pastel")
# urllib's ssl cert configuratioon
ssl._create_default_https_context = ssl._create_unverified_context

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Draw a nested boxplot to show bills by day and time
sns.boxplot(x="day", y="total_bill",
            hue="smoker", palette=["m", "g"],
            data=tips)
sns.despine(offset=10, trim=True)

plt.show()
