# Requirements Document – Basic ETL Data Pipeline

## Business Problem
We want to analyze sales and customer feedback to identify:
**"What are the top 5 products by revenue in the last quarter, and how does customer sentiment vary for these products?"**

## Data Sources
1. **sales_data_raw.csv** – contains sales transactions
2. **customer_feedback.json** – contains customer comments and ratings

## Required Data Points
- product_id  
- product_name  
- sale_price  
- sale_date  
- customer_id  
- sentiment_score

## Desired Output
A summarized table/report showing:
| Product ID | Product Name | Total Revenue | Average Sentiment | Rank |
|-------------|---------------|----------------|-------------------|------|

## Outcome
Enable business stakeholders to:
- Identify high-performing products
- Understand customer perception
- Support marketing and inventory decisions
