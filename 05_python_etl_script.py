# 05_python_etl_script.py
# Python ETL script: Extract data from SQL Server → Transform → Load into PostgreSQL

import pandas as pd
import pyodbc
from sqlalchemy import create_engine
from 04_python_etl_config import SQL_SERVER_CONFIG, POSTGRES_CONFIG

# --- Extract Stage ---
def extract_data():
    print("Connecting to SQL Server...")
    conn_str = (
        f"DRIVER={{{SQL_SERVER_CONFIG['driver']}}};"
        f"SERVER={SQL_SERVER_CONFIG['server']};"
        f"DATABASE={SQL_SERVER_CONFIG['database']};"
        f"UID={SQL_SERVER_CONFIG['username']};"
        f"PWD={SQL_SERVER_CONFIG['password']}"
    )
    cnxn = pyodbc.connect(conn_str)
    query = "SELECT TOP 1000 * FROM dbo.FactInternetSales"
    df = pd.read_sql(query, cnxn)
    print(f"Extracted {len(df)} records from SQL Server.")
    return df

# --- Transform Stage ---
def transform_data(df):
    print("Transforming data...")
    df["SalesAmount"] = df["SalesAmount"].astype(float)
    df["ExtractedDate"] = pd.Timestamp.now()
    print("Transformation complete.")
    return df

# --- Load Stage ---
def load_data(df):
    print("Loading data into PostgreSQL...")
    postgres_url = (
        f"postgresql+psycopg2://{POSTGRES_CONFIG['user']}:{POSTGRES_CONFIG['password']}@"
        f"{POSTGRES_CONFIG['host']}:{POSTGRES_CONFIG['port']}/{POSTGRES_CONFIG['database']}"
    )
    engine = create_engine(postgres_url)
    df.to_sql("stg_factinternetsales", engine, if_exists="replace", index=False)
    print("Data loaded successfully.")

# --- Main ETL Process ---
if __name__ == "__main__":
    df_extracted = extract_data()
    df_transformed = transform_data(df_extracted)
    load_data(df_transformed)
    print("ETL process completed successfully.")
