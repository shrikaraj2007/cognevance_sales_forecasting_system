# Sales Forecasting System

## Project Overview

This project builds a Sales Forecasting System using historical monthly sales data. The system analyzes past sales trends and uses Linear Regression to predict future sales.

## Objectives

- Analyze historical sales data
- Clean and preprocess the dataset
- Identify monthly and yearly sales trends
- Build a sales forecasting model
- Predict future sales
- Visualize actual and forecasted sales
- Generate useful business insights

## Dataset

The dataset contains monthly sales records from January 2024 to December 2025.

- Total Records: 24
- Columns: Date, Sales

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Linear Regression

## Project Workflow

1. Create and collect historical sales data.
2. Clean and preprocess the data.
3. Analyze monthly and yearly sales trends.
4. Create a time-based index.
5. Train a Linear Regression model.
6. Forecast sales for the next six months.
7. Visualize the forecasting results.
8. Generate business insights.

## Historical Findings

- Lowest monthly sales: 12,000 in January 2024.
- Highest monthly sales: 25,000 in December 2025.
- Sales show an overall increasing trend from 2024 to 2025.

## Sales Forecast

The model forecasts the following sales for the next six months:

| Month | Predicted Sales |
|---|---:|
| January 2026 | 24,828.26 |
| February 2026 | 25,382.52 |
| March 2026 | 25,936.78 |
| April 2026 | 26,491.04 |
| May 2026 | 27,045.30 |
| June 2026 | 27,599.57 |

## Visualization

The project includes a chart showing actual sales, predicted sales, and future sales forecasts.

File:

`sales_forecast_chart.png`

## Business Insights

- Historical sales show a consistent upward trend.
- Forecasted sales continue to increase during January–June 2026.
- Forecast results can support inventory and resource planning.
- Regular model updates can improve future forecasting analysis.

## Project Files

- `create_dataset.py` – Creates the sales dataset
- `sales_data.csv` – Historical sales data
- `analysis.py` – Data cleaning and sales analysis
- `cleaned_sales_data.csv` – Cleaned dataset
- `forecast.py` – Linear Regression forecasting model
- `sales_forecast.csv` – Future sales predictions
- `sales_forecast_chart.png` – Forecast visualization
- `business_insights_report.md` – Business insights report
- `README.md` – Project documentation

## Conclusion

The Sales Forecasting System successfully analyzes historical sales data and predicts future sales using Linear Regression. The project demonstrates how Python and data analysis tools can be used for forecasting and business planning.

Note: Forecast values are model-based estimates and are not guaranteed future sales.