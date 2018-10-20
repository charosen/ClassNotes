#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
Scatterplot with varying points sizes and hues
'''

# 模块导入
import ssl

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white")
ssl._create_default_https_context = ssl._create_unverified_context

# Load the example mpg dataset
mpg = sns.load_dataset("mpg")

# Plot miles per gallon against horsepower with other semantics
sns.relplot(x="horsepower", y="mpg", hue="origin", size="weight",
            sizes=(40, 400), alpha=.5, palette="muted",
            height=6, data=mpg)

plt.show()
