# EDA Project - Code Organization by Task

This guide shows which code to download and run for each task.

---

## 📥 WHAT TO DOWNLOAD

```
1. requirements.txt        ← Install dependencies
2. eda_analysis.py         ← Main analysis code
3. download_sample_data.py ← Get sample datasets
4. data.csv                ← Your dataset (optional)
5. README.md               ← Quick start guide
```

**Download from:** `https://github.com/sravya3333/eda-project`

---

## 🔍 TASK 1: Statistical Analysis & Summary Statistics

### What This Task Does:
- Calculate mean, median, standard deviation
- Show min, max, quartiles
- Count categories
- Check data types
- Identify missing values

### Code Location:
`eda_analysis.py` → Functions:
- `basic_info()` - Line 26-41
- `summary_statistics()` - Line 56-75
- `separate_columns()` - Line 48-51

### Run This:
```bash
python eda_analysis.py
```

### Output:
```
=== DATA TYPES ===
Age              int64
Income          int64
...

=== MISSING VALUES ===
[Shows any missing data]

=== DESCRIPTIVE STATISTICS ===
count    1000.000000
mean       49.500000
std        28.866070
50%        49.500000
...
```

### Code Snippet (if running separately):
```python
import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')

# Summary Statistics
print(df.describe())
print(df.info())
print(df.isnull().sum())
print(df.value_counts())
```

---

## 📊 TASK 2: Explore Dataset Using Visualizations

### What This Task Does:
- Create distribution plots (histograms)
- Generate boxplots for outlier detection
- Show categorical bar charts
- Generate correlation heatmaps
- Create pairwise relationship plots

### Code Location:
`eda_analysis.py` → Functions:
- `plot_numeric_distributions()` - Line 77-93
- `plot_boxplots()` - Line 95-107
- `plot_categorical_distribution()` - Line 109-124
- `plot_correlation_heatmap()` - Line 126-137
- `plot_pairplot()` - Line 139-154

### Run This:
```bash
python eda_analysis.py
```

### Generated Files:
```
plots/
├── 01_numeric_distributions.png
├── 02_boxplots.png
├── 03_categorical_distributions.png
├── 04_correlation_heatmap.png
└── 05_pairplot.png
```

### Code Snippet (if running separately):
```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('data.csv')

# Distribution plot
df.hist(figsize=(10, 6))
plt.savefig('distribution.png')

# Boxplot
df.boxplot()
plt.savefig('boxplot.png')

# Correlation heatmap
sns.heatmap(df.corr(), annot=True)
plt.savefig('correlation.png')

# Pairplot
sns.pairplot(df)
plt.savefig('pairplot.png')
```

---

## 🔗 TASK 3: Identify Correlations & Key Factors

### What This Task Does:
- Calculate correlation coefficients
- Identify strong vs weak relationships
- Perform statistical tests (Pearson correlation)
- Calculate p-values
- Rank features by correlation strength

### Code Location:
`eda_analysis.py` → Functions:
- `analyze_relationships()` - Line 156-189
- `run_statistical_tests()` - Line 191-208
- `plot_correlation_heatmap()` - Line 126-137

### Run This:
```bash
python eda_analysis.py
```

### Output:
```
=== STATISTICAL TESTS ===

Target variable: Purchase_Amount
Age vs Purchase_Amount: r=0.6534, p=0.0000
Income vs Purchase_Amount: r=0.7821, p=0.0000
Years_Customer vs Purchase_Amount: r=0.4421, p=0.0001
```

### Code Snippet (if running separately):
```python
import pandas as pd
from scipy.stats import pearsonr

df = pd.read_csv('data.csv')

# Correlation matrix
corr_matrix = df.corr()
print(corr_matrix)

# Correlation with target
target = 'Purchase_Amount'
for col in df.columns:
    if col != target and df[col].dtype in ['int64', 'float64']:
        coef, p_value = pearsonr(df[col], df[target])
        print(f"{col}: r={coef:.4f}, p={p_value:.4f}")
```

---

## 🔍 TASK 4: Find Important Patterns, Trends & Relationships

### What This Task Does:
- Identify distribution shapes (skewness, kurtosis)
- Find variance patterns (high vs low variability)
- Discover group differences
- Detect trends over categories
- Analyze pairwise relationships

### Code Location:
`eda_analysis.py` → Functions:
- `analyze_relationships()` - Line 156-189
- `plot_pairplot()` - Line 139-154
- `plot_correlation_heatmap()` - Line 126-137
- `generate_report()` - Line 210-310

### Run This:
```bash
python eda_analysis.py
```

### Output (from report):
```
5. PATTERNS & TRENDS
   • Highest variance: Income
   • Lowest variance: Years_Customer
   • Most skewed: Purchase_Amount
   • Most diverse category: Country

4. KEY FINDINGS & RELATIONSHIPS
   1. Income: Correlation = 0.7821 (strong positive)
   2. Age: Correlation = 0.6534 (moderate positive)
   3. Country -> Purchase_Amount: USA has highest avg
```

### Code Snippet (if running separately):
```python
import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')

# Skewness and Kurtosis
print("Skewness:")
print(df.skew())
print("\nKurtosis:")
print(df.kurtosis())

# Variance
print("\nVariance:")
print(df.var())

# Group analysis
print("\nAverage Purchase by Country:")
print(df.groupby('Country')['Purchase_Amount'].mean())
```

---

## 📋 TASK 5: Present Findings in Structured Report

### What This Task Does:
- Generates professional report file
- Summarizes all findings
- Provides recommendations
- Lists all visualizations
- Documents data quality issues

### Code Location:
`eda_analysis.py` → Functions:
- `generate_report()` - Line 210-310

### Run This:
```bash
python eda_analysis.py
```

### Output File:
```
eda_report.txt (automatically generated)
```

### Report Contents:
```
============================================================
EXPLORATORY DATA ANALYSIS (EDA) REPORT
============================================================

1. DATA QUALITY ASSESSMENT
   • Missing values: 0
   • Duplicate rows: 0
   • Data types: 4 different types

2. DATASET OVERVIEW
   • Numeric columns (5): Age, Income, ...
   • Categorical columns (4): Country, Gender, ...

3. SUMMARY STATISTICS
   [Statistical values table]

4. KEY FINDINGS & RELATIONSHIPS
   1. Income: Correlation = 0.7821 (strong positive)
   2. Age: Correlation = 0.6534 (moderate positive)
   ...

5. PATTERNS & TRENDS
   • Highest variance: Income
   • Most skewed: Purchase_Amount
   ...

6. RECOMMENDATIONS
   • Investigate outliers
   • Validate correlations
   • Build predictive models
   ...

7. VISUALIZATIONS GENERATED
   ✓ 01_numeric_distributions.png
   ✓ 02_boxplots.png
   ✓ 03_categorical_distributions.png
   ✓ 04_correlation_heatmap.png
   ✓ 05_pairplot.png
```

### Code Snippet (if running separately):
```python
import pandas as pd

df = pd.read_csv('data.csv')

# Create custom report
report = []
report.append("=" * 60)
report.append("MY EDA REPORT")
report.append("=" * 60)
report.append(f"\nRows: {df.shape[0]}, Columns: {df.shape[1]}")
report.append(f"Missing values: {df.isnull().sum().sum()}")
report.append(f"\nSummary Stats:\n{df.describe()}")

# Save report
with open('my_report.txt', 'w') as f:
    f.write('\n'.join(report))
```

---

## 🚀 COMPLETE WORKFLOW

### Step 1: Download Files
```bash
git clone https://github.com/sravya3333/eda-project.git
cd eda-project
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Get Data
```bash
python download_sample_data.py
# Choose option 1-6
```

### Step 4: Configure (Optional)
Edit `eda_analysis.py`:
```python
DATA_PATH = "data.csv"
TARGET_COLUMN = None  # or "Purchase_Amount" if you want
```

### Step 5: Run Analysis
```bash
python eda_analysis.py
```

### Step 6: Review Results
```
Console output ← Shows statistics
plots/ folder ← Contains 5 visualizations
eda_report.txt ← Complete findings report
```

---

## 📊 Task Mapping

| Task | Function | Output |
|------|----------|--------|
| 1. Statistical Analysis | `basic_info()`, `summary_statistics()` | Console output, summary stats |
| 2. Visualizations | `plot_*()` functions | 5 PNG files in plots/ folder |
| 3. Correlations | `analyze_relationships()`, `run_statistical_tests()` | Correlation values, p-values |
| 4. Patterns & Trends | All visualization + analysis functions | Pairplots, heatmaps, patterns |
| 5. Structured Report | `generate_report()` | eda_report.txt file |

---

## 💾 FILES TO DOWNLOAD

**Essential:**
- ✅ `eda_analysis.py` (Main code)
- ✅ `requirements.txt` (Dependencies)
- ✅ `download_sample_data.py` (Get datasets)

**Documentation:**
- 📖 `README.md` (Quick start)
- 📖 `TASK_BY_TASK_GUIDE.md` (This file)

**Generated After Running:**
- 📊 `eda_report.txt`
- 🖼️ `plots/` folder with 5 images

---

## ✅ CHECKLIST

Before submission:
- [ ] Downloaded all files
- [ ] Installed requirements.txt
- [ ] Downloaded sample data
- [ ] Ran eda_analysis.py
- [ ] Got eda_report.txt
- [ ] Got plots/ folder with 5 images
- [ ] Reviewed console output
- [ ] Understood each task
- [ ] Ready for next phase

---

**Start Here:**
```bash
python download_sample_data.py
python eda_analysis.py
```
