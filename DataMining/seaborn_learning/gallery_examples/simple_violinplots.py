#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
Violinplots with observations
'''

# 模块导入
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

# Create a random dataset across several variables
rs = np.random.RandomState(0)
n, p = 40, 8
d = rs.normal(0, 2, (n, p))
d += np.log(np.arange(1, p + 1)) * -5 + 10

# Use cubehelix to get a custom sequential palette
pal = sns.cubehelix_palette(p, rot=-.5, dark=.3)

# Show each distribution with both violins and points
sns.violinplot(data=d, palette=pal, inner="points")

plt.show()
