# 🧠 Building a Basic ETL Data Pipeline Using Python

## 📘 Overview
This project demonstrates a **Basic ETL (Extract, Transform, Load) pipeline** built using **Python**, **SQL Server**, and **PostgreSQL**.  
It guides through setting up databases, creating ETL users, writing ETL scripts, and validating data migration between SQL Server and PostgreSQL.

---

## 🎯 Objectives
1. Install and configure SQL Server Express, SSMS, PostgreSQL, and pgAdmin.
2. Restore and work with the **AdventureWorksDW2022** sample database.
3. Create and manage **ETL roles and users** with proper privileges.
4. Perform ETL tasks using Python with:
   - `pandas`
   - `sqlalchemy`
   - `psycopg2`
   - `pyodbc`
5. Extract data from SQL Server, transform it in Python, and load it into PostgreSQL.
6. Validate the transferred data in pgAdmin.

---

## 🧰 Prerequisites

### Software Required
- **SQL Server Express + SSMS**
- **PostgreSQL + pgAdmin**
- **Python 3.9+**
- **ODBC Driver 17 for SQL Server**
- **AdventureWorksDW2022** sample database (.bak file)

### Python Libraries
Install the required libraries:
```bash
pip install pandas sqlalchemy psycopg2-binary pyodbc
