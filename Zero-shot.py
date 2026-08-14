from transformers import pipeline
import csv
from typing import Dict, List
import numpy as np
import pprint


class ChineseEVPAnalyzer:
    def __init__(self, csv_path: str, model_name: str = "bart-large-mnli"):
        """
        初始化 EVP 分析器 device="cuda:1"
        :param csv_path: CSV 文件路径，包含维度与关键词
        :param model_name: 预训练模型名称
        """
        # 从 CSV 读取维度和关键词
        self.dimension_keywords = self._load_dimensions_from_csv(csv_path)
        self.classifier = pipeline("zero-shot-classification", model=model_name, temperature=0.3,)

    def _load_dimensions_from_csv(self, csv_path: str) -> Dict[str, List[str]]:
        """从 CSV 文件加载维度与关键词的映射"""
        dimension_keywords = {}
        with open(csv_path, "r", encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                dimension = row["dimension"]
                keywords = row["keywords"].split("、")
                dimension_keywords[dimension] = keywords
        return dimension_keywords

    def evaluate_evp(self, text: str, multi_label: bool = True) -> Dict[str, float]:
        """
        七维 EVP 评估
        :param text: 输入文本
        :param multi_label: 是否允许多标签（一个文本可同时匹配多个关键词）
        :return: 各维度得分字典
        """
        evp_scores = {}
        for dimension, keywords in self.dimension_keywords.items():
            # 对每个维度调用 Zero-shot 分类器
            result = self.classifier(
                text,
                candidate_labels=keywords,
                multi_label=multi_label,
                hypothesis_template='本条文本涉及以下理论主题：{}。',
            )
            # 取该维度下关键词的最高分作为维度得分
            top_score = max(result["scores"]) if result["scores"] else 0.0
            evp_scores[dimension] = round(top_score, 3)
        return self._normalize_scores(evp_scores)


    def _normalize_scores(self, raw_scores: Dict[str, float]) -> Dict[str, float]:
        """使用softmax将原始分数转换为概率分布"""
        scores = list(raw_scores.values())
        exp_scores = np.exp(scores - np.max(scores))  # 数值稳定性处理
        probabilities = exp_scores / exp_scores.sum()

        # 构建归一化后的结果
        normalized_scores = {}
        for i, (dimension, _) in enumerate(raw_scores.items()):
            normalized_scores[dimension] = round(probabilities[i], 3)

        return normalized_scores


def batch_predict(input_csv: str, output_csv: str, keyword_csv: str) -> None:
    """
    批量预测并保存结果到 CSV
    :param input_csv: 输入 CSV 文件路径（含待分析文本）
    :param output_csv: 输出 CSV 文件路径（保存结果）
    :param keyword_csv: 维度关键词 CSV 文件路径
    """
    # 初始化分析器
    analyzer = ChineseEVPAnalyzer(keyword_csv)

    # 读取输入文件并保留所有列
    with open(input_csv, "r", encoding="utf-8") as f_in:
        reader = csv.DictReader(f_in)
        rows = list(reader)  # 保留所有原始数据
        fieldnames = reader.fieldnames  # 原始列名

    # 添加 EVP 维度列名
    evp_columns = list(analyzer.dimension_keywords.keys())
    new_fieldnames = fieldnames + evp_columns

    # 处理每一行数据
    for row in rows:
        # 执行 EVP 预测
        evp_scores = analyzer.evaluate_evp(row["text"])
        # 将预测结果合并到原始数据
        row.update(evp_scores)

    # 写入输出文件
    with open(output_csv, "w", encoding="utf-8", newline="") as f_out:
        writer = csv.DictWriter(f_out, fieldnames=new_fieldnames)
        writer.writeheader()
        writer.writerows(rows)


# 示例使用
if __name__ == "__main__":
    # 输入输出文件路径
    input_csv = "TQdata.csv"
    output_csv = "evp_results_all.csv"
    keyword_csv = "keyword.csv"

    # 执行批量预测
    batch_predict(input_csv, output_csv, keyword_csv)
    print(f"预测完成！结果已保存至 {output_csv}")