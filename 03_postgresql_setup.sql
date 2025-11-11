-- 03_postgresql_setup.sql
-- PostgreSQL configuration for ETL target database

-- Create database
CREATE DATABASE adventureworks;

-- Switch to adventureworks before running the following
\c adventureworks;

-- Create ETL role
CREATE ROLE etl WITH LOGIN PASSWORD 'demopass';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE adventureworks TO etl;
GRANT USAGE, CREATE ON SCHEMA public TO etl;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO etl;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO etl;

-- Ensure privileges apply to future objects
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO etl;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO etl;
