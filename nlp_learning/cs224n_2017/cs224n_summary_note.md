<h1>CS224N 2017 NLP with Deep Learning</h1>

<h2>lecture01: 课程介绍</h2>

<h3>1. 什么是自然语言处理？</h3>

1. NLP：
     1. 交叉学科：计算机科学，人工智能，语言学；
     2. 目标：让计算机理解和处理自然语言；
     3. 终极目标：完全理解与表示语言的意义(meaning)
         1. 完美的语言理解是一个`AI-complete`问题；
2. NLP涉及的层次/语言学对语言层次的传统描述：
     1. ![-w998](media/15482343995316.jpg)
3. NLP应用：
    1. 简单应用：eg，拼写检查、关键词检索...
    2. 复杂应用：
        1. 文本挖掘：从文本中抽取特定信息；
        2. 文本分类：eg，文档的阅读难度reading level；文档的情感分析；
    3. 更复杂应用：
        1. 机器翻译Machine Translation
        2. 口语对话系统Spoken dialog systems
        3. 复杂问答系统Complex question answering

<h3>2. 人类语言的特点</h3>

1. 人类语言并不是需要你处理成有用信息的一堆海量数据，它是指向性明确的、将某条具体信息传递给其他人的通信方式；
2. 人类语言的**定义**：一个离散的discrete/符号的symbolic/标称的categorical的信号系统；
    1. 使用“符号”进行通信，eg，火箭=🚀，小提琴=🎻...
    2. 存在极少数非符号的、富有表现力的信号；
    3. （信息论）符号在通信中具有高可靠性（why most of symbol）；
3. 人类语言**沟通的具体方式**：使用多种连续的载体来承载离散的语言符号，eg，声音、手势、图片...
    1. 语言在大脑中的表示是**连续**的；
    2. 语言的传播媒介是**连续**的；
    3. 语言本身是符号/**离散**/标称的信号系统--**存在稀疏性sparsity问题**；
    4. DP4NLP核心思想：为原始语言数据寻找合适的**连续特征表示**，并使用**连续的激活模式continuous pattern of activation**来处理连续特征表示；

<h3>3. 什么是深度学习</h3>

1. Machine Learning: 90%人工发现问题关键、人工设计特征+10%机器参数优化/数值优化numeric optimization
2. Deep Learning:
    1. 机器学习的子领域、表示学习的分支；
    2. 无需人工设计特征，自动学习出原始数据的（多层）特征表示；
3. Why Deep Learning?
    1. 人工定义的特征：太过具体、不完整、耗时...
    2. 学习得到的特征：方便拓展、学习快
    3. ...
4. 深度学习的崛起：
    1. 第一个突破--语音识别：Context-Dependent Pre-trained Deep Neural Networks for Large Vocabulary Speech Recognition Dahl et al. (2010)；
    2. 第二个突破--计算机视觉：ImageNet Classification with Deep Convolutional Neural Networks by Krizhevsky, Sutskever, & Hinton, 2012, U. Toronto. 37% error red.

<h3>4. NLP难在哪</h3>

1. 人类语言存在歧义；
2. 人类语言理解需要真实世界知识、常识、上下文知识...

<h3>5. DP for NLP</h3>

1. DP4NLP：结合NLP的思想与DP的方法来解决NLP的问题
2. DP运用于：
    1. NLP的不同层级LEVELS：语音speech, 词word, 句子syntax, 语义semantics...
    2. NLP的不同工具TOOLS：词性parts-of-speech, 实体entities, 解析parsing...
    3. NLP的不同应用：machine translation, sentiment analysis, dialogue agents, question ansewring...
3. DP4NLP应用：
    1. 词向量word vectors表示词义word meaning，本质将词义映射到高维向量空间；
        1. ![-w922](media/15482377840089.jpg)

    2. 词向量word vectors计算词相似度；
        1. ![](media/15482378293578.jpg)
    3. DP on NLP LEVELS--词素morphemes级别的特征表示：
        1. words are made of morphemes:eg, prefix + stem + suffix(un + interest + ed)...
        2. `Luong et al. 2013`: every morpheme is a vector
        3. ![-w331](media/15482380301995.jpg)
    4. DP on NLP Tools--依存句法分析：
        1. ![-w928](media/15482381491760.jpg)
    5. DP on NLP LEVELS--语义级别的特征表示：
        1. `Bowman et al. 2014`: every word and every phrase and every logical expression is a vector；
        2. ![-w932](media/15482382763687.jpg)
    6. DP on NLP APPLICATIONS--
        1. 情感分析：RecursiveNN...
        2. QA：...
        3. 对话机器人：Google inbox suggested replies
        4. 神经机器翻译Neural Machine Translation：Sutskever et al. 2014, Bahdanau et al. 2014, Luong and Manning 2016
4. **总结：DP4NLP的所有级别的特征表示都是向量！！！**





    
