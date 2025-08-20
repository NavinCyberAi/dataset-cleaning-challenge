# 📌 data_cleaning.py
# Simple program to load, check, and clean 6 datasets
# Human-readable version for easy understanding

import pandas as pd

# Step 1: File names (update path if needed)
files = {
    "PurchasePrices2017Dec": "2017PurchasePricesDec.csv",
    "BegInv2016": "BegInvFINAL12312016.csv",
    "EndInv2016": "EndInvFINAL12312016.csv",
    "InvoicePurchases2016": "InvoicePurchases12312016.csv",
    "Purchases2016": "PurchasesFINAL12312016.csv",
    "Sales2016": "SalesFINAL12312016.csv"
}

# Step 2: Read all datasets into a dictionary
datasets = {}
for name, file in files.items():
    try:
        print(f"\n Reading {file} ...")
        datasets[name] = pd.read_csv(file)
        print(f" Loaded {file} with {datasets[name].shape[0]} rows and {datasets[name].shape[1]} columns.")
    except Exception as e:
        print(f" Error loading {file}: {e}")

# Step 3: Check for missing values and duplicates
for name, df in datasets.items():
    print(f"\n Checking dataset: {name}")
    print("➡ Shape:", df.shape)
    print("➡ Missing values per column:\n", df.isnull().sum())
    print("➡ Total Duplicates:", df.duplicated().sum())

# Step 4: Fix missing values and duplicates
cleaned_datasets = {}
for name, df in datasets.items():
    # Remove duplicates
    df_cleaned = df.drop_duplicates()
    # Fill missing values (simple method: fill with "Unknown" or 0)
    df_cleaned = df_cleaned.fillna("Unknown")
    cleaned_datasets[name] = df_cleaned
    print(f"\n Cleaned dataset: {name}")
    print("➡ Shape after cleaning:", df_cleaned.shape)

# Step 5: Save cleaned files
for name, df in cleaned_datasets.items():
    out_file = f"cleaned_{name}.csv"
    df.to_csv(out_file, index=False)
    print(f" Saved {out_file}")
