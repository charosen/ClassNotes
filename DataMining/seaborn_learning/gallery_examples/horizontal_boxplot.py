#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
学习使用seaborn中的水平盒图Horizontal boxplot，并显示出观测值，也就是数据点
Horizontal boxplot with observations
'''

# 模块导入
# 标注库导入
import ssl
# 第三方库导入
import seaborn as sns
import matplotlib.pyplot as plt

# seaborn global settings
sns.set(style="ticks")
# urllib's ssl cert settings
ssl._create_default_https_context = ssl._create_unverified_context

# Initialize the figure with a logarithmic(对数的) x axis
f, ax = plt.subplots(figsize=(7, 6))
ax.set_xscale("log")

# Load the example planets dataset
planets = sns.load_dataset("planets")

# Plot the orbital(轨道的) period with horizontal boxes
sns.boxplot(x="distance", y="method", data=planets,
            whis="range", palette="vlag")

# Add in points to show each observation(观测量，即数据值)
sns.swarmplot(x="distance", y="method", data=planets,
              size=2, color=".3", linewidth=0)

# Tweak the visual presentation
ax.xaxis.grid(True)
ax.set(ylabel="")
sns.despine(trim=True, left=True)

plt.show()
