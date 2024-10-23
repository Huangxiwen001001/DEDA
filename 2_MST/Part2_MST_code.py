import os
import numpy as np
import networkx as nx
from scipy.sparse.csgraph import minimum_spanning_tree
import matplotlib.pyplot as plt

# 设置文件路径
file_directory = r'D:\1_FDU\3_Learn_Python\DigitalEconomyDecisionAnalytics-master\FinalProject\2_MST'

# 英文翻译的行业名，用于图例
english_labels = {
    0: 'Transportation_Bond', 1: 'Media_Bond', 2: 'Utilities_Bond', 3: 'Agriculture_Bond', 4: 'Pharmaceuticals_Bond',
    5: 'Retail_Bond', 6: 'Defense_Bond', 7: 'Chemicals_Bond', 8: 'Home_Appliances_Bond', 9: 'Building_Materials_Bond',
    10: 'Construction_Decoration_Bond', 11: 'Real_Estate_Bond', 12: 'Non_Ferrous_Metals_Bond', 13: 'Machinery_Bond',
    14: 'Automotive_Bond', 15: 'Coal_Bond', 16: 'Environmental_Protection_Bond', 17: 'Electric_Power_Equipment_Bond',
    18: 'Electronics_Bond', 19: 'Petrochemicals_Bond', 20: 'Social_Services_Bond', 21: 'Textiles_Bond',
    22: 'Comprehensive_Bond',
    23: 'Computers_Bond', 24: 'Light_Industry_Bond', 25: 'Telecommunications_Bond', 26: 'Steel_Bond',
    27: 'Non_Bank_Finance_Bond',
    28: 'Food_Beverage_Bond', 29: 'Transportation_Stock', 30: 'Media_Stock', 31: 'Utilities_Stock',
    32: 'Agriculture_Stock',
    33: 'Pharmaceuticals_Stock', 34: 'Retail_Stock', 35: 'Defense_Stock', 36: 'Chemicals_Stock',
    37: 'Home_Appliances_Stock',
    38: 'Building_Materials_Stock', 39: 'Construction_Decoration_Stock', 40: 'Real_Estate_Stock',
    41: 'Non_Ferrous_Metals_Stock',
    42: 'Machinery_Stock', 43: 'Automotive_Stock', 44: 'Coal_Stock', 45: 'Environmental_Protection_Stock',
    46: 'Electric_Power_Equipment_Stock',
    47: 'Electronics_Stock', 48: 'Petrochemicals_Stock', 49: 'Social_Services_Stock', 50: 'Textiles_Stock',
    51: 'Comprehensive_Stock',
    52: 'Computers_Stock', 53: 'Light_Industry_Stock', 54: 'Telecommunications_Stock', 55: 'Steel_Stock',
    56: 'Non_Bank_Finance_Stock',
    57: 'Food_Beverage_Stock'
}

# 遍历文件夹中的所有npy文件
for file_name in os.listdir(file_directory):
    if file_name.endswith('.npy'):
        # 加载npy文件
        file_path = os.path.join(file_directory, file_name)
        data = np.load(file_path)

        # 生成最小生成树
        mst_matrix = minimum_spanning_tree(data).toarray()

        # 创建图结构
        graph = nx.from_numpy_matrix(mst_matrix)

        # 设置节点标签为节点编号
        node_labels = {i: str(i) for i in range(data.shape[0])}

        # 绘制图形
        fig, ax = plt.subplots(figsize=(10, 10), dpi=300)  # 高分辨率
        pos = nx.spring_layout(graph)
        nx.draw(graph, pos, ax=ax, with_labels=True, labels=node_labels, node_size=500, node_color='lightblue',
                font_size=10, edge_color='gray')

        # 保存图片为jpg格式
        save_path = os.path.join(file_directory, f'MST_{file_name.split(".")[0]}.jpg')
        plt.savefig(save_path, format='jpg', bbox_inches='tight')
        plt.close()

        print(f'Saved MST for {file_name} as {save_path}')

        # 生成节点编号和标签对应关系的文字
        correspondence_text = "\n".join([f'Node {i}: {english_labels[i]}' for i in range(data.shape[0])])

        # 保存文字到文件
        text_save_path = os.path.join(file_directory, f'label_{file_name.split(".")[0]}.txt')
        with open(text_save_path, 'w') as f:
            f.write(correspondence_text)

        print(f'Saved labels correspondence for {file_name} as {text_save_path}')
