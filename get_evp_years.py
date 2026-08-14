import pandas as pd

# 读取CSV文件，假设分隔符为制表符（根据样例调整）
df = pd.read_csv('evp_results_all.csv', sep=',')

print(df.head(10))

# 提取年份：将year列转换为字符串，分割后取前四位
df['year'] = df['year'].astype(str).apply(lambda x: x.split('/')[0]).astype(int)

# 定义需要计算平均值的列
columns_to_avg = [
    '经济价值（Economic）',
    '发展价值（Development）',
    '兴趣价值（Interest）',
    '应用价值（Management）',
    '管理价值（Application）',
    '社会价值（Social）',
    '工作与生活平衡（Work-Life）'
]

# 按年份分组计算均值，并保留三位小数
result = (
    df.groupby('year', as_index=False)[columns_to_avg]
    .mean()
    .round(3)
)

# 保存结果为新的CSV文件
result.to_csv('evp_year_results_averages.csv', index=False)