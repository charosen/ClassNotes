<h1>知识图谱理论篇(十四) --Diffusion-Convolutional Neural Network</h1>

<h2>1. 论文阅读---"Diffusion-Convolutional Neural Network(NIPS 2016)"</h2>

参考链接：
1. [论文笔记之Diffusion-Convolutional Neural Networks](https://blog.csdn.net/bvl10101111/article/details/54343310)
2. [Diffusion-Convolutional Neural Networks （传播-卷积神经网络）](https://www.cnblogs.com/wangxiaocvpr/p/8763510.html)
3. [Diffusion-Convolutional Neural Networks](https://davidham3.github.io/blog/2018/07/19/diffusion-convolutional-neural-networks/)

<h3>1. 摘要&intro</h3>

论文提出DCNN模型(Diffusional Convolutional Neural Network)。通过diffusion convolution操作，DCNN模型直接从图数据（有结构的数据）中编码graph diffusion信息（graph diffusion可以表示成方阵幂级数，其蕴含了节点的邻居上下文信息）以学习得到diffusion-based表示

DCNN存在以下特性：

1. **diffusion representation对于同构图具有不变性；**
2. 预测的时间复杂度为多项式级别；
3. 训练过程可以在GPU上使用张量操作并行实现；


DCNN优势：

+ 精度：DCNN比其他方法在顶点分类任务上精度更高，图分类上表现的也不错。
+ 灵活性：DCNN提供了图数据的灵活表示，使用简单的处理对顶点特征、边特征以及结构信息进行编码。DCNN可以用于很多分类任务，包括顶点分类，边分类，图分类。
+ 速度：DCNN的预测可以表示成一系列多项式时间复杂度的tensor操作，模型可以在GPU上实现。

<h3>2. 模型</h3>

模型解读参考[Diffusion-Convolutional Neural Networks](https://davidham3.github.io/blog/2018/07/19/diffusion-convolutional-neural-networks/)

Note：
1. GCN、DCNN的权值共享体现在同一跳的同一个feature权值一样（共享）
2. 图卷积是邻居深度层面上共享参数，传统卷积是网格内位置上的共享参数

<h3>3. 实验</h3>

参考论文
