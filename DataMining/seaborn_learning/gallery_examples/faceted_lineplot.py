#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
Line plots on multiple facets.
'''

# 模块导入
# 标准库导入
import ssl
# 第三方库导入
import seaborn as sns
import matplotlib.pyplot as plt

# seaborn global configuration
sns.set(style="ticks")
# urllib's ssl cert configuration
ssl._create_default_https_context = ssl._create_unverified_context

# Load dataset
dots = sns.load_dataset("dots")

# Define a palette to ensure that colors will be
# shared across the facets
palette = dict(zip(dots.coherence.unique(),
                   sns.color_palette("rocket_r", 6)))
print(dots.coherence.unique())

# Plot the lines on two facets
sns.relplot(x="time", y="firing_rate",
            hue="coherence", size="choice", col="align",
            size_order=["T1", "T2"], palette=palette,
            height=5, aspect=.75, facet_kws=dict(sharex=False),
            kind="line", legend="full", data=dots)

plt.show()
