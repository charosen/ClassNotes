<h1>知识图谱理论篇(七) --Bi-GRU Word Attention模型、Entity-centric Attention模型远程监督关系抽取</h1>

<h2>1. 论文阅读 -- Improving Distantly Supervised Relation Extraction using Word and Entity Based Attention</h2>

1. introduction
    1. 远程监督存在误标注问题，导致数据集引入噪声，远程监督假说过于strong，Riedel et al. (2010); Hoffmann et al. (2011); Surdeanu et al. (2012)等研究放宽了DS assumption；
        1. Riedel et al. (2010) --> expressed-at-least-once assumption: 如果两个实体在知识库中存在关系r，则**至少一句**提及这两个实体的句子表达了关系r --> 多实例单标签学习multi-instance single-label learning；
        2. Hoffmann et al. (2011) --> 关系可能会重叠：一对实体e1，e2可能会存在多种关系 --> 多实例多标签学习multi-instance multi-label learning；
    2. Riedel2010数据集中50%的句子超过40个词，长句子中并不是所有词都对表达关系语义有贡献，因此词级别的注意力机制可提升关系抽取性能；
    3. 远程监督数据集中，存在at-least-one假设不成立的情况，即一个instance set中的所有instance都不表示关系r，这导致multi-instance learning失效，这在测试集中是致命的，阻碍正确评估；
    4. 论文贡献：
        1. 为解决at-least-one假设不成立情况，避免multi-instance learning失效，发布Google-IISC Distant Supervision dataset，保证每一个instance set中至少有一个instance表示指定关系r；
        2. 提出俩个词级别注意力模型，Bi-GRU(word attention)和EA(entity-centric attetion)；
        3. 组合现有模型与新模型，提出一个weighted ensemble model；
2. 模型介绍：
    1. 基于Bi-GRU的词级别注意力模型（BGWA）：
    2. 实体注意力模型(Entity-Attention)：
    3. Ensemble Model：
3. 远程监督关系抽取数据集--GIDS：
4. 实验与结果：在GIDS和Riedel2010两个数据集上测试了词注意力模型、实体注意力模型和ensemble model；
    1. 评判准则：held-out evaluation，使用PR曲线评估模型性能；
    2. 模型超参数选择：
        1. ![](media/15557776787022.jpg)
        2. ![](media/15557777018412.jpg)

5. 相关工作：略
6. 总结：
    1. 模型很好blabla；
    2. 数据集很牛逼blabla；
    3. 未来还要研究将提出的几个词级别注意力模型与句子级别注意力相结合的模型；

<h2>附录 True Positive、False Positive、True Negative、False Negative、Precision、Recall、F1与ROC曲线、PR曲线</h2>

1. 不平衡数据：
    1. 例如：一个产品生产的不合格产品数量会远低于合格产品数量。信用卡欺诈的检测中，合法交易远远多于欺诈交易。这时候，**准确率Accuracy的度量会出现一些问题，因为她把每个类都看得同等重要**。例如，1%的信用卡交易是欺诈行为，则预测每个交易都是合法的模型有99%的**准确率Accuracy**，它也可能检测不到任何欺诈交易。
2. 混淆矩阵
    1. **在不平衡数据中，稀有类比较有意义，对于二元分类，稀有类通常记为正类，而多数类被认为是负类。**下面显示了**混淆矩阵**：![](media/15557451968325.jpg)
3. 根据混淆矩阵，分类器分类结果分为以下4种：
    1. 真正（true positive，TP）：实例是正类且被预测成正类；
    2. 假正（false positive，FP）：实例是负类且被预测成正类；
    3. 真负（true negative，TN）：实例是负类且被预测成负类；
    4. 假负（false negative，FN）：实例是正类且被预测成负类；
4. 根据4种分类结果，我们可以得到如下针对不平衡数据的分类器评价标准：
    1. 真正率（true positive rate，TPR）或灵敏度（sensitivity）或召回率(Recall)：正例中有多少被正确预测为正例$$TPR=\frac{TP}{TP+FN}=\frac{(++)}{(++)+(+-)}$$
    2. 真负率（true negative rate，TNR）或特指度（specificity）：负例中有多少被正确预测为负例$$TNR=\frac{TN}{TN+FP}=\frac{(--)}{(--)+(-+)}$$
    3. 假正率（false positive rate，FPR）：负例中有多少被错误预测为正例$$FPR=\frac{FP}{TN+FP}=\frac{(+-)}{(--)+(-+)}$$
    4. 假负率（false negative rate，FNR）：正例中有多少被错误预测为负例$$FNR=\frac{FN}{FN+TP}=\frac{(-+)}{(-+)+(++)}$$
    5. 精度（precision）：预测为正的例子中有多少是真正的正例$$p=\frac{TP}{TP+FP}=\frac{(++)}{(++)+(-+)}$$
    6. 召回率（recall）即为真正率：正例中有多少被正确预测为正例$$r=\frac{(TP)}{(TP)+(FN)}=\frac{(++)}{(++)+(+-)}$$
    7. F1 统计量：F1 是召回率和精度的调和平均数，F1 趋近于它们之间的较小值，因此，一个高的 F1 确保精度和召回率都高。$$F_{1}=\frac{2rp}{r+p}=\frac{2\times TP}{2\times TP+FP+FN}=\frac{2}{\frac{1}{r}+\frac{1}{p}}$$
5. 接受者操作曲线（ROC）：是真正率和假正率取折中的一种图形化方法。真正率为 y 轴，假正率为 x 轴。
    1. ROC的几个关键点：
        1. 坐标原点（TPR=0,FPR=0）:把所有的都预测为负
        2. 右上角点（TPR=1,FPR=1）:把所有的都预测为正
        3. 左上角点（TPR=1,FPR=0）:理想模型。只要是正的，都预测为正。
    2. 一个好的分类器，尽量靠近左上角，随机猜想为对角线。
    3. ![](media/15557475649227.jpg)
    4. ROC曲线绘制方法：按正样本概率从高到低排序样本结果，将分类器阈值设为正样本概率最大的的正样本的概率，依次选取样本并将阈值降为选取样本的正样本概率，并更新TPR和FPR，直到遍历完所有样本；
6. PR曲线：Precision Recall曲线，PR曲线用来衡量分类的性能，纵坐标为Precision，横坐标为Recall。
    1. PR曲线绘制方法：按正样本概率从高到低排序样本结果，将分类器阈值设为正样本概率最大的的正样本的概率，依次选取样本并将阈值降为选取样本的正样本概率，并更新Precision和Recall，直到遍历完所有样本；

参考链接：
1. [分类（6）：不平衡和多分类问题](https://www.jianshu.com/p/15185f0ecb57);
2. [多分类ROC曲线](https://blog.csdn.net/u011047955/article/details/87259052);
3. [ROC曲线、PR曲线](https://www.cnblogs.com/houkai/p/3330061.html);

