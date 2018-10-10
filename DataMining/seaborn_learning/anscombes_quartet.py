#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
安斯库姆四重奏（Anscombe's quartet）是四组基本的统计特性一致的数据，但由它们
绘制出的图表则截然不同。每一组数据都包括了11个(x,y)点。这四组数据由统计学家
弗朗西斯·安斯库姆（Francis Anscombe）于1973年构造，他的目的是用来说明在分析
数据前先绘制图表的重要性，以及离群值对统计的影响之大。
'''
# 导入模块：
# 标准库导入：
import ssl
import matplotlib.pyplot as plt
# 第三方库导入：
import seaborn as sns


ssl._create_default_https_context = ssl._create_unverified_context

sns.set(style="ticks")

# Load the example dataset for Anscombe's quartet
df = sns.load_dataset("anscombe")
# print(df)

# Show the results of a linear regression within each dataset
sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
           col_wrap=2, ci=None, palette="muted", height=4,
           scatter_kws={"s": 50, "alpha": 1})

# Show plot
plt.show()
