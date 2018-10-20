#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
学习使用seaborn的线图line plot，Timeseries plot with error bands
'''

# 模块导入
# 标准库导入
import ssl
# 第三方库导入
import seaborn as sns
import matplotlib.pyplot as plt

# seaborn全局配置
sns.set(style="darkgrid")
# 配置urllib的ssl证书
ssl._create_default_https_context = ssl._create_unverified_context

# Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")

# Plot the response for different events and regions
sns.lineplot(x="timepoint", y="signal",
             hue="region", style="event",
             data=fmri)

plt.show()
