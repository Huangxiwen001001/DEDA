*========================*
DEDA-Fudan-Group2：Final Project
*========================*

成员（按分工顺序排序）：王肃坤、黄熙雯、陈泽昊、李思源、王贺

*==============================================
项目使用的数据均来源于：Xiaojian Niu, Jiahao Gong, Sukun Wang, Haofan Qiang. Research on the Cascading Interdependent Mechanism of Upside and Downside Financial Risks across Stock and Bond Markets: Cascading Interdependent Multiplex Networks Approach from an Industry Perspective, 2024, Working Paper.

项目分为三个部分，具体说明如下：

*--------------------------------------------------------------------------

1 聚类 Clustering（路径：FinalProject/1_Clustering）

1.1 数据说明

个体：29个行业（申万一级行业分类）；

时间及频率：2009-01-09至2010-01-09（国际金融危机中后期）；周度数据

聚类指标：行业 j 的风险联动总强度Risk_j。由行业间债券风险联动网络邻接矩阵内，行业 j 的风险传染强度（第 j 行）和风险承受强度（第 j 列）加总得到。其中，行业间债券风险联动网络邻接矩阵由“基于去一法和数据锐化的非线性格兰杰因果检验”对债券已实现波动率RV计算得到。


1.2 聚类方法

1.2.1 谱聚类 Spectral Clustering；
三种展示方式：谱聚类图（graph_spectral_clustering.jpg）；t-SNE图（graph_tsne.jpg）；UMAP图（graph_umap.jpg）

1.2.2 层次聚类 Hierarchical clustering
一种展示方式：Iris聚类树（graph_iris_clustering.jpg）


1.3 聚类结果解释

每一类别 所含行业数字标签 对应的具体名称，见“result_clustering.txt”中的Spectral Clustering Results和Hierarchical Clustering Results

同一类别的行业具有更相似的风险联动特征，其背后有一定的经济意义（比如行业性质类似、受国际金融危机的影响相似，等等）


*----------------------------------------------------------------------------

2 最小生成树 Minimum Spanning Tree（路径：FinalProject/2_MST）

2.1 数据说明

MST对图（由节点、链接构成）进行分析

图的节点：58个节点，分别是29个行业的股票节点，以及29个行业的债券节点

图的链接：行业不同资产之间的风险联动强度

该部分分析了以下四个阶段的风险联动网络：
股票牛市（stock bull，2014年7月—2015年6月）
股票熊市（stock bear，2015年6月—2016年1月）
债券牛市（bond bull，2013年11月—2016年10月）
债券熊市（bond bear，2016年10月—2017年11月）


2.2 最小生成树结果

图像结果：见“MST_vol_bad_stock_bull_非线性网络.jpg”等四张图

行业名称：图像中节点编号对应的行业名称（中文），见“industry_mapping_rule.txt”；行业名称（英文），见“label_vol_bad_bond_bear_非线性网络.txt”

结果解释：最小生成树保留了风险联动网络中最主干的部分。如果某些行业在这四个阶段都存在，说明这些行业对于风险联动具有重要的作用；尤其是占据中心位置的行业，更说明其关键地位


*-------------------------------------------------------------------------------

3 机器学习预测 Machine Learning（路径：FinalProject/3_ML）

3.1 数据说明

数据结构：股票市场下行风险联动网络，以邻接矩阵表示，由29个行业股票资产节点及其链接构成

时间及频率：2008-06-05至2022-12-30，共710个网络邻接矩阵；采用滚窗计算，窗口为250天，步长为一周（5个交易日）

预测思路：将以下时段设定为金融危机发生时期，期内的网络特征标注为1，期外标注为0，训练模型以预测未来的金融危机发生时期，评价模型性能：
 (datetime(2007, 7, 26), datetime(2009, 12, 31)),  # Global financial crisis
 (datetime(2013, 6, 7), datetime(2013, 12, 31)),  # Bank liquidity crisis
 (datetime(2015, 6, 15), datetime(2016, 12, 20))  # Stock market crash


3.2 训练设定

3.2.1 图神经网络 GNN 参数设置

隐藏层数量 hidden_channels=65；分类种类 num_classes=2；节点特征 num_node_features=1；链接特征 num_edge_features=1；训练次数 epoch = 350

3.2.2 模型性能评价指标
预测准确率 Accuracy（越高越好） F1-score（越高越好） F-Alarm（越低越好）


3.3 训练过程与结果

训练过程准确率时序图：见“graph_accuracy_curve.jpg”

训练集预警信号图：见“graph_prediction_results.jpg”

Accuracy、F1-score、F-Alarm逐次训练结果：见“accuraciesGGNN.csv”

*==================================================

以上是Final Project所有实证工作的说明。


作者：（小组成员）王肃坤 黄熙雯

