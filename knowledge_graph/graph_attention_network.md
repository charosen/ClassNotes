<h1>知识图谱理论篇(十三) --论文阅读GRAPH ATTENTION NETWORKS</h1>

<h2>1. 论文阅读---“GRAPH ATTENTION NETWORKS”(ICLR 2018)</h2>

<h3>0. abstract</h3>

1. 提出**图注意力网络graph attention networks**，该网络直接**作用于图**结构**数据**，利用**自注意力层使得节点会自注意其所有邻居节点特征**，解决基于图卷积或图卷积近似的先前模型的缺点；
2. 通过堆叠层（层内节点会自注意其所有邻居节点特征），我们可以为邻居中的不同节点分配不同权重，且无需进行大量计算，无需提前知晓图结构；
3. 这样，GAT同时解决了基于谱方法的GNN的多项关键挑战，且GAT可用于inductive，或者transductive问题（inductive, transductive?）

<h3>1. introduction</h3>

1. CNN在处理欧式数据/网格数据，许多任务上性能多么多么好，但是不能处理非欧数据
2. 图神经网络GNN的发展
    1. 早期的工作使用RNN来学习**有向无环图**的特征表示。2005 年和 2009 年提出了 GNN（Graph Neural Networks），作为 RNN 的泛化，可以直接处理更一般的图结构，比如**有环图、有向图、无向图**。GCN 包含了一个迭代过程，迭代时节点状态向前传播直至稳态equilibrium，后面使用一个神经网络来依据节点状态产生节点输出。Li et al., 2016使用了Cho et al., 2014提出的门控循环单元进行改进。
3. 图卷积网络GCN的发展--将卷积应用于图数据
    1. 基于普方法的GCN
        1. 第一代GCN Bruna et al. (2014),--通过图拉普拉斯矩阵特征分解来定义谱域图卷积，需要大量计算与卷积核非空间局部
        2. 第二代GCN Defferrard et al. (2016) --使用切比雪夫多项式近似图卷积核，无需计算拉普拉斯特征分解，且卷积核空间局部化
        3. Kipf & Welling (2017) -- 使用切比雪夫**一阶**多项式近似图卷积/对一跳邻居作卷积，并通过堆叠多层卷积层，实现输入空间上k跳邻居卷积
        4. **谱方法缺点：卷积核依赖于图拉普拉斯特征向量基，即需要提前知道图拉普拉斯矩阵，即本质上需要提前知道图结构。因此，在特定结构的图上训练的模型无法直接应用于不同结构的图数据**
    2. 基于非普方法的GCN
        1. 非谱方法 (Duvenaud et al., 2015; Atwood & Towsley, 2016; Hamilton et al., 2017)方法直接在图上定义卷积操作，卷积操作于一组组空间接近的邻居节点。**非普方法的关键挑战是需要定义一个能处理不同数量邻居的卷积操作，并且保证 CNN 权重共享的性质。**在某些情况下，这需要为每个 node degree 学习一个权重矩阵 (Duvenaud et al., 2015)，在对每个 input channel 和 neighborhood degree 训练权重时，使用转移矩阵的幂定义邻居 (Atwood & Towsley, 2016)，或是对有着固定数量顶点的邻居进行提取和归一化(Niepert et al., 2016)。Monti et al., 2016提出了混合模型 CNN，(MoNet)，这个空间方法提供了一个 CNN 在图上泛化的统一的模型。最近，Hamilton et al., 2017提出了 GraphSAGE，对每个顶点采样采出一个固定数量的邻居，然后使用一个指定的聚合操作聚集他们（比如取所有采样邻居的均值，或是将他们放进RNN后产生的结果）。这个方法在几个大规模的 inductive 数据集上获得了很惊人的效果。
    3. 注意力机制
        1. 注意力机制在很多基于序列的任务中已经成为了一个标准 (Bahdanau et al., 2015; Gehring et al., 2016)。注意力机制的一个好处是可以处理变长输入，专注于输入中最相关的部分来做决策。使用注意力机制计算一个序列的表示时，一般提到的是 self-attention 或 intra-attention。与 RNN 或卷积一起使用时，self-attention 在机器阅读(Cheng et al., 2016)和学习句子表示(Lin et al., 2017)这些任务上很有用。然而，Vaswani et al., 2017的研究表明，self-attention 不仅可以提升 RNN 和卷积的模型，在机器翻译任务上也是可以构建出性能最强的模型的。
    4. 论文贡献
        1. 提出了基于attention的模型GAT对图结构的顶点进行分类。核心思想是使用self-attention机制，通过对顶点邻居的自注意，计算图中每个顶点的表示。
        2. GAT高效--可并行计算多个“顶点-邻居”对；
        3. GAT，通过对邻居指定任意的权重，可以在有着不同度的顶点上使用；
        4. **模型可以直接应用在 inductive learning 任务上**，包括模型必须要生成完整的未见过的图generalize to completely unseen graphs等任务；
        5. 在4个benchmark上验证了GAT：Cora，Citeseer，Pubmed citation networks，protein-protein interaction，获得了比肩 state-of-the-art 的结果，**展现了基于 attention的模型在处理任意结构的图的可能性**。
    
值得注意的是，如 Kipf & Welling 2017和Atwood & Towsley 2016，我们的工作可以重写为 MoNet(Monti et al., 2016)的一种特殊形式。除此以外，我们在边上共享分享神经网络计算的方法让人联想到关系网络(Santoro et al., 2017)和VAIN(Hoshen, 2017)的公式，在这两篇文章中，通过使用一种共享机制，object或agent间的关系被聚合成对，。相似地，GAT模型可以联系到 Duan et al., 2017 和 Denil et al., 2017 的工作，他们使用一个邻居注意力操作来计算一个环境中不同object的注意力系数。其他相关的方法包括局部线性嵌入(LLE)(Roweis & Saul, 2000)和记忆网络(Weston et al., 2014)。LLE 在每个数据点选择了固定数量的邻居，为每个邻居学习了权重系数，以此将每个数据点重构为邻居的加权之和。之后的优化提取了顶点嵌入的特征。记忆网络与我们的工作也有关系，如果我们将一个顶点的邻居解释为记忆，通过注意它的值可以计算顶点特征，之后通过在同样的位置存储新特征进行更新。

    
<h3>2. 图注意力网络架构GAT</h3>

**图注意力层graph attention layer**

输入是一组顶点特征${\mathbf{h}} = \lbrace \vec{h}_1, \vec{h}_2, …, \vec{h}_N \rbrace , \vec{h}_i \in \mathbb{R}^F$，其中 𝑁 是顶点数，𝐹 是每个顶点的特征数；输出为新（维度可能不同）顶点特征${\mathbf{h}’} = \lbrace \vec{h}’_1, \vec{h}’_2, …, \vec{h}’_N\rbrace , \vec{h}’_i \in \mathbb{R}^{F’}$

为了在将输入特征变换到高维特征时获得充足的表现力，至少需要一个可学习的线性变换。为了到达这个目的，每个顶点都会使用一个共享参数的线性变换，参数为${\mathbf{W}} \in \mathbb{R}^{F’ \times F}$。然后在每个顶点上做一个 self-attention ——一个共享的attention机制$a : \mathbb{R}^{F’} \times \mathbb{R}^{F’} \rightarrow \mathbb{R}$来计算注意力系数 attention coefficients：$$\tag{1} e_{ij} = a(\mathbf{W} \vec{h}_i, \mathbf{W} \vec{h}_j)$$

表示顶点j的特征对顶点i的重要性(importance)。在最一般的公式中，模型可以使每个顶点都注意其他所有顶点（与所有节点都存在边/注意力系数），扔掉所有的图结构信息。我们使用mask attention使得图结构可以注入到注意力机制中——我们只对顶点$j \in \mathcal{N_i}$计算$e_{ij}$，其中$\mathcal{N_i}$是顶点i在图中的一些邻居。在我们所有的实验中使用i的一阶邻居（包括i自身）。为了让系数在不同的顶点都可比(**归一化，在统一尺度下衡量系数的影响力**)，我们对所有的j使用 softmax 进行了归一化：$$\tag{2} \alpha_{ij} = \mathrm{softmax}_j (e_{ij}) = \frac{\exp{e_{ij}}}{\sum_{k \in \mathcal{N}_i} \exp{e_{ik}}}$$

![](media/15585788859123.jpg)

在我们的实验中，注意力机制a是一个单层的前向传播网络，参数为权重向量$\vec{\text{a}} \in \mathbb{R}^{2F’}$，使用LeakyReLU作为非线性层（斜率𝛼=0.2）。整个合并起来，注意力机制计算出的系数（如图1左侧所示）公式为：$$\tag{3} \alpha_{ij} = \frac{ \exp{ ( \mathrm{LeakyReLU} ( \vec{\text{a}}^T [\mathbf{W} \vec{h}_i \Vert \mathbf{W} \vec{h}_j ] ))}}{\sum_{k \in \mathcal{N_i}} \exp{(\mathrm{LeakyReLU}(\vec{\text{a}}^T [\mathbf{W} \vec{h}_i \Vert \mathbf{W} \vec{h}_k]))}}$$

其中$·^T$表示转置，||表示concatenation操作。

得到归一化的分数后，使用归一化的注意力系数计算对应特征的线性组合，作为每个顶点最后的输出特征（最后可以加一个非线性层，$\sigma$）：$$\tag{4} \vec{h}’_i = \sigma(\sum_{j \in \mathcal{N}_i} \alpha_{ij} \mathbf{W} \vec{h}_j)$$

为了稳定 self-attention 的学习过程，我们发现使用 multi-head attention 来扩展我们的注意力机制是很有效的，就像 Vaswani et al., 2017。特别地，K个独立的 attention 机制执行 式4 这样的变换，然后他们的特征连(concatednated)在一起，就可以得到如下的输出：$\tag{5} \vec{h}’_i = \Vert^{K}_{k=1} \sigma(\sum_{j \in \mathcal{N}_i} \alpha^k_{ij} \mathbf{W}^k \vec{h}_j)$

其中||表示concatenation，$\alpha^k_{ij}$是通过第 k个注意力机制$(a^k)$计算出的归一化的注意力系数，$\mathbf{W}^k$是对应的输入线性变换的权重矩阵。注意，在这里，最后的返回输出$\mathbf{h}’$，每个顶点都会有$KF’$个特征（不是$F’$）。

特别地，如果我们在网络的最后一层使用 multi-head attention，concatenation 就不再可行了，我们会使用 averaging，并且在averaging之后再使用最后的非线性层（分类问题通常是 softmax 或 sigmoid ）：$$\vec{h}’_i = \sigma(\frac{1}{K} \sum^K_{k=1} \sum_{j \in \mathcal{N}_i} \alpha^k_{ij} \mathbf{W}^k \vec{h}_j)$$

multi-head 图注意力层的聚合过程如图1右侧所示。

**与相关工作的性能比较**

+ 计算高效：**self-attention层的操作可以在所有的边上并行，输出特征的计算可以在所有顶点上并行。**没有耗时的特征值分解。**单个的GAT计算$F'$个特征的时间复杂度可以压缩至$O(\vert V \vert F F’ + \vert E \vert F’)，F$**是输入的特征数，$\vert V \vert$和$\vert E \vert$是图中顶点数和边数。复杂度与Kipf & Welling, 2017的GCN差不多。**尽管使用multi-head attention可以并行计算，但也使得参数和空间复杂度变成了K倍。**
+ **对比GCN，GAT允许对顶点的同一个邻居分配不同的重要度**，使得模型能力上有一个飞跃。不仅如此，对学习到的attentional权重进行分析可以得到更好的解释性，就像机器翻译领域一样（比如Bahdanau et al., 2015的定性分析）。
+ 注意力机制以一种共享的策略应用在图的所有的边上，因此它并不需要在之前就需要得到整个图结构或是所有的顶点的特征（很多之前的方法的缺陷）。因此这个方法有几个影响：
    + 图不需要是无向的（如果边$j \rightarrow i$没有出现，我们可以直接抛弃掉$\alpha_{ij}$的计算）
    + 这个方法可以直接应用到inductive learning——包括在训练过程中在完全未见过的图上评估模型的任务上。

    

我们可以做出一种使用稀疏矩阵操作的GAT层，将空间复杂度降低到与顶点数和边数成正比，使得GAT模型可以在更大的图数据集上运行。然而，我们使用的tensor操作框架只支持二阶tensor的稀疏矩阵乘法，限制了当前实现的版本模型的批处理能力（尤其在有多个图的数据集上）。解决这个问题是未来的一个重要研究方向。在这些使用稀疏矩阵的场景下，在某些图结构下GPU的运算并不能比CPU快多少。另一个需要注意的地方是我们的模型的感受野的大小的上界取决于网络的深度（与GCN和其他模型相似）。像skip connections(He et al., 2016)这样的技术可以来近似的扩展模型的深度。最后，在所有边上的并行计算，尤其是在分布式计算场景下，存在很多冗余的计算，因为图中的邻居往往高度重叠（每个分布式处理器上都会重复计算这些重叠的邻居节点）。

<h3>3. Evaluation</h3>

实验部分请参考：
1. [Graph Attention Networks](https://davidham3.github.io/blog/2018/07/13/graph-attention-networks/)
2. [论文 | 图注意力网络 | GRAPH ATTENTION NETWORKS](https://www.jianshu.com/p/8078bf1711e7)







 