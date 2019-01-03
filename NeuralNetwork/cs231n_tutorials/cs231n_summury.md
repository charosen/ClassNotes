<h1 id="head">Standford CS231n 2017总结</h1>

<h2 id="table_of_content">目录</h2>

+ [Standford CS231n 2017 总结](#head)
    + [目录](#table_of_content)
    + [02. 图像分类](#chapter2)

<h2 id="chapter2">02. 图像分类</h2>

1. 图像分类问题面临的挑战：视角变幻Viewpoint variation、光照条件Illumination conditions、变形Deformation、遮挡Occlusion、背景干扰Background clutter、类内差异Intraclass variation...

    1. ![](media/15465245417516.jpg)

2. **最近邻算法**--解决图像分类：使用训练数据集中距离输入图像最近的图像的类别标签作为输入图像的分类；
    1. 最近邻算法的超参数：距离度量
    2. 最近邻算法的时间复杂度：训练O(1)，预测O(N)
3. **K近邻算法**--解决图像分类：使用训练数据集中距离输入图像最近的k个图像的类别标签的majority vote作为输入图像的分类；
    1. K邻算法的超参数：距离度量和邻居数K；
    2. 距离度量可以是：
        1. L2距离（欧几里得距离）：Best for non coordinate points；
        2. L1距离（曼哈顿距离）：Best for coordinate points；
4. 超参数优化方法：
    1. 大数据集、复杂深度模型：将数据分成训练集、验证集、测试集，在训练集上训练模型，在验证集上选择超参数；
    2. 小数据集、简单网络模型：使用交叉验证；
