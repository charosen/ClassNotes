#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
Paired density and scatterplot matrix.
'''

# 模块导入
# 第三方库导入
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white")


df = sns.load_dataset("iris")


g = sns.PairGrid(df, diag_sharey=False)
g.map_lower(sns.kdeplot)
g.map_upper(sns.scatterplot)
g.map_diag(sns.kdeplot, lw=3)

plt.show()
