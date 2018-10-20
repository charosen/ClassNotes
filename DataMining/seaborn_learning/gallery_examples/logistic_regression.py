#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块字符串
'''
Faceted logistic regression
'''

# 模块导入
# 标准库导入
import ssl
# 第三方库导入
import seaborn as sns
import matplotlib.pyplot as plt

# seaborn global setting
sns.set(style="darkgrid")
ssl._create_default_https_context = ssl._create_unverified_context

# Load the example titanic dataset
df = sns.load_dataset("titanic")

# Make a custom palette with gendered colors
pal = dict(male='#6495ed', female='#F08080')

# Show the survival probability as a function of age and sex
g = sns.lmplot(x="age", y="survived", col="sex", hue="sex", data=df,
               palette=pal, y_jitter=.02, logistic=True)

g.set(xlim=(0, 80), ylim=(-.05, 1.05))

plt.show()
