# Libraries Tell Applicants What They Need — But Not Why They Should Join: An EVP Iceberg Analysis of Library Recruitment Advertisements

This repository contains the code, source data, and reproducibility materials for the study Libraries Tell Applicants What They Need — But Not Why They Should Join: An EVP Iceberg Analysis of Library Recruitment Advertisements, presented at the 89th Annual Meeting of the Association for Information Science & Technology (ASIS&T), 2026.

**Default zero-shot model:** `facebook/bart-large-mnli`

## 1. Data

Recruitment advertisements were collected from the WeChat public account **“图情招聘”** and cover **2019–2025**.

- Total valid advertisements: **2,258**
- Academic/university libraries: **1,717**
- Public libraries: **541**
- Information-rich advertisements: **483**
- Information-poor advertisements: **1,775 (78.6%)**

The data were filtered, deduplicated, cleaned, and structured. Main fields include publication date, recruiting institution, position, recruitment requirements, and library type.

### Source data

| File | Description |
|---|---|
| `TQdata.csv` | Source dataset containing the 2,258 recruitment records collected from the “图情招聘” WeChat public account and used as the starting dataset for the study. |
| `evp_results_all.csv` | Zero-shot classification results for the full sample. It contains the seven EVP dimension scores generated from the recruitment texts.|
| `information-rich-results.xls` | A 483-record information-rich subset filtered directly from evp_results_all.csv. The EVP scores in this file are inherited from the full-sample zero-shot output. |
| `Descriptive Statistical Analysis.xlsx` | Descriptive statistical results derived from the EVP outputs and used in the study/poster analysis. |
| `keyword.csv` | The seven EVP dimensions and their domain-specific seed words used by Zero-shot.py for seed-guided zero-shot classification. |

## 2. Analytical Workflow

```text
WeChat recruitment advertisements
        ↓
Filtering, cleaning, deduplication, structuring
        ↓
Library-type classification + manual verification
        ↓
TQdata.csv (2,258 records)
        ↓
BART-large-MNLI zero-shot EVP classification
        ↓
evp_results_all.csv
        ↓
Filter information-rich records
        ↓
information-rich-results.xls (483 records)
        ↓
Descriptive statistics and library-type comparison
```

## 3. EVP Framework

| Dimension | Operational definition |
|---|---|
| **Economic Value** | Salary, benefits, allowances, and other economic rewards. |
| **Development Value** | Training, promotion, professional development, and career growth. |
| **Interest Value** | Interesting, innovative, challenging, or meaningful work. |
| **Application Value** | Opportunities to apply professional knowledge and skills. |
| **Management Value** | Organizational rules, responsibilities, coordination, and management support. |
| **Social Value** | Teamwork, interpersonal relationships, belonging, and service orientation. |
| **Work–Life Balance Value** | Leave, working hours, workload, and other work–life arrangements. |

The corresponding Chinese seed words are provided in `sourcedata/keyword.csv`.

## 4. Zero-Shot Model

Default model:

```text
facebook/bart-large-mnli
```

For each recruitment text, `Zero-shot.py` loads the seven EVP dimensions and seed words, calculates a score for each dimension, normalizes the seven scores, and records the highest-scoring dimension as **Max EVP**.

The 483 information-rich records are filtered from `evp_results_all.csv` **after the full-sample classification**.

## 5. Repository Files

| File | Purpose |
|---|---|
| `获取推文连接.py` | Collects WeChat article links and metadata. |
| `过滤链接.py` | Filters recruitment-related article links. |
| `微信推文爬取.py` | Scrapes recruitment content from WeChat articles. |
| `爬取数据处理3.py` | Processes scraped data and assigns library type. |
| `Zero-shot.py` | Performs seven-dimensional EVP zero-shot classification. |
| `get_evp_years.py` | Calculates annual mean EVP scores. |
| `sourcedata/` | Contains source data, model outputs, statistical results. |

## 6. Reproducibility

Install dependencies:

```bash
pip install requests beautifulsoup4 lxml pandas numpy transformers torch
```

Run the main analysis:

1. Use `sourcedata/TQdata.csv` as input.
2. Use `sourcedata/keyword.csv` as the EVP seed-word file.
3. Set the model in `Zero-shot.py` to:

```python
model_name = "facebook/bart-large-mnli"
```

4. Run:

```bash
python Zero-shot.py
```

5. Save the full-sample output as `evp_results_all.csv`.
6. Filter the 483 information-rich records from this file to obtain `information-rich-results.xls`.

For annual EVP trends, run `get_evp_years.py` after updating its input filename if needed.

> The WeChat crawling scripts may require local authentication information and path adjustments. Do not upload active cookies, tokens, or other private credentials to a public repository.

