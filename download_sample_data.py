"""
Script to download sample datasets for EDA practice
Choose from:
1. Iris Dataset
2. Titanic Dataset
3. Wine Dataset
4. Breast Cancer Dataset
5. Customers Dataset
6. Sales Dataset
"""

import pandas as pd
import numpy as np
import os

def download_iris():
    """Download Iris dataset"""
    from sklearn import datasets
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    df.to_csv('data.csv', index=False)
    print("✓ Iris dataset downloaded: data.csv")
    print(f"  Shape: {df.shape}")

def download_titanic():
    """Download Titanic dataset"""
    url = "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv"
    df = pd.read_csv(url)
    df.to_csv('data.csv', index=False)
    print("✓ Titanic dataset downloaded: data.csv")
    print(f"  Shape: {df.shape}")

def download_wine():
    """Download Wine dataset"""
    from sklearn import datasets
    wine = datasets.load_wine()
    df = pd.DataFrame(wine.data, columns=wine.feature_names)
    df['target'] = wine.target
    df.to_csv('data.csv', index=False)
    print("✓ Wine dataset downloaded: data.csv")
    print(f"  Shape: {df.shape}")

def download_breast_cancer():
    """Download Breast Cancer dataset"""
    from sklearn import datasets
    cancer = datasets.load_breast_cancer()
    df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
    df['target'] = cancer.target
    df.to_csv('data.csv', index=False)
    print("✓ Breast Cancer dataset downloaded: data.csv")
    print(f"  Shape: {df.shape}")

def download_custom_customers():
    """Generate sample customers dataset"""
    np.random.seed(42)
    n_samples = 1000
    
    data = {
        'CustomerID': range(1, n_samples + 1),
        'Age': np.random.randint(18, 80, n_samples),
        'Income': np.random.randint(20000, 150000, n_samples),
        'Purchase_Amount': np.random.uniform(10, 1000, n_samples),
        'Years_Customer': np.random.randint(0, 20, n_samples),
        'Visits_Per_Month': np.random.randint(0, 30, n_samples),
        'Country': np.random.choice(['USA', 'UK', 'Canada', 'India', 'Australia'], n_samples),
        'Gender': np.random.choice(['Male', 'Female'], n_samples),
        'Premium_Member': np.random.choice(['Yes', 'No'], n_samples)
    }
    
    df = pd.DataFrame(data)
    df.to_csv('data.csv', index=False)
    print("✓ Customer dataset generated: data.csv")
    print(f"  Shape: {df.shape}")

def download_custom_sales():
    """Generate sample sales dataset"""
    np.random.seed(42)
    n_samples = 500
    
    data = {
        'Date': pd.date_range('2022-01-01', periods=n_samples, freq='D'),
        'Product': np.random.choice(['Laptop', 'Phone', 'Tablet', 'Headphones'], n_samples),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], n_samples),
        'Sales': np.random.uniform(100, 5000, n_samples),
        'Quantity': np.random.randint(1, 50, n_samples),
        'Profit': np.random.uniform(10, 1000, n_samples),
        'Customer_Satisfaction': np.random.uniform(1, 5, n_samples)
    }
    
    df = pd.DataFrame(data)
    df['Date'] = df['Date'].astype(str)
    df.to_csv('data.csv', index=False)
    print("✓ Sales dataset generated: data.csv")
    print(f"  Shape: {df.shape}")

def main():
    
    print("\n" + "=" * 60)
    print("DOWNLOAD SAMPLE DATASETS FOR EDA")
    print("=" * 60)
    print("\nChoose a dataset:")
    print("1. Iris Dataset (Flower measurements)")
    print("2. Titanic Dataset (Passenger survival)")
    print("3. Wine Dataset (Wine classification)")
    print("4. Breast Cancer Dataset (Medical data)")
    print("5. Customer Dataset (Generated)")
    print("6. Sales Dataset (Generated)")
    print("\n" + "-" * 60)
    
    choice = input("Enter your choice (1-6): ").strip()
    
    if choice == '1':
        download_iris()
    elif choice == '2':
        download_titanic()
    elif choice == '3':
        download_wine()
    elif choice == '4':
        download_breast_cancer()
    elif choice == '5':
        download_custom_customers()
    elif choice == '6':
        download_custom_sales()
    else:
        print("Invalid choice. Downloading Iris dataset by default...")
        download_iris()
    
    print("\n✓ Dataset ready! Run: python eda_analysis.py")
    print("=" * 60)

if __name__ == "__main__":
    main()