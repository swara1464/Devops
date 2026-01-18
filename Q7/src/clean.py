import pandas as pd
import os

# Define paths
input_path = 'data/raw/data.csv'
output_dir = 'data/processed'
output_path = os.path.join(output_dir, 'cleaned_data.csv')

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

print(f"Reading data from {input_path}...")
df = pd.read_csv(input_path)

# Cleaning steps
print("Cleaning data...")
# 1. Drop rows with missing values
df = df.dropna()
# 2. Filter out invalid emails (simple check)
df = df[df['email'].str.contains('@')]

print(f"Cleaned data shape: {df.shape}")

# Save processed data
print(f"Saving cleaned data to {output_path}...")
df.to_csv(output_path, index=False)
print("Done!")
