import pandas as pd
from sqlalchemy import create_engine



db_file = 'sales_data.db'
table_name = 'sales'
export_csv_file = 'sales_export.csv'

engine = create_engine(f'sqlite:///{db_file}')

print(f"Connecting to database '{db_file}'...")

try:

    df = pd.read_sql_table(table_name, engine)
    
    print(f"Successfully read {len(df)} rows from table '{table_name}'.")

 
    df.to_csv(export_csv_file, index=False)
    
    print(f"\n--- SUCCESS! ---")
    print(f"Data exported to '{export_csv_file}'.")
    print("Phase 3 (Export) is complete. You can now open this CSV in Excel.")

except Exception as e:
    print(f"\n--- ERROR ---")
    print(f"An error occurred: {e}")
    print("Make sure 'sales_data.db' exists and 'sales' table is correct.")