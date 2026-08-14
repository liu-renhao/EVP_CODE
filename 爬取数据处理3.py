import csv

# 定义高校图书馆的关键字列表
university_keywords = ['学校', '学院', '教学', '大学', '高校', '校区', '中学', '小学', '幼儿园', '教育']

# 存储处理后的数据
processed_data = []

# 设置CSV字段大小限制
csv.field_size_limit(500 * 1024 * 1024)

# 读取原始CSV文件
with open('./Zero-shot/51output_snow.csv', mode='r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)

    # 读取标题行
    headers = next(reader)

    # 添加新的列名
    headers.append('library_type')
    processed_data.append(headers)

    # 确定text列的索引（假设列名为'text'）
    try:
        text_index = headers.index('text')
    except ValueError:
        # 如果列名不匹配，尝试其他可能的列名
        possible_names = ['text', 'Text', 'TEXT', '内容', '描述']
        for name in possible_names:
            if name in headers:
                text_index = headers.index(name)
                break
        else:
            # 如果找不到text列，使用第二列（索引1）作为默认
            print("警告：未找到'text'列，将使用第二列作为文本内容")
            text_index = 1

    # 遍历每一行数据
    for row in reader:
        # 确保行有足够的列
        if len(row) > text_index:
            text_content = row[text_index]

            # 判断图书馆类型
            library_type = '公共图书馆'  # 默认值为公共图书馆

            # 检查text列中是否包含高校关键词
            if any(keyword in text_content for keyword in university_keywords):
                library_type = '高校图书馆'

            # 添加新的列值
            row.append(library_type)
            processed_data.append(row)

# 将处理后的数据写入新的CSV文件
with open('51output_snow_new.csv', mode='w', encoding='utf-8-sig', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(processed_data)

print(f"处理完成！共处理 {len(processed_data) - 1} 行数据（包含标题行）")
print("结果已保存到 'processed_result_with_library_type.csv' 文件中")