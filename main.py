import pandas as pd
from sqlalchemy import create_engine

file_name = 'project1-dataset.csv'
try:
    df = pd.read_csv(file_name)
    print(f"Successfully loaded {file_name}")
except FileNotFoundError:
    print(f"Error: {file_name} not found. Make sure it's in the same folder as main.py.")
    exit()


df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%m/%d/%Y')
print("Successfully converted Order Date and Ship Date to datetime.")


relevant_columns = [
    'Region', 
    'Country', 
    'Item_Type', 
    'Sales_Channel', 
    'Order_Date', 
    'Units_Sold', 
    'Total_Revenue', 
    'Total_Cost', 
    'Total_Profit'
]
df_cleaned = df[relevant_columns]
print(f"Selected {len(relevant_columns)} relevant columns.")


db_file = 'sales_data.db'
engine = create_engine(f'sqlite:///{db_file}')


df_cleaned.to_sql('sales', engine, if_exists='replace', index=False)

print(f"\n--- SUCCESS! ---")
print(f"Cleaned data has been saved to the table 'sales' in the file '{db_file}'.")
print("Phase 1 is complete.")