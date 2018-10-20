#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
Scatterplot with continuous hues and sizes.
'''

# 模块导入
import ssl

import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
ssl._create_default_https_context = ssl._create_unverified_context

# Load the example iris dataset
planets = sns.load_dataset("planets")

cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
ax = sns.scatterplot(x="distance", y="orbital_period",
                     hue="year", size="mass",
                     palette=cmap, sizes=(10, 200),
                     data=planets)

plt.show()
