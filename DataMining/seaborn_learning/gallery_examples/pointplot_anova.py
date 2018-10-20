#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
plotting a three-way ANOVA
'''

# 模块导入
import ssl

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
ssl._create_default_https_context = ssl._create_unverified_context

# Load the example exercise dataset
df = sns.load_dataset("exercise")

# Draw a pointplot to show pulse as a function of three categorical factors
g = sns.catplot(x="time", y="pulse", hue="kind", col="diet",
                capsize=.2, palette="YlGnBu_d", height=6, aspect=.75,
                kind="point", data=df)

g.despine(left=True)

plt.show()
