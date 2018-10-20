#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
scatterplot matrix
'''

# 模块导入
# import ssl

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="ticks")

df = sns.load_dataset("iris")
sns.pairplot(df, hue="species")

plt.show()
