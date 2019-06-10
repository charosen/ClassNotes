<h1>知识图谱理论篇(十三) --Graph Neural Network 综述</h1>

<h2>1. 论文阅读---"Deep Learning on Graphs: A Survey"</h2>

论文总结链接：
1. [深度学习时代的图模型，清华发文综述图网络](https://mp.weixin.qq.com/s/WW-URKk-fNct9sC4bJ22eg)
2. [图深度学习 Deep Learning on Graph](https://blog.csdn.net/u011748542/article/details/86540001)

GCN论文汇总：<https://davidham3.github.io/blog/2018/07/23/gcn%E8%AE%BA%E6%96%87%E6%B1%87%E6%80%BB/#more>


abstract、intro、gnn综述，直接略过，主要是想了解GCN的发展

<h3>4. GCN的综述</h3>

**4.1.1. 谱方法**

先介绍了图傅立叶变换、谱图理论、图谱卷积，请参考[之前的谱图理论小结](https://github.com/charosen/ClassNotes/blob/master/knowledge_graph/cnn_on_graph_fast_localized_spectral_filtering.md)

Spectral Networks and Deep Locally Connected Networks on Graphs提出卷积核：$$\begin{aligned} g_\theta(\land) = \left(\begin{array}{ccc} \theta_0 &\\ &\ddots &\\ &&\theta_{N-1} \end{array}\right) \end{aligned}$$，上述卷积核的学习复杂度为O(n)，论文作出了改进--光滑卷积核(没看懂)：$$diag(\Theta^l_{i, j}) = \kappa \alpha_{l,i,j}$$

+ $\kappa$示固定的插值核
+ $\alpha_{l,i,j}$是需学习的插值系数：

第一代GCN存在两方面问题：
1. 卷积复杂度、计算复杂度高，为$O(n^2)$
2. 图卷积依赖图拉普拉斯矩阵的特征向量基，导致参数不能在多个具有不同sizes和结构的图上共享（不能用在别的图上）；

所以后续图卷积研究方向分成两条线进行，分别关注解决上述两个问题之一；

**4.1.2 Efficiency Aspect -- 解决复杂度方向**

[知识图谱理论篇(十一) --论文阅读Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering](https://github.com/charosen/ClassNotes/blob/master/knowledge_graph/cnn_on_graph_fast_localized_spectral_filtering.md)使用
1. 多项式参数化图卷积核，实现严格局部化的图卷积
2. 切比雪夫多项式近似多项式，降低计算复杂度至$O(K|E|)$

Kipf和Welling提出的[知识图谱理论篇(十二) --论文阅读SEMI-SUPERVISED CLASSIFICATION WITH GRAPH CONVOLUTIONAL NETWORKS](https://github.com/charosen/ClassNotes/blob/master/knowledge_graph/semi_supervised_classification_GCN.md)只使用一阶邻居进行快速的、近似的图卷积$$ h^{(l+1)}_{i} = \sigma ( \sum_{j \in N(i)} \frac{ \tilde{A}_{i,j}}{ \tilde{D}^{- \frac{1}{2}}_{i,i} \tilde{D}^{- \frac{1}{2}}_{j,j}} h^{(l)}_j W^{(l)})$$，矩阵形式为$$ H^{(l+1)} = \sigma(\tilde{D}^{-\frac{1}{2}} \tilde{A} \tilde{D}^{-\frac{1}{2}} H^{(l)} W^{(l)})$$，通过堆叠多个这样的卷积层，而实现k阶邻居的局部卷积；

**上述两篇论文的方法将谱域GCN以及空域GCN联系起来。**

**4.1.3. Multiple Graphs Aspect -- 解决在一个图上训练的模型应用到异构图（基本上都是空域spatial domain模型）**

**Neural FP**使用一阶邻居计算空域卷积$$ h^{(l+1)}_{i} = \sigma ( \sum_{j \in N(i)} h^{(l)}_j W^{(l)})$$，卷积参数$W^{(l)}$可以在不同图中共享且独立于图的大小，注意，Neural FP与Kipf&Welling提出的方法很相似，不同的是Neural FP不添加归一化来考虑节点的度的影响；（可以参考[如何理解 Graph Convolutional Network（GCN）？中纵横的回答](https://www.zhihu.com/question/54504471/answer/332657604)，Neural FP更像是求和聚合邻居节点的信息，而Kipf&Welling更像是几何平均聚合邻居节点的信息）；

Neural FP可以为不同度的节点分别学习不同的参数$W^{(l)}$，例如$W^{(l)}_1, W^{(l)}_2, ...$且Neural FP在小图上训练效果比较好；

**PATCHY-SAN**采用了不同的思想，使用图标注流程graph labeling procedure(例如，Weisfeiler-Lehman kernel)来分配一个独特的/唯一的节点顺序，接着，按照这个预定义的顺序将节点拍成一行，并从节点的k跳邻居中中选择固定数目的顶点，然后使用标准的1-D CNN处理（**本质，将图数据特征转换成特定一维顺序的节点特征，并用1-D CNN来学习特征**）。

**DCNN--Diffusional CNN** 使用扩散过程的特征向量基替代卷积中的特征向量基，即节点的可接受域receptive field是通过节点间的扩散转移概率diffusion transition probability确定。 $P^K$是长度为K的扩散过程的转移慨率，比如随机游走，此时卷积定义为(公式好像有问题)：$$H^{l+1} = \delta( P^K H^l \Theta^l)$$

请参考[DCNN笔记](https://github.com/charosen/ClassNotes/blob/master/knowledge_graph/dcnn.md)

DGCN 将扩散和邻接机制融合，使用对偶图卷积网络，有两种卷积，一类如Kipf&Welling公式，另一类使用转移概率的 positive 逐点互信息(PPMI)矩阵$X_P$替换邻接矩阵,$D_P(i,i)=\sum_{j\neq i}X_P(i,j)$:
$$Z^{l+1}=\rho(D^{-\frac{1}{2}}_PX_PD^{-\frac{1}{2}}_PZ^l\Theta^l)$$


**4.1.4. 通用框架**

基于4.1.2与4.1.3中的两项工作，MPNN为多种图模型提供了统一框架，其消息传播函数如下：$$\begin{array}{c}{\mathbf{m}_{i}^{l+1}=\sum_{j \in \mathcal{N}(i)} \mathcal{F}^{l}\left(\mathbf{h}_{i}^{l}, \mathbf{h}_{j}^{l}, \mathbf{F}_{i, j}^{E}\right)} \\ {\mathbf{h}_{i}^{l+1}=\mathcal{G}^{l}\left(\mathbf{h}_{i}^{l}, \mathbf{m}_{i}^{l+1}\right)}\end{array}$$

从概念上讲，**MPNN** 提出的框架，每个节点根据其状态发送消息，并根据从直接邻域顶点收到的消息更新其状态。同时添加一个“主”节点，该节点连接到所有节点以加速长距离时的消息传递，并且通过划分hidden representation到不同towers来提升模型泛化能力，详情请参考[知识图谱理论篇(十五) --Neural Message Passing for Quantum Chemistry](https://github.com/charosen/ClassNotes/blob/master/knowledge_graph/MPNN.md)。

**GraphSAGE** 采用了多聚合函数与上述方法类似：$$
\begin{array}{c}{m_{i}^{l+1}=A G G R E G A T E^{l}\left(\left\{h_{i}^{l}, \forall j \in \mathcal{N}(i\}\right)\right.} \\ {h_{i}^{l+1}=\rho\left(\Theta^{l}\left[h_{i}^{l}, m_{i}^{l+1}\right]\right)}\end{array}
$$给出了三个建议的聚合函数：

+ element-wise mean
+ LSTM
+ pooling$A G G R E G A T E^{l}=\max \left\{\rho\left(\Theta_{p o o l} h_{j}^{l}+b_{p o o l}\right), \forall j \in \mathcal{N}(i)\right\}$

**Mixture Model Network (MoNet)** 尝试使用template matching将GCN和CNN先前的工作整合到一个统一框架。$$
\begin{array}{l}{h_{i k}^{l+1}=\sum_{j \in \mathcal{N}(i)} \mathcal{F}_{k}^{l}(u(i, j)) h_{j}^{l}, k=1, \cdots, f_{l+1}} \\ {\mathcal{F}_{k}^{l}(u)=\exp \left(-\frac{1}{2}\left(u-\mu_{k}^{l}\right)^{T}\left(\Sigma_{k}^{l}\right)^{-1}\left(u-\mu_{k}^{l}\right)\right)} \\ {u(i, j)=\left(D(i, i)^{-\frac{1}{2}}, D(j, j)^{-\frac{1}{2}}\right)}\end{array}
$$

Graph Network (GNs) 给出了一个对GCNs和GNNs都通用更为一般的框架，学习图上三个集合的表示：顶点，边和图$h_{i}^{l}, e_{i j}^{l}, z^{l}$：$$
\begin{aligned} m_{i}^{l} &=\mathcal{G}^{E \rightarrow V}\left(\left\{h_{j}^{l}, \forall j \in \mathcal{N}(i)\right\}\right) \\ m_{V}^{l} &=\mathcal{G}^{V \rightarrow G}\left(\left\{h_{j}^{l}, \forall v_{i} \in V\right\}\right) \\ m_{E}^{l} &=\mathcal{G}^{E \rightarrow G}\left(\left\{h_{i j}^{l}, \forall\left(v_{i}, v_{j}\right) \in E\right\}\right) \\ h_{i}^{l+1} &=\mathcal{F}^{V}\left(m_{i}^{l}, h_{i}^{l}, z^{l}\right) \\ e_{i j}^{l+1} &=\mathcal{F}^{E}\left(e_{i j}^{l}, h_{i}^{l}, h_{i}^{l}, z^{l}\right) \\ z^{l+1} &=\mathcal{F}^{G}\left(m_{E}^{l}, m_{V}^{l}, z^{l}\right) \end{aligned}
$$

**总结**，图卷积运算的发展趋势为从谱域演变为空间域，并且从多步邻域顶点演变为直接邻域顶点。

**4.2. readout操作**

通过卷积操作，可以学习到节点有价值的特征，这些特征主要用于解决针对节点的任务。为了进一步处理面向图的任务，获取的顶点信息需要聚合为图级别的表示。在文献中，这称为Readout或图粗化操作，这个问题并不是可以直接套用的，因为传统CNN中带步长的卷积stride conv或者池化操作在非网格结构下不能直接使用。

**序列不变性。**图Readout操作的一个关键条件时节点的序列不变性，即构建一个双射将原图中的节点和边投影为新生成的图的点和边，但是在投影后的图上学得的图表示与前者相同。例如，一个药物是否能够治疗某种疾病应该独立于药物以何种形式表示成图。注意，因为图同构问题是一个NP问题，因此我们只能在多项式时间复杂度级别上找到一个序列不变性（图同构，表示相同）的函数，但是反之不一定满足，即不同构的图也存在相同的表示。

**4.2.1. 统计运算**

具有序列不变性的基础运算即一些简单的统计运算，例如求和、求平均、max-pooling等

$$
\mathbf{h}_{G}=\sum_{i=1}^{N} \mathbf{h}_{i}^{L} \text { or } \mathbf{h}_{G}=\frac{1}{N} \sum_{i=1}^{N} \mathbf{h}_{i}^{L} \text { or } \mathbf{h}_{G}=\max \left\{\mathbf{h}_{i}^{L}, \forall i\right\}
$$

但是上述统计运算的表示能力不足以表示整个图，相关文献也提出了使用fuzzy histogram来统计节点表示的分布。

另一个方法是使用全连接层做模型最后一层$$
\mathbf{h}_{G}=\Theta_{F C} \mathbf{H}^{L}
$$，全连接层可以是作节点特征的加权求和，其优点在于模型可以为不同节点学习不同的权重，缺点在于不能保证序列不变性


**4.2.2 hierarchical
 clustering**
 
 后续补充

**4.2.3 其他方法**

后续补充



















