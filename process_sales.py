import pandas as pd
import glob

# Step 1: Load all CSV files from the data folder
csv_files = glob.glob('data/*.csv')  # Make sure your CSVs are inside a folder named 'data'

df_list = []
for file in csv_files:
    df = pd.read_csv(file)
    df_list.append(df)

# Step 2: Combine all CSVs into one DataFrame
all_data = pd.concat(df_list, ignore_index=True)

# Step 3: Filter only Pink Morsels
pink_morsels = all_data[all_data['product'] == 'Pink Morsel']

# Step 4: Calculate total sales
pink_morsels['sales'] = pink_morsels['quantity'] * pink_morsels['price']

# Step 5: Keep only the required columns
final_data = pink_morsels[['sales', 'date', 'region']]

# Step 6: Save to a new CSV
final_data.to_csv('formatted_sales.csv', index=False)

print("Formatted CSV created successfully!")
