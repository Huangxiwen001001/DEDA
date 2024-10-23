import pandas as pd

# 读取原始文件
input_file_path = r'D:\1_FDU\3_Learn_Python\DigitalEconomyDecisionAnalytics-master\FinalProject\1_Clustering\data_网络拓扑指标_债市周度.csv'
output_file_path = r'D:\1_FDU\3_Learn_Python\DigitalEconomyDecisionAnalytics-master\FinalProject\1_Clustering\data_risk_Industry.csv'

# 加载数据
data = pd.read_csv(input_file_path)

# 定义行业翻译字典
industry_translation = {
    '交通运输': 'Transportation',
    '传媒': 'Media',
    '公用事业': 'Utilities',
    '农林牧渔': 'Agriculture, Forestry, Animal Husbandry, and Fishery',
    '医药生物': 'Pharmaceuticals and Biotechnology',
    '商贸零售': 'Trade and Retail',
    '国防军工': 'Defense and Military',
    '基础化工': 'Basic Chemicals',
    '家用电器': 'Household Appliances',
    '建筑材料': 'Building Materials',
    '建筑装饰': 'Construction and Decoration',
    '房地产': 'Real Estate',
    '有色金属': 'Non-Ferrous Metals',
    '机械设备': 'Machinery and Equipment',
    '汽车': 'Automobiles',
    '煤炭': 'Coal',
    '环保': 'Environmental Protection',
    '电力设备': 'Power Equipment',
    '电子': 'Electronics',
    '石油石化': 'Petroleum and Petrochemicals',
    '社会服务': 'Social Services',
    '纺织服饰': 'Textiles and Apparel',
    '综合': 'Conglomerate',
    '计算机': 'Computers',
    '轻工制造': 'Light Industry and Manufacturing',
    '通信': 'Telecommunications',
    '钢铁': 'Steel',
    '非银金融': 'Non-Bank Financials',
    '食品饮料': 'Food and Beverages'
}

# 翻译行业名称
data['Ind'] = data['Ind'].map(industry_translation)

# 为每个行业分配数字标签
industry_label_mapping = {industry: idx + 1 for idx, industry in enumerate(industry_translation.values())}
data['Industry_Label'] = data['Ind'].map(industry_label_mapping)

# 保存为新的 CSV 文件
data.to_csv(output_file_path, index=False)

print(f"文件已成功保存到 {output_file_path}")
