## Chapter 3. 数据预处理 

<h3 id='3.1.'>一、数据预处理(Data Preprocessing:An Overview)</h3>

1. 数据预处理的目的：提高数据质量；
2. 数据质量的衡量标准：**准确性(Accuracy)、完整性(Completeness)、一致性(Consistency)**、时效性(Timeliness)、可信度(Belivability)、可解释性(Interpretability)；
3. 数据预处理的主要工作：数据清理、数据集成、数据归约、数据变换与数据离散化

<h3 id='3.2.'>二、数据清理(Data Cleaning)</h3>

<h4 id='3.2.1.'>1. 填充 缺失属性值--数据不完整(Incompleteness)</h4>

1. 数据缺失（不完整）Missing Data情形：缺失属性值，缺失整个属性，只包含聚合数据...
2. 处理方法：
    1. 直接丢弃数据对象：可能会丢弃非缺失的、有价值的属性；
    2. 人工补全：
    3. 自动补全：
        1. 使用全局常量来补全："Unknown"或"-∞"；
            + 不要直接添0，因为0有时候是有意义的；
            + 当所有缺失值都用"Unknown"补全时，挖掘程序可能认为其是一个新的概念，效果不好；
        2. 使用所有数据对象的该属性的中心度量（均值、中位数、众数）来补全（一类数据情况）；
        3. 使用属于同一类的数据对象的该属性的中心度量（均值、中位数、重视）来补全（多类数据情况）；
        4. 使用最可能值来补全：

<h4 id='3.2.2.'>2. 平滑噪声数据--数据不准确(Inaccuracy)</h4>

1. 噪声Noise：属性测量值的随机误差与方差；
2. 处理方法：
    1. 分箱(Bining)：
        1. 排序数据，并分组数据至**等频率**的箱子；
        2. 在箱子内使用均值或中位数或箱子边界来平滑箱内数据，实现局部平滑；
    2. 回归(Regression)：使用回归函数来拟合数据，偏离回归函数的数据可以丢弃或者使用回归函数上的数据来平滑噪声；
    3. 聚类(Clustering)：检测并去除异常值，平滑噪声
    4. 半监督方法(Semi-supervised)：

<h4 id='3.2.3.'>3. 数据清理是一个不断反复的过程</h4>

1. 数据清理步骤1--偏差检测(Data discrepancy detection)：
    + 使用元数据（数据的数据，例如数据的定义域、范围、依赖性、分布）检查；
    + 检查字段过载(Field overloading)：新属性的定义挤进已经定义的属性的未使用位；
    + 检查唯一性规则(Uniqueness rule)、连续性规则(Consecutive rule)、空值规则(null rule)；
    + 使用商业软件检查：
        + 数据清洗工具(Data scrubbing tools)：
        + 数据审计工具(Data auditing tools)：
2. 数据清理步骤2--数据变换(Data Transformation)：用以纠正偏差；
    + 数据迁移工具(Data migration tools)：
    + 抽取/变换/载入工具(Extraction/Transformation/Loading)：
3. 两个步骤迭代执行

<h3 id='3.3.'>三、数据集成(Data Integration)</h3>

<h4 id='3.3.1.'>1. 实体识别问题</h4>

1. 模式集成(Schema integration)：从不同数据源集成元数据
2. 对象匹配(Object matching)：
3. 实体识别(Entity identification)：

<h4 id='3.3.2.'>2. 数据值冲突的检测与处理</h4>

数据值冲突原因：不同表达式、不同编码、不同度量单位（例如，公制与英制）

<h4 id='3.3.3.'>3. 冗余和相关分析</h4>

<h5 id='3.3.3.1.'>3.1. 数据集成后，冗余来源：</h5>

1. 不同数据源的属性命名不一致；
2. 衍生属性(Derived attributes)：可从其他属性继承/衍生得到的属性；

<h5 id='3.3.3.2.'>3.2. 标称数据的相关分析Correlation Analysis(Nominal Attr)</h5>

使用卡方$\chi^2$相关检验(chi-squared test)：就是概率论里的假设检验

1. 零假设(Null hypothesis)：假设两个属性相互独立（或者不相关）；
2. 画两个属性的相依表（类似于离散随机变量的联合分布律）

    ![相依表与卡方检验-c](./img/chi_squared_test.png)

3. 计算卡方检验(chi-squared test)值：

    $$\chi^2 = \sum_i^n \sum_j^n \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$
    
    + 观测频度$O_{ij}$：相依表中每格的数；
    + 期望频度$E_{ij}$：假设两个属性独立时，数据总数 * 联合概率（边缘概率连乘积）$E_{ij} = n * p_{ij} = n * p_i * p_j$；

4. 计算自由度：（属性A类别数-1）*（属性B类别数-1）；
5. 根据自由度、卡方值查表，判断能否拒绝假设：
    + 卡方值越大，越相关；
    + 对$\chi^2$值贡献最大的标称属性的类别是其实际计数与期望计数最不相同的类别；

<h5 id='3.3.3.3.'>3.3. 数值属性的相关分析Correlation Analysis(Numeric Attr)</h5>

使用皮尔斯叉乘相关系数(Correlation coefficient, Pearson's product moment coefficient)

(右侧等式很容易推导)

$$r_{A,B} = \frac{\sum_{i=1}^n (a_i - \overline{A})(b_i - \overline{B})}{n \delta_A \delta_B} = \frac{\sum_{i=1}^n (a_i b_i) - n \overline{A} \overline{B}}{n \delta_A \delta_B}$$

+ n：数据量/样本数目；
+ $\overline{A}, \overline{B}$：是A、B属性的样本均值；
+ $\delta_A, \delta_B$：是A、B属性的样本标准差；
+ $\sum (a_i b_i)$：是A、B属性的叉乘；

Pearson相关系数>0, 两属性正相关；Pearson相关系数<0, 两属性负相关；Pearson相关系数=0，两属性独立

![皮尔森相关系数可视化-c](./img/visualization_correlation.png)

<h5 id='3.3.3.4.'>3.4. 数值属性的协方差分析Covariance Analysis(Numeric Attr)</h5> 

使用协方差(Covariant)：

$$Cov(A, B) = E[(A - \overline{A})(B - \overline{B})] = \frac{\sum_{i=1}^n (a_i - \overline{A})(b_i - \overline{B})}{n}$$

协方差与Pearson相关系数的关系：

$$r_{A, B} = \frac{Cov(A, B)}{\delta_A \delta_B}$$

协方差>0, 正相关；协方差<0, 负相关；协方差=0，不相关，但不说明独立，多元高斯分布情况下，不相关==独立；

![协方差例子-c](./img/covariance_example.png)

<h3 id='3.4.'>四、数据归约(Data Reduction)</h3>

<h4 id='3.4.1.'>1. 维归约(Dimension Reduction)</h4>

<h5 id='3.4.1.1.'>1.1. 属性子集选择(Attribute Subset Selection)</h5>

1. 降维手段：删除不相关属性（对数据挖掘任务无用的属性）与冗余属性（包含的信息与其他属性相冗余的属性）；
2. 属性子集选择的相关技术：

![属性子集选择的相关技术-c](./img/attribute_subset_selection_techs.png)

<h5 id='3.4.1.2.'>1.2. 属性生成(Feature Generation)</h5>

![属性生成-c](./img/attribute_creation.png)

<h4 id='3.4.2.'>2. 数量归约(Numerosity Redcution)</h4>

<h5 id='3.4.2.1.'>2.1. 数量归约方法分类</h5>

1. 参数方法(Parametric methods)：使用模型估计数据，进而使用模型参数来代替原始数据，例如，回归和对数线性模型(Log-linear models)；
2. 非参数方法(Non-parametric methods)：不使用模型；

<h5 id='3.4.2.2.'>2.2. 数据归约参数方法：回归</h5>



<h5 id='3.4.2.3.'>2.3. 数据归约非参数方法：直方图</h5>



<h5 id='3.4.2.4.'>2.4. 数据归约非参数方法：聚类</h5>



<h5 id='3.4.2.5.'>2.5. 数据归约非参数方法：抽样</h5>



<h5 id='3.4.2.3.'>2.3. 数据归约非参数方法：数据立方</h5>




<h4 id='3.4.3.'>3. 数据压缩(Data compression)</h4>




<h3 id='3.5.'>五、数据变换与数据离散化(Data Transformation and Data Discretization)</h3>
