#!/usr/bin/env python3
# -*-coding: utf-8 -*-

# 模块字符串
'''
学习使用seaborn中的cubehelix调色板cubehelix colormap, 使用seaborn中的
cubehelix_palette方法
'''

# 模块导入
# 标准库导入
# import ssl
# 第三方库导入
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ssl._create_default_https_context = ssl._create_unverified_context

sns.set(style="dark")
rs = np.random.RandomState(50)

# Set up the matplotlib figure
f, axes = plt.subplots(3, 3, figsize=(9, 9), sharex=True, sharey=True)

# Rotate the starting poing around the cubehelix hue circle
for ax, s in zip(axes.flat, np.linspace(0, 3, 10)):

    # Create a cubehelix colormap to use with kdeplot:
    cmap = sns.cubehelix_palette(start=s, light=1, as_cmap=True)

    # Generate and plot a random bivariate dataset
    x, y = rs.randn(2, 50)
    sns.kdeplot(x, y, cmap=cmap, shade=True, cut=5, ax=ax)
    ax.set(xlim=(-3, 3), ylim=(-3, 3))


f.tight_layout()

plt.show()
