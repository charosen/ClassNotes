<h1>知识图谱理论篇(十五) --Neural Message Passing for Quantum Chemistry</h1>

<h2>1. 论文阅读---"Neural Message Passing for Quantum Chemistry(ICML 2017)"</h2>

参考链接：[图深度学习 Deep Learning on Graph](https://blog.csdn.net/u011748542/article/details/86540001)

<h3>1. 摘要&intro</h3>

先前论文已经提出很多对分子同构/图同构具有不变性的（图）神经网络模型，这些模型有以下特点：

1. 都有各自的**消息传播函数message passing algorithm**
2. 都有各自的**聚合函数aggregation procedure**
3. 由上述两个函数/算法构成整个输入图的函数

论文贡献：
1. 提出这些（图）模型的、高效可行的泛化变体模型（也就是框架）--MPNN，（**MPNN总结了许多现有模型的共性，以便于归纳现有模型间的关系以及发现新的模型变体**）
2. 展示了现有(图)模型与通用框架MPNN之间的关系--将图模型公式reformulate/套用进通用框架MPNN的公式
3. 在molecular property prediction任务上，探索了额外的、新奇的框架的模型变体variaitons；

<h3>2. Message Passing Neural Network模型</h3>

至少8个著名模型可以reformulate成MPNN框架形式。简单起见，论文只讨论MPNN使用于无向图G（其节点特征$x_v$和边特征$e_{vw}$）并十分容易拓展到有向多图情况；

MPNN前向传播分为两个阶段phase：

1. 消息传播阶段message passing phase：
    1. 消息函数：$m^{t+1}_v = \sum_{w \in N(v)} M_t (h^t_v, h^t_w, e_{vw})$
    2. 节点更新函数：$h^{t+1}_v = U_t (h^t_v, m^{t+1}_v)$
2. 聚合阶段readout phase/graph coarsening phase（对应传统CNN的Pooling操作）
    1. 使用某些readout函数R计算整个图的特征向量：$$\hat y = R(\{ h^T_v | v \in G \} )$$
    2. readout函数R应该对节点状态的排列组合具有不变性，以实现MPNN对图同构具有不变性；


注意，只要对图引入所有边的hidden states$h^t_{e_{vw}}$（也就是把边也转换成“边”节点），MPNN也可以使用message function和vertex update function学习边特征；

<h3> 2.1. 下面介绍现有模型与MPNN框架的关系</h3>

（现有模型使用了哪些特定的message functions，哪些特定的vertex update functions， 哪些特定的readout operations）

**Neural FP与MPNN**

convolution network for learning molecular fingerprints, Duvenaud et al.(2015)

1. 消息函数：$M(h_v, h_w, e_{vw}) = (h_w, e_{vw})$（这是某一个消息函数，还要求和才得到$m_v^{t+1}$），其中(... , ...)表示串接操作；
2. 节点更新函数：$U_t ( h^t_v, m^{t+1}_v ) = \delta ( H_t^{deg(v)} m_v^{t+1} ) $，其中deg(v)是v节点的度，Neural FP为不同度N的节点分配不同的参数矩阵$H_t^N$
3. readout操作：skip-connection

问题：Neural FP的消息传播导致$m_v^{t+1} = ( \sum h_w^t, \sum e_{vw} )$，这使得节点和边是分开求和的，不能够发现到节点状态和边状态之间的互相关

**Gated GNN与MPNN**

gated graph neural networks, Li et al.(2016)

略

**Interaction Networks与MPNN**

interaction networks, Battaglia et al.(2016)

略

**Molecular Graph Convolutions与MPNN**

Molecular Graph Convolutions, Kearnes et al.(2016)

略

**Deep Tensor Neural Networks与MPNN**

Deep Tensor Neural Networks, Schu ̈tt et al.(2017)

略

**谱图卷积与MPNN**

Laplacian Based Methods, Bruna et al. (2013); Deffer-rard et al. (2016); Kipf & Welling (2016)


Bruna et al. (2013); Defferrard et al. (2016)

1. 消息函数：$M_t ( h_v^t, h_w^t ) = C_{vw}^t h_w^t$，其中$C_{vw}^t$由图拉普拉斯矩阵的特征向量与模型参数组成；
2. 节点更新函数：$U_{t}(h_{v}^{t}, m_{v}^{t+1})=\sigma(m_{v}^{t+1})$

Kipf & Welling (2016)

1. 消息函数：$M_{t}(h_{v}^{t}, h_{w}^{t})=c_{v w} h_{w}^{t}$，其中$c_{v w}=(\operatorname{deg}(v) \operatorname{deg}(w))^{-1 / 2} A_{v w}$
2. 节点更新函数：$U_{v}^{t}(h_{v}^{t}, m_{v}^{t+1})=\operatorname{ReLU}(W^{t} m_{v}^{t+1})$


<h3>5. 针对molecular property prediction做的MPNN变体</h3>

基于baseline GG-NN模型，论文使用MPNN探索了新型的GG-NN变体，尝试了不同的message functions，output functions，寻找合适的输入表达式，以及合适的超参数

论文后续使用d表示节点隐藏表示的维度，n表示图节点个数。MPNN变体主要作用于有向图，其入向边与出向边使用分开的消息通道，即$m_v$是$m^{in}_v$和$m^{in}_w$的串接。当作用于无向图时，我们将原始边拆分成两条有相同label的入向边和出向边。

注意，边的方向是没有意义的，消息也可能沿着边的反方向传播，这里区分入向边与出向边是为了参数分类parameter typing（入向边和出向边使用不同的可学习参数矩阵），因此将无向图变成有向图时，消息通道的参数翻倍。


> The input to our MPNN model is a set of feature vectors for the nodes of the graph, $x_v$, and an adjacency matrix A with vector valued entries to indicate different bonds in the molecule as well as pairwise spatial distance between two atoms. 


**5.1. message functions**

Matrix Multiplication：GG-NN中使用的message functions$M(h_{v}, h_{w}, e_{v w})=A_{e_{v w}} h_{w}$

Edge Network：为了利用边的特征向量，我们提出一种消息函数$M(h_{v}, h_{w}, e_{v w})= A\left(e_{v w}\right) h_{w}$，其中$A(e_{v w})$是一个神经网络，将边向量映射成矩阵

Pair Message：matrix multiplication的一个属性为从节点w到节点v的信息是一个关于hidden state $h_w$与边$e_{vw}$的函数。可以发现，该函数不依赖于$h_v$。理论上，如果节点消息能够既依赖源节点又依赖目的节点，神经网络才能更高效地利用消息通道。因此，论文尝试使用Battagia et al. 2016中提到的一个message function的变体，沿着边e从点w到点v的消息可以表示为$m_{w v}=f(h_{w}^{t}, h_{v}^{t}, e_{v w})$，其中f为神经网络；

> When we apply the above message functions to directed graphs, there are two separate functions used, $M^{in}$ and an $M^{out}$. Which function is applied to a particular edge $e_{vw}$ depends on the direction of that edge.

**5.2. virtual grpah element(通过往图中添加虚拟节点或虚拟边，使得模型能够学习长依赖)**

1. 虚拟边：对没有边的两个顶点添加虚拟类型边“virtual” type edge，允许**information to travel long distances** during the propagation phase；
2. 虚拟节点--master node：这个latent master node与所有节点都用一种特殊类型的边相连。master node充当全局暂存空间，每个节点在消息传递的每个步骤中都从master node读取信息和向master node写入信息。

> We allow the master node to have a separate node dimension dmaster, as well as separate weights for the internal update function (in our case a GRU). This allows information to travel long distances during the propagation phase. It also, in theory, allows additional model capacity (e.g. large values of $d_{master}$ ) with- out a substantial hit in performance, as the complexity of the master node model is $O(|E|d^2 + nd^2_{master})$.


**5.3. readout函数**

论文测试两种readout函数

1. baseline GG-NN使用的readout函数
2. Vinyals et al. (2015)提出的set2set模型


**5.4. multiple towers（解决MPNN scalability不好的问题）**

略，详见论文
