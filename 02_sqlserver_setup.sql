-- 02_sqlserver_setup.sql
-- SQL Server configuration for ETL user and database restoration

USE master;
GO

-- Restore AdventureWorks database manually via SSMS before running this

-- Create login for ETL operations
CREATE LOGIN etl WITH PASSWORD = 'demopass', DEFAULT_DATABASE = AdventureWorksDW2022;
GO

USE AdventureWorksDW2022;
GO

-- Create database user mapped to login
CREATE USER etl FOR LOGIN etl;
GRANT CONNECT TO etl;
GO

-- Optional: Grant read permissions for ETL user
GRANT SELECT ON SCHEMA::dbo TO etl;
GO
