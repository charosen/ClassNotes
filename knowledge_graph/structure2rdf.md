<h1>旅游知识图谱实践篇（二）--结构化数据到RDF</h1>

这是从零构建海南旅游知识图谱实践系列的第二篇，本篇主要介绍将结构化数据转换成RDF格式数据的几种方法。

<h2>1. 简介</h2>

经过[旅游知识图谱实践篇（一）--携程半结构化知识抽取](https://github.com/charosen/ClassNotes/blob/master/knowledge_graph/semi_structure_extractor.md)所述的半结构化数据爬取，项目获得了携程海南旅游的结构化数据。这些结构化数据可以存储在各种数据库中，如关系数据库MySQL, SQL Server, 非关系数据库MongoDB等等。

并且，各色数据库对数据的存储形式不同（如，MySQL使用类似表结构存储数据，MongoDB使用Bson文档存储数据），这些异构数据非常不利于构建知识图谱。根据互联网之父Bernee Lee提出的语义网络以及[知识图谱理论篇（四）--语义网技术栈（Semantic Web Stack）](https://github.com/charosen/ClassNotes/blob/master/knowledge_graph/semantic_web_stack.md)，我们需要将各色异构数据转换成语义网友好的RDF格式。

<h2>2. 关系数据库数据转换RDF</h2>

对于关系数据库，W3C的RDB2RDF工作小组制定了两个标准[Direct Mapping](https://www.w3.org/TR/rdb-direct-mapping/)和[R2RML](https://www.w3.org/TR/r2rml/#term-map)，用于将关系数据库的数据转换为RDF数据；

**Direct Mapping**:编写启发式规则将数据库中的表转换为RDF三元组，映射规则如下 

1. 表-->概念类；
2. 列-->属性；
3. 行-->资源；
4. 单元格-->字面量；
5. 如果单元格所在的列是外键，那么其值为IRI，或者说实体/资源;

Direct Mapping的优点在于其简单方便，其缺点在于不能定制化映射，不能把数据库的数据映射到我们自己定义的本体上。

**R2RML**:一种用于表示从关系数据库到RDF数据集的**自定义**映射的**语言**。

R2RML映射使用[logical table](https://www.w3.org/TR/r2rml/#dfn-logical-table)来从输入数据库获取数据，一个logical table可以是：

1. 表a base table；
2. 视图a view，或者
3. 一个有效的SQL查询（也叫"[R2RML view]()"，因为它无需修改数据库而模拟SQL视图）；

R2RML映射使用[triples map](https://www.w3.org/TR/r2rml/#dfn-triples-map)将logical table中的每一行映射成多个RDF三元组，一个triples map包含以下部分：

1. [subject map](https://www.w3.org/TR/r2rml/#dfn-subject-map)负责生成logical table一行映射而成的所有三元组的subject；
2. [predicate-object maps](https://www.w3.org/TR/r2rml/#dfn-predicate-object-map)，它是由[predicate maps](https://www.w3.org/TR/r2rml/#dfn-predicate-map)与[object maps](https://www.w3.org/TR/r2rml/#dfn-object-map)组成，负责生成三元组的predicate和object；

默认情况下，所有RDF三元组都存储在输出数据集的默认图default graph中。三元组映射可以包含图形映射[graph maps](https://www.w3.org/TR/r2rml/#dfn-graph-map)，这些图形映射将部分或全部三元组放入命名图[named graph](https://www.w3.org/TR/r2rml/#dfn-named-graph)中。

详情请参考：
1. [从零开始构建知识图谱（二）数据库到 NTriples 以及通过Apache jena 访问NT](http://pelhans.com/2018/09/03/kg_from_0_note2/);
2. [实践篇（二）：关系数据库到RDF](https://zhuanlan.zhihu.com/p/32552993);
3. [R2RML](https://www.w3.org/TR/r2rml/#term-map);

<h2>3. 关系数据库、JSON、CSV等数据转换RDF</h2>

在现实世界中，数据不仅可能存储在关系数据库，数据也可能存储在CSV、TSV、XML、JSON等格式文件。W3C为解决异构结构化数据转换成RDF数据的问题，提出了一个R2RML的拓展版本--RML（RDF Mapping Language）。

**RML**:一种用于表示从异构数据结构到RDF数据集的**自定义**映射的**语言**，支持关系数据库、CSV、TSV、JSON、XML格式数据。

同理，RML映射使用[logical source](http://semweb.mmlab.be/rml/spec.html#logical-source)来从输入数据库获取数据，一个logical source可以是：

1. A base source (any input source or base table),
2. a view (in case of databases)；

[logical source](http://semweb.mmlab.be/rml/spec.html#logical-source)定义需要：

1. 如果数据源是关系数据库，则需要定义rml:source和rml:referenceFormualtion，可选定义rml:iterator；
2. 如果数据源是csv，则需要定义rml:source和rml:iterator；
3. 如果数据源是json、xml，则需要定义rml:source、rml:referenceFormualtion和rml:iterator；

> The source (**rml:source**) locates the input data source. It is a [URI] that represents the data source where the data source is.
The logical iterator (**rml:iterator**) defines the iteration loop used to map the data of the input source. 
The reference formulation (**rml:referenceFormulation**) defines the reference formulation used to refer to the elements of the data source. The reference formulation must be specified in the case of databases and XML and JSON data sources. By default SQL2008 for databases, as SQL2008 is the default for R2RML, [XPath] for XML and JSONPath for JSON data sources.

类似的，RML映射使用[triples map](https://www.w3.org/TR/r2rml/#dfn-triples-map)将logical source中的(数据库、CSV、TSV)每一行/(XML)每一个元素/(JSON)每一个对象映射成多个RDF三元组，一个triples map包含以下部分：

1. [subject map](https://www.w3.org/TR/r2rml/#dfn-subject-map)负责生成logical table一行映射而成的所有三元组的subject；
2. [predicate-object maps](https://www.w3.org/TR/r2rml/#dfn-predicate-object-map)，它是由[predicate maps](https://www.w3.org/TR/r2rml/#dfn-predicate-map)与[object maps](https://www.w3.org/TR/r2rml/#dfn-object-map)组成，负责生成三元组的predicate和object；

详情请参考：

1. [RDF Mapping Language (RML)(一定要看)](http://semweb.mmlab.be/rml/spec.html#);

<h2>4. 非关系数据库数据转换RDF</h2>

上述的RML映射虽然一定程度上拓展的R2RML，但是它并不支持将非关系数据库中数据映射成RDF数据。因此，W3C提出一种新的映射语言xR2RML，用于将非关系数据库数据转换成RDF数据；

（后续可补充...）

详情请参考论文：

1. [Translation of Relational and Non-Relational Databases into RDF with xR2RML](https://hal.archives-ouvertes.fr/hal-01141686);
2. [xR2RML: Relational and Non-Relational Databases to RDF Mapping Language](https://hal.archives-ouvertes.fr/hal-01066663);

<h2>5. 海南旅游知识图谱所采取的解决方案</h2>

由于实践篇（一）选择MongoDB存储海南携程旅游数据，在这里我们使用xR2RML映射语言来将数据库中的数据转换成RDF格式。

本项目使用github上关于[xR2RML mapping language](https://hal.archives-ouvertes.fr/hal-01141686)的一个java实现工具--[morph-xr2rml](https://github.com/frmichel/morph-xr2rml)来完成数据转换。

Morph-xR2RML自带关系数据库(MySQL, PostgreSQL, MonetDB)与非关系数据库MongoDB的连接器，且Morph-xR2RML具有两种运行模式：

1. 图输出模式：将数据一次性直接转换成RDF图；
2. 查询重写模式：将SPARQL查询转换成目标数据库的查询，根据数据库查询结果返回一个SPARQL答案。

Morph-xR2RML官方提供了MongoDB和MySQL的使用例子，分别位于目录`morph-xr2rml-dist/example_mongo`、`morph-xr2rml-dist/example_mongo_rewritting`、`morph-xr2rml-dist/example_mysql`、`morph-xr2rml-dist/example_mysql_rewritting`；

Morph-xR2RML安装使用到了maven（java项目间依赖管理工具），maven的核心功能为合理叙述项目间的依赖关系，详情请参考：

1. [Maven通俗讲解](https://blog.csdn.net/shuzhe66/article/details/45009175);
2. [maven(一) maven到底是个啥玩意~](https://www.cnblogs.com/whgk/p/7112560.html);

上面简述的Morph-xR2RML工具，现在我们将详细介绍海南旅游知识图谱数据转换过程：

首先，本项目使用xR2RML映射语言定义了海南旅游写成知识图谱的映射文件`smarttrip_mapping.ttl`，用于将MongoDB中的旅游数据映射到实践一中自定义的旅游知识本体。`smarttrip_mapping.ttl`文件城市部分代码如下（.ttl是turtle格式的RDF文件）：

```
# City Mapping
<#City>
    a rr:TriplesMap;
    xrr:logicalSource [
        # Jongo needs strings in singles quotes (difference with MongoDB shell)
        xrr:query """db.city.find( { } )""";
    ];
    rr:subjectMap [
        xrr:reference "$.url";
        rr:class kg:city;
    ];
    # 中文名
    rr:predicateObjectMap [
        rr:predicate kg:中文名;
        rr:objectMap [ xrr:reference "$.名称"; rr:language "cn"; ];
    ];
    # id
    rr:predicateObjectMap [
        rr:predicate kg:id;
        rr:objectMap [ xrr:reference "$['_id']"; rr:datatype xsd:integer; ];
    ];
    # 时间戳
    rr:predicateObjectMap [
        rr:predicate kg:timestamp;
        rr:objectMap [ xrr:reference "$.timestamp"; rr:datatype xsd:dateTimeStamp; ];
    ];
    # 数据来源
    rr:predicateObjectMap [
        rr:predicate kg:source;
        rr:objectMap [ xrr:reference "$.source"; ];
    ].

```

在定义好映射文件之后，项目通过修改`morph.properties`文件来配置海南携程旅游MongoDB数据库连接，并指定输出RDF Graph的格式为N-Triples。

PS: morph-xr2rml在连接MongoDB数据库时，使用"MONGODB-CR"进行身份认证，"MONGODB-CR"是旧版本的认证机制，4.0版本以上的MongoDB数据库已经不知处这种认证机制，因此要求MongoDB版本低于4.0，且进行如下配置：

```
首先关闭认证，修改system.version文档里面的authSchema版本为3，初始安装时候应该是5，命令行如下： 
> use admin 
switched to db admin 
>  var schema = db.system.version.findOne({"_id" : "authSchema"}) 
> schema.currentVersion = 3 
3 
> db.system.version.save(schema) 
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 }) 

用户权限不够，修改上述authSchema版本会报错，如果报错，则先执行如下命令，给用户提供更新authSchema版本的权限：
db.grantRolesToUser ( "root", [
{ role: "__system", db: "admin" }
] )

不过如果你现在开启认证，仍然会提示AuthenticationFailed MONGODB-CR credentials missing in the user document 
原因是原来创建的用户已经使用了SCRAM-SHA-1认证方式 
> use admin 
> db.auth('root','123456')
> db.system.users.find()
{ "_id" : "admin.root", "user" : "root", "db" : "admin", "credentials" : { "SCRAM-SHA-1" : { "iterationCount" : 10000, "salt" : "XoI5LXvuqvxhlmuY6qkJIw==", "storedKey" : "VAT7ZVMw2kFDepQQ6/E0ZGA5UgM=", "serverKey" : "TebHOXdmY6IHzEE1rW1Onwowuy8=" } }, "roles" : [ { "role" : "userAdminAnyDatabase", "db" : "admin" } ] }
{ "_id" : "mydb.test", "user" : "test", "db" : "mydb", "credentials" : { "MONGODB-CR" : "c8ef9e7ab00406e84cfa807ec082f59e" }, "roles" : [ { "role" : "readWrite", "db" : "mydb" } ] }
解决方式就是删除刚刚创建的用户，重新重建即可： 
> db.system.users.remove({user:"test"});
> use mydb 
>db.createUser({user:'test',pwd:'123456',roles:[{role:'readWrite',db:'mydb'}]}) 
```
然后，我们在命令行执行如下命令即可得到RDF格式数据，完成数据格式转换：

```
java -jar target/morph-xr2rml-dist-1.0-SNAPSHOT-jar-with-dependencies.jar \
   --configDir <configuration directory> \
   --configFile <configuration file within this directory>
```

<h2>6. 总结</h2>

本篇介绍了把JSON、TSV、CSV、XML、关系数据库MySQL、非关系数据库MongoDB等多种数据源数据转换成RDF格式数据的方法，同时，本项目从多种方法中选取MongoDB+xR2RML方法来完成数据转换。

当然，现方法仍存在诸多问题需要解决：

1. morph-xr2rml只能执行简单的MongoDB查询query语句，比如"db.collection.find({})"，而似乎无法执行聚合Aggregation语句；
2. JsonPath好像无法取出MongoDB返回的Json数据中的键；