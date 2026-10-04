import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

warnings.filterwarnings("ignore")
sns.set_style("whitegrid")

# ------------------------------------------------------------
# 1. CONFIGURATION
# ------------------------------------------------------------
DATA_PATH = "data.csv"              # Replace with your file
TARGET_COLUMN = None                 # Example: "sales", "price", "churn"
OUTPUT_REPORT = "eda_report.txt"

# ------------------------------------------------------------
# 2. LOAD DATA
# ------------------------------------------------------------
def load_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found: {path}")

    df = pd.read_csv(path)
    print(f"\nDataset loaded successfully: {df.shape[0]} rows, {df.shape[1]} columns")
    print(df.head())
    return df

# ------------------------------------------------------------
# 3. DATA QUALITY CHECKS
# ------------------------------------------------------------
def basic_info(df):
    print("\n=== DATA TYPES ===")
    print(df.dtypes)

    print("\n=== MISSING VALUES ===")
    missing = df.isnull().sum()
    print(missing[missing > 0].to_string())

    print("\n=== DUPLICATES ===")
    print(f"Duplicate rows: {df.duplicated().sum()}")

    print("\n=== DESCRIPTIVE STATISTICS ===")
    print(df.describe(include="all").T)

# ------------------------------------------------------------
# 4. FEATURE TYPE DETECTION
# ------------------------------------------------------------
def separate_columns(df):
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()
    return numeric_cols, categorical_cols

# ------------------------------------------------------------
# 5. SUMMARY STATISTICS
# ------------------------------------------------------------
def summary_statistics(df):
    numeric_cols, categorical_cols = separate_columns(df)

    print("\n=== NUMERIC COLUMNS ===")
    print(numeric_cols)

    print("\n=== CATEGORICAL COLUMNS ===")
    print(categorical_cols)

    if numeric_cols:
        print("\n=== NUMERIC SUMMARY ===")
        print(df[numeric_cols].describe().round(2))

    if categorical_cols:
        print("\n=== CATEGORY COUNTS ===")
        for col in categorical_cols[:10]:
            print(f"\n{col}:")
            print(df[col].value_counts().head(10))

# ------------------------------------------------------------
# 6. MISSING VALUE TREATMENT
# ------------------------------------------------------------
def handle_missing_values(df):
    numeric_cols, categorical_cols = separate_columns(df)

    for col in numeric_cols:
        median_val = df[col].median()
        df[col].fillna(median_val, inplace=True)

    for col in categorical_cols:
        mode_val = df[col].mode(dropna=True)
        if not mode_val.empty:
            df[col].fillna(mode_val.iloc[0], inplace=True)

    return df

# ------------------------------------------------------------
# 7. VISUALIZATIONS
# ------------------------------------------------------------
def plot_numeric_distributions(df, numeric_cols):
    if not numeric_cols:
        return

    n = len(numeric_cols)
    cols = 2
    rows = (n + 1) // 2

    plt.figure(figsize=(14, 5 * rows))
    for i, col in enumerate(numeric_cols, 1):
        plt.subplot(rows, cols, i)
        sns.histplot(df[col], bins=25, kde=True)
        plt.title(f"Distribution of {col}")
        plt.tight_layout()
    plt.savefig("plots/01_numeric_distributions.png", dpi=100, bbox_inches='tight')
    plt.close()
    print("✓ Saved: plots/01_numeric_distributions.png")

def plot_boxplots(df, numeric_cols):
    if not numeric_cols:
        return

    plt.figure(figsize=(14, 4 * len(numeric_cols)))
    for i, col in enumerate(numeric_cols, 1):
        plt.subplot(len(numeric_cols), 1, i)
        sns.boxplot(x=df[col])
        plt.title(f"Boxplot of {col}")
    plt.tight_layout()
    plt.savefig("plots/02_boxplots.png", dpi=100, bbox_inches='tight')
    plt.close()
    print("✓ Saved: plots/02_boxplots.png")

def plot_categorical_distribution(df, categorical_cols, max_cols=10):
    cols = [c for c in categorical_cols if c in df.columns][:max_cols]
    if not cols:
        return

    plt.figure(figsize=(14, 4 * len(cols)))
    for i, col in enumerate(cols, 1):
        plt.subplot(len(cols), 1, i)
        sns.countplot(data=df, x=col, order=df[col].value_counts().index[:10])
        plt.title(f"Count plot: {col}")
        plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("plots/03_categorical_distributions.png", dpi=100, bbox_inches='tight')
    plt.close()
    print("✓ Saved: plots/03_categorical_distributions.png")

def plot_correlation_heatmap(df, numeric_cols):
    if len(numeric_cols) < 2:
        return

    corr = df[numeric_cols].corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("plots/04_correlation_heatmap.png", dpi=100, bbox_inches='tight')
    plt.close()
    print("✓ Saved: plots/04_correlation_heatmap.png")

def plot_pairplot(df, numeric_cols, target_col=None):
    if len(numeric_cols) < 2:
        return

    sample_cols = numeric_cols[:5] if len(numeric_cols) > 5 else numeric_cols
    data = df[sample_cols].copy()

    if target_col and target_col in df.columns and target_col in sample_cols:
        pass

    sns.pairplot(data, diag_kind="kde", height=2.2)
    plt.savefig("plots/05_pairplot.png", dpi=100, bbox_inches='tight')
    plt.close()
    print("✓ Saved: plots/05_pairplot.png")

# ------------------------------------------------------------
# 8. RELATIONSHIP ANALYSIS
# ------------------------------------------------------------
def analyze_relationships(df, target_col=None):
    numeric_cols, categorical_cols = separate_columns(df)
    findings = []

    if target_col and target_col in df.columns and target_col in numeric_cols:
        for col in numeric_cols:
            if col == target_col:
                continue
            corr = df[col].corr(df[target_col])
            findings.append({
                "feature": col,
                "metric": "pearson_correlation",
                "value": corr,
                "interpretation": "strong positive" if abs(corr) > 0.7 else
                                  "moderate positive" if abs(corr) > 0.4 else
                                  "weak/low" if abs(corr) > 0.1 else
                                  "very weak"
            })

    # Categorical vs numeric analysis
    for col in categorical_cols:
        for num_col in numeric_cols:
            if df[col].nunique() <= 20:
                grouped = df.groupby(col)[num_col].mean()
                if not grouped.empty:
                    best = grouped.idxmax()
                    findings.append({
                        "feature": f"{col} -> {num_col}",
                        "metric": "group_mean",
                        "value": grouped.to_dict(),
                        "interpretation": f"Category '{best}' has the highest average {num_col}"
                    })

    return findings

# ------------------------------------------------------------
# 9. STATISTICAL TESTS
# ------------------------------------------------------------
def run_statistical_tests(df, target_col=None):
    numeric_cols, _ = separate_columns(df)
    print("\n=== STATISTICAL TESTS ===")

    if target_col and target_col in df.columns and target_col in numeric_cols:
        print(f"\nTarget variable: {target_col}")
        for col in numeric_cols:
            if col == target_col:
                continue
            coef, p_value = stats.pearsonr(df[col].dropna(), df[target_col].dropna())
            print(f"{col} vs {target_col}: r={coef:.4f}, p={p_value:.4f}")

# ------------------------------------------------------------
# 10. REPORT GENERATION
# ------------------------------------------------------------
def generate_report(df, findings, target_col=None):
    numeric_cols, categorical_cols = separate_columns(df)

    report_lines = []
    report_lines.append("=" * 60)
    report_lines.append("EXPLORATORY DATA ANALYSIS (EDA) REPORT")
    report_lines.append("=" * 60)
    report_lines.append(f"\nDataset Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    report_lines.append("")
    
    report_lines.append("1. DATA QUALITY ASSESSMENT")
    report_lines.append("-" * 60)
    report_lines.append(f"   • Missing values: {df.isnull().sum().sum()}")
    report_lines.append(f"   • Duplicate rows: {df.duplicated().sum()}")
    report_lines.append(f"   • Data types: {df.dtypes.nunique()} different types")
    report_lines.append("")
    
    report_lines.append("2. DATASET OVERVIEW")
    report_lines.append("-" * 60)
    report_lines.append(f"   • Numeric columns ({len(numeric_cols)}): {', '.join(numeric_cols[:5])}")
    if len(numeric_cols) > 5:
        report_lines.append(f"     and {len(numeric_cols) - 5} more...")
    report_lines.append(f"   • Categorical columns ({len(categorical_cols)}): {', '.join(categorical_cols[:5])}")
    if len(categorical_cols) > 5:
        report_lines.append(f"     and {len(categorical_cols) - 5} more...")
    report_lines.append("")
    
    report_lines.append("3. SUMMARY STATISTICS (Numeric Columns)")
    report_lines.append("-" * 60)
    if numeric_cols:
        report_lines.append(df[numeric_cols].describe().round(2).to_string())
    report_lines.append("")
    
    report_lines.append("4. KEY FINDINGS & RELATIONSHIPS")
    report_lines.append("-" * 60)
    if findings:
        for i, item in enumerate(findings[:15], 1):
            if item["metric"] == "pearson_correlation":
                report_lines.append(
                    f"   {i}. {item['feature']}: Correlation = {item['value']:.4f} "
                    f"({item['interpretation']})"
                )
            else:
                report_lines.append(f"   {i}. {item['feature']}: {item['interpretation']}")
    else:
        report_lines.append("   • No strong relationships found in the current dataset.")
    report_lines.append("")
    
    report_lines.append("5. PATTERNS & TRENDS")
    report_lines.append("-" * 60)
    if numeric_cols:
        report_lines.append(f"   • Highest variance: {df[numeric_cols].var().idxmax()}")
        report_lines.append(f"   • Lowest variance: {df[numeric_cols].var().idxmin()}")
        report_lines.append(f"   • Most skewed: {df[numeric_cols].skew().abs().idxmax()}")
    if categorical_cols:
        report_lines.append(f"   • Most diverse category: {max(categorical_cols, key=lambda x: df[x].nunique())}")
    report_lines.append("")
    
    report_lines.append("6. RECOMMENDATIONS")
    report_lines.append("-" * 60)
    report_lines.append("   • Investigate outliers and extreme values in the data")
    report_lines.append("   • Validate discovered correlations with domain knowledge")
    report_lines.append("   • Explore missing value patterns and their causes")
    report_lines.append("   • Perform segmentation analysis for categorical variables")
    report_lines.append("   • Build predictive models using high-correlation features")
    report_lines.append("   • Consider feature engineering for improved insights")
    report_lines.append("")
    
    report_lines.append("7. VISUALIZATIONS GENERATED")
    report_lines.append("-" * 60)
    report_lines.append("   ✓ 01_numeric_distributions.png - Distribution of all numeric columns")
    report_lines.append("   ✓ 02_boxplots.png - Outlier detection with boxplots")
    report_lines.append("   ✓ 03_categorical_distributions.png - Category frequencies")
    report_lines.append("   ✓ 04_correlation_heatmap.png - Feature correlations")
    report_lines.append("   ✓ 05_pairplot.png - Pairwise relationships")
    report_lines.append("")
    report_lines.append("=" * 60)

    with open(OUTPUT_REPORT, "w") as f:
        f.write("\n".join(report_lines))

    print(f"\n✓ Report saved to: {OUTPUT_REPORT}")

    return "\n".join(report_lines)

# ------------------------------------------------------------
# 11. MAIN EXECUTION
# ------------------------------------------------------------
def main():
    # Create plots directory
    os.makedirs("plots", exist_ok=True)
    
    print("\n" + "=" * 60)
    print("STARTING EXPLORATORY DATA ANALYSIS (EDA)")
    print("=" * 60)
    
    df = load_data(DATA_PATH)
    basic_info(df)
    df = handle_missing_values(df)
    summary_statistics(df)

    numeric_cols, categorical_cols = separate_columns(df)

    # Visualizations
    print("\n\nGenerating visualizations...")
    plot_numeric_distributions(df, numeric_cols[:6])
    plot_boxplots(df, numeric_cols[:6])
    plot_categorical_distribution(df, categorical_cols[:6])
    plot_correlation_heatmap(df, numeric_cols)
    plot_pairplot(df, numeric_cols)

    # Statistical analysis
    run_statistical_tests(df, TARGET_COLUMN)

    # Relationships
    findings = analyze_relationships(df, TARGET_COLUMN)
    print("\n=== TOP RELATIONSHIPS ===")
    for item in findings[:10]:
        print(item)

    # Save report
    report = generate_report(df, findings, TARGET_COLUMN)
    print("\n" + "=" * 60)
    print("EDA ANALYSIS COMPLETE!")
    print("=" * 60)
    print(report)

if __name__ == "__main__":
    main()