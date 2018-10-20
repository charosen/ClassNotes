#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
学习使用seaborn的hexbin plot, 并带有边缘分布marginal distributions
'''

# 模块导入
# 第三方模块导入
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# seaborn global settins
sns.set(style="ticks")

# 伪随机数生成器
rs = np.random.RandomState(11)
x = rs.gamma(2, size=1000)
y = -.5 * x + rs.normal(size=1000)

sns.jointplot(x, y, kind="hex", color="#4CB391")

plt.show()
