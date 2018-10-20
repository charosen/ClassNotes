#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
学习使用seaborn中的分组条图Grouped barplots.
'''

# 模块导入
# 标准库导入
import ssl
# 第三方库导入
import seaborn as sns
import matplotlib.pyplot as plt

# seaborn global configuration
sns.set(style="whitegrid")
# urllib's ssl cert configuration
ssl._create_default_https_context = ssl._create_unverified_context

# Load the example Titanic dataset
titanic = sns.load_dataset("titanic")

# Draw a nested barplot to show survival for class and sex
g = sns.catplot(x="class", y="survived", hue="sex", data=titanic,
                height=6, kind="bar", palette="muted")

g.despine(left=True)
g.set_ylabels("survival probability")

plt.show()
