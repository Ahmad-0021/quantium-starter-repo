import glob
import pandas as pd

# 1. Read and combine all 3 CSV files from the data folder
csv_files = glob.glob('data/*.csv')
df = pd.concat((pd.read_csv(file) for file in csv_files), ignore_index=True)

# 2. Filter for Pink Morsel data only
filtered_df = df[df['product'] == 'pink morsel'].copy()

# 3. Clean the price column (removes the '$' sign and converts to decimals)
filtered_df['price'] = filtered_df['price'].str.replace('$', '', regex=False).astype(float)

# 4. Calculate Sales (quantity * cleaned price)
filtered_df['Sales'] = filtered_df['quantity'] * filtered_df['price']

# 5. Extract only the three required columns
final_df = filtered_df[['Sales', 'date', 'region']]

# 6. Save the output to a clean CSV file
final_df.to_csv('formatted_output.csv', index=False)

print("Data processing complete! Saved to 'formatted_output.csv'.")
print(final_df.head())
