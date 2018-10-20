#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
Linear regression with marginal distributions
'''

# 模块导入
# 标准库导入
# import ssl
# 第三方库导入
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid")


tips = sns.load_dataset("tips")
g = sns.jointplot("total_bill", "tip", data=tips, kind="reg",
                  xlim=(0, 60), ylim=(0, 12), color="m", height=7)

plt.show()
