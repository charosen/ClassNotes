#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
学习使用seaborn中的分布图distribution plot及其参数
'''

# 模块导入
# 第三方模块导入
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# seaborn的全局配置
sns.set(style="white", palette="muted", color_codes=True)
# 伪随机数生成器
rs = np.random.RandomState(10)

# Set up the matplotlib figure
f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
# 除去左坐标轴
sns.despine(left=True)

# Generate a random univariate(单变量的) dataset
d = rs.normal(size=100)

# Plot a simple histogram with binsize(分箱大小) determined automatically
sns.distplot(d, kde=False, color="b", ax=axes[0, 0])

# Plot a kernel density estimate（内部密度估计） and rug plot(地毯图)
sns.distplot(d, hist=False, rug=True, color="r", ax=axes[0, 1])

# Plot a filled kernel density estimate（填充的内部密度估计）
sns.distplot(d, hist=False, color="g", kde_kws={"shade": True}, ax=axes[1, 0])

# Plot a histogram and kernel density estimate
sns.distplot(d, color="m", ax=axes[1, 1])

plt.setp(axes, yticks=[])
plt.tight_layout()
plt.show()
