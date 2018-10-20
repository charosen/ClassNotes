#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
学习使用seaborn画核密度估计图kernel density estimate,
Joint kernel density estimate
'''

# 模块导入
# 第三方库导入
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# seaborn global setting
sns.set(style="white")

# Generate a random correlated bivariable（双变量的） dataset
rs = np.random.RandomState(5)
mean = [0, 0]
cov = [(1, .5), (.5, 1)]
x1, x2 = rs.multivariate_normal(mean, cov, 500).T
x1 = pd.Series(x1, name="$X_1$")
x2 = pd.Series(x2, name="$X_2$")

# Show the joint distribution using kernel density estimation
g = sns.jointplot(x1, x2, kind="kde", height=7, space=0)

plt.show()
