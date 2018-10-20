#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
Multiple linear regression.
'''

# 模块导入
# 标准库导入
# import ssl
# 第三方库导入
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

# Load the iris dataset
iris = sns.load_dataset("iris")

# Plot sepal with as a function of sepal_length across days
g = sns.lmplot(x="sepal_length", y="sepal_width", hue="species",
               truncate=True, height=5, data=iris)

# Use more informative axis labels than are provided by default
g.set_axis_labels("Sepal length(mm)", "Sepal width(mm)")

plt.show()
