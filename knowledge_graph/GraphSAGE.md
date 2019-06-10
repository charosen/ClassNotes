<h1>知识图谱理论篇(十六) --Neural Message Passing for Quantum Chemistry</h1>

<h2>1. 论文阅读---"Inductive Representation Learning on Large Graphs(NIPS 2017)"</h2>

参考链接：
1. [Inductive Representation Learning on Large Graphs](https://davidham3.github.io/blog/2018/07/19/inductive-representation-learning-on-large-graphs/)
2. [网络表示学习: 淘宝推荐系统&&GraphSAGE](https://zhuanlan.zhihu.com/p/44197242)

<h3>摘要</h3>

先前图模型均是transductive setting，论文提出了一个inductive的框架GraphSAGE利用顶点特征信息（比如文本属性）来高效地为没有见过的顶点生成embedding。与其为每个顶点训练单独的embedding，我们学习到一个函数，这个函数通过从一个顶点的局部邻居采样并聚合顶点特征来生成embedding。

<h3>1. intro</h3>

