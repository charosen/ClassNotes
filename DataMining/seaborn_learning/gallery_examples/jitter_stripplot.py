#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
学习使用seaborn中显示条件均值conditional means, 并显示观测值，也就是数据点observation
Conditional means with observations
'''

# 模块导入
# 标准库导入
import ssl
# 第三方库导入
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# seaborn global setting
sns.set(style="whitegrid")
# urllib's ssl cert setting
ssl._create_default_https_context = ssl._create_unverified_context

# Load the example of dataset
iris = sns.load_dataset("iris")

# "Melt" the dataset to "long-form" or "tidy" representation
iris = pd.melt(iris, "species", var_name="measurement")

# Initialize the figure
f, ax = plt.subplots()
sns.despine(bottom=True, left=True)

# Show each observation with a scatterplot
sns.stripplot(x="value", y="measurement", hue="species",
              data=iris, dodge=True, jitter=True,
              alpha=.25, zorder=1)

# Improve the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[3:], labels[3:], title="species",
          handletextpad=0, columnspacing=1,
          loc="lower right", ncol=3, frameon=True)

plt.show()
