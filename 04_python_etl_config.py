# 04_python_etl_config.py
# Configuration file for ETL connections

SQL_SERVER_CONFIG = {
    "server": "DESKTOP-XXXX\\SQLEXPRESS",
    "database": "AdventureWorksDW2022",
    "username": "etl",
    "password": "demopass",
    "driver": "ODBC Driver 17 for SQL Server"
}

POSTGRES_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "adventureworks",
    "user": "etl",
    "password": "demopass"
}
