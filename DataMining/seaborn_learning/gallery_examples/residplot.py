#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
Plotting model residuals
'''

# 模块导入
# 第三方库导入
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

# Make an example dataset with y~x
rs = np.random.RandomState(7)
x = rs.normal(2, 1, 75)
y = 2 + 1.5 * x + rs.normal(0, 2, 75)


# Plot the residuals after fitting a linear model
sns.resiplot(x, y, lowess=True, colort="g")
