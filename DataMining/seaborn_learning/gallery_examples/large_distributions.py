#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
Plotting large distributions
'''

# 模块导入
# 标准库导入
import ssl
# 第三方库导入
import seaborn as sns
import matplotlib.pyplot as plt

# seaborn global settings
sns.set(style="whitegrid")
ssl._create_default_https_context = ssl._create_unverified_context

diamonds = sns.load_dataset("diamonds")
clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]

sns.boxenplot(x="clarity", y="carat",
              color="b", order=clarity_ranking,
              scale="linear", data=diamonds)

plt.show()
