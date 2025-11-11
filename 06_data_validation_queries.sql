-- 06_data_validation_queries.sql
-- Validate data in PostgreSQL after ETL

-- Check if table exists
SELECT table_name FROM information_schema.tables
WHERE table_schema = 'public';

-- Count records in loaded table
SELECT COUNT(*) FROM stg_factinternetsales;

-- View sample data
SELECT * FROM stg_factinternetsales LIMIT 10;

-- Optional: Aggregation example
SELECT
    ProductKey,
    SUM(SalesAmount) AS total_sales
FROM stg_factinternetsales
GROUP BY ProductKey
ORDER BY total_sales DESC
LIMIT 5;
