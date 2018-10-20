#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
Scatterplot with marginal ticks
'''

# 模块导入
# 第三方库导入
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white", color_codes=True)

# Generate a random bivariable dataset
rs = np.random.RandomState(9)
mean = [0, 0]
cov = [(1, 0), (0, 2)]
x, y = rs.multivariate_normal(mean, cov, 100).T

# Use JointGrid directly to draw a custom plot
grid = sns.JointGrid(x, y, space=0, height=6, ratio=50)
grid.plot_joint(plt.scatter, color="g")
grid.plot_marginals(sns.rugplot, height=1, color="g")

plt.show()
