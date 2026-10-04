# Exploratory Data Analysis (EDA) Project

A comprehensive Python project for performing Exploratory Data Analysis on any dataset. This project helps you uncover patterns, trends, correlations, and generate actionable insights.

## 📋 Features

✅ **Statistical Analysis** - Comprehensive summary statistics and descriptive analysis  
✅ **Data Quality Checks** - Missing values, duplicates, and data type analysis  
✅ **Visualizations** - Distribution plots, boxplots, correlation heatmaps, pairplots  
✅ **Correlation Analysis** - Identify relationships between variables  
✅ **Pattern Detection** - Find trends and important patterns in data  
✅ **Automated Report** - Generate structured findings report  

## 📁 Project Structure

```
eda-project/
├── README.md                      # This file
├── requirements.txt               # Python dependencies
├── eda_analysis.py               # Main EDA analysis script
├── download_sample_data.py        # Download/generate sample datasets
├── data.csv                       # Your dataset (add your own)
├── eda_report.txt                # Generated analysis report
└── plots/                         # Generated visualizations
    ├── 01_numeric_distributions.png
    ├── 02_boxplots.png
    ├── 03_categorical_distributions.png
    ├── 04_correlation_heatmap.png
    └── 05_pairplot.png
```

## 🚀 Quick Start

### Step 1: Clone/Download the Repository
```bash
git clone https://github.com/sravya3333/eda-project.git
cd eda-project
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Download or Add Dataset

**Option A: Download Sample Dataset**
```bash
python download_sample_data.py
```
Then choose from:
- 1: Iris Dataset
- 2: Titanic Dataset
- 3: Wine Dataset
- 4: Breast Cancer Dataset
- 5: Generated Customer Data
- 6: Generated Sales Data

**Option B: Use Your Own Dataset**
- Place your CSV file in the project folder
- Rename it to `data.csv` or update `DATA_PATH` in `eda_analysis.py`

### Step 4: Run EDA Analysis
```bash
python eda_analysis.py
```

## 📊 What Gets Generated

### 1. Console Output
- Data shape and basic info
- Data types and missing values
- Summary statistics
- Statistical tests results
- Key findings and relationships

### 2. Visualizations (in `plots/` folder)
- **01_numeric_distributions.png** - Histograms with KDE curves
- **02_boxplots.png** - Outlier detection
- **03_categorical_distributions.png** - Bar charts for categories
- **04_correlation_heatmap.png** - Feature correlation matrix
- **05_pairplot.png** - Pairwise relationships

### 3. Report File
- **eda_report.txt** - Structured findings and recommendations

## 🎯 Configuration

Edit `eda_analysis.py` (lines 15-16) to customize:

```python
# For general analysis
DATA_PATH = "data.csv"
TARGET_COLUMN = None

# For customer data with target
DATA_PATH = "data.csv"
TARGET_COLUMN = "Purchase_Amount"

# For Titanic data
DATA_PATH = "data.csv"
TARGET_COLUMN = "Survived"
```

## 📈 Analysis Includes

### Task 1: Statistical Analysis & Summary Statistics
- Mean, median, standard deviation
- Min, max, quartiles
- Skewness and kurtosis
- Category value counts

### Task 2: Visualizations
- Distribution plots (histograms)
- Boxplots for outlier detection
- Categorical bar charts
- Correlation heatmaps
- Pairwise relationship plots

### Task 3: Correlation & Key Factors
- Pearson correlation coefficients
- Strong vs weak relationships
- Feature importance based on correlation
- Statistical significance (p-values)

### Task 4: Patterns, Trends & Relationships
- Univariate patterns (distribution shapes)
- Bivariate relationships (scatter patterns)
- Categorical group differences
- Trend identification

### Task 5: Structured Report
- Executive summary
- Data quality assessment
- Statistical findings
- Key recommendations
- Actionable insights

## 💡 Example Usage

### Example 1: Analyze Iris Dataset
```bash
python download_sample_data.py  # Choose option 1
python eda_analysis.py
```

### Example 2: Analyze Your CSV File
```bash
# Copy your data.csv to the project folder
python eda_analysis.py
```

### Example 3: Analyze with Target Variable
Edit `eda_analysis.py`:
```python
TARGET_COLUMN = "Sales"  # Your target variable
```
Then run:
```bash
python eda_analysis.py
```

## 📚 Output Examples

### Console Output
```
============================================================
STARTING EXPLORATORY DATA ANALYSIS (EDA)
============================================================

Dataset loaded successfully: 150 rows, 5 columns

=== DATA TYPES ===
sepal length (cm)    float64
sepal width (cm)     float64
...

=== MISSING VALUES ===
[empty if no missing values]

=== DESCRIPTIVE STATISTICS ===
count, mean, std, min, 25%, 50%, 75%, max
```

### Generated Report
```
============================================================
EXPLORATORY DATA ANALYSIS (EDA) REPORT
============================================================

Dataset Shape: 150 rows × 5 columns

1. DATA QUALITY ASSESSMENT
   • Missing values: 0
   • Duplicate rows: 0
   • Data types: 2 different types

2. DATASET OVERVIEW
   • Numeric columns (4): sepal length, sepal width, ...
   • Categorical columns (1): target

3. SUMMARY STATISTICS
   [Statistical values table]

4. KEY FINDINGS
   1. sepal length: Correlation = 0.8717 (strong positive)
   ...
```

## 🔧 Troubleshooting

**Q: "Dataset not found" error**
```
A: Make sure data.csv is in the same folder as eda_analysis.py
```

**Q: No visualizations generated**
```
A: Check if you have numeric columns in your dataset
   Adjust column limits in the script if needed
```

**Q: Memory error with large dataset**
```
A: Sample your data: df = df.sample(n=10000, random_state=42)
```

## 🎓 Skills Developed

- ✅ Data loading and exploration
- ✅ Missing value handling
- ✅ Statistical analysis
- ✅ Data visualization
- ✅ Correlation and relationship analysis
- ✅ Report generation and documentation
- ✅ Python programming (pandas, numpy, matplotlib, seaborn)

## 📞 Support

For detailed guide and advanced usage, see GUIDE.md

---

**Happy Analyzing! 🎉** Start with `python download_sample_data.py`
