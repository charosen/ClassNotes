#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
学习使用seaborn中的FacetGrid, 使用分面格子FacetGrid并定制每个格子的投影方式
FacetGrid with custom projection.

FacetGrid应该是seaborn对matplotlib.pyplot的subplots的封装？
'''

# 模块导入
# 第三方模块导入
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# seaborn global configuration
sns.set()

# Generate an example radial(辐射状) dataset
r = np.linspace(0, 10, num=100)
df = pd.DataFrame({'r': r, 'slow': r, 'medium': 2*r, 'fast': 4 * r})
print(df)

# Convert the dataframe to long-form or "tidy" format
df = pd.melt(df, id_vars=['r'], var_name='speed', value_name='theta')
print(df)

# Set up a grid of axes with a polar projection(极坐标？)
g = sns.FacetGrid(df, col="speed", hue="speed",
                  subplot_kws=dict(projection='polar'), height=4.5,
                  sharex=False, sharey=False, despine=False)

# Draw a scatterplot onto each axes in the grid
g.map(sns.scatterplot, "theta", "r")

plt.show()
