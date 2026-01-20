import pandas as pd

# Load Excel file
file_path = "../data/Exp_3_VBOX_Data.xlsx"

# Read sheets 7, 8, and 9
sheets_to_use = ['7', '8', '9']
df_list = [pd.read_excel(file_path, sheet_name=sheet) for sheet in sheets_to_use]

# Combine data
df = pd.concat(df_list, ignore_index=True)

# Keep relevant columns
df = df[['Speed (kmph)', 'Time']]

# Drop missing values
df.dropna(inplace=True)

# Ensure correct data types
df['Speed (kmph)'] = pd.to_numeric(df['Speed (kmph)'], errors='coerce')
df['Time'] = pd.to_numeric(df['Time'], errors='coerce')

# Remove invalid values
df = df[df['Speed (kmph)'] >= 0]

print("Data cleaning completed. Rows after cleaning:", len(df))
