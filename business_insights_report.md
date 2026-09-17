# Business Insights Report – Sales Forecasting System

## 1. Project Overview

This project develops a Sales Forecasting System using historical monthly sales data. The system analyzes past sales trends and uses Linear Regression to forecast future sales for the next six months.

## 2. Dataset Details

* Dataset: Historical Monthly Sales Data
* Period: January 2024 to December 2025
* Total Records: 24
* Main Columns:

  * Date
  * Sales

## 3. Methodology

The following steps were performed:

1. Loaded the historical sales dataset using Pandas.
2. Converted the Date column into datetime format.
3. Checked for missing values and duplicate records.
4. Sorted the data according to date.
5. Analyzed monthly and yearly sales trends.
6. Created a time-based numerical index for forecasting.
7. Applied Linear Regression using Scikit-learn.
8. Forecasted sales for the next six months.
9. Visualized actual, predicted, and forecasted sales using Matplotlib.

## 4. Historical Sales Findings

* Lowest monthly sales were recorded in January 2024 with sales of 12,000.
* Highest monthly sales were recorded in December 2025 with sales of 25,000.
* Overall, the historical data shows an increasing sales trend from 2024 to 2025.
* Sales increased from the beginning of 2024 to the end of 2025, with some small monthly fluctuations.

## 5. Six-Month Sales Forecast

| Month         | Predicted Sales |
| ------------- | --------------: |
| January 2026  |       24,828.26 |
| February 2026 |       25,382.52 |
| March 2026    |       25,936.78 |
| April 2026    |       26,491.04 |
| May 2026      |       27,045.30 |
| June 2026     |       27,599.57 |

The model estimates a continued upward sales trend during the forecast period.

## 6. Business Insights

* The historical sales data indicates consistent growth over time.
* Forecasted sales continue to increase from January to June 2026.
* The increasing trend can help businesses plan inventory and resources.
* Sales forecasts can support future budgeting and operational planning.
* Regularly updating the model with new sales data can improve future forecasting analysis.

## 7. Business Recommendations

* Monitor monthly sales performance against forecasted values.
* Maintain sufficient inventory to support periods of increasing demand.
* Update the forecasting model regularly when new sales data becomes available.
* Use forecast results as estimates for planning rather than guaranteed future sales.
* Combine sales forecasts with other business factors such as promotions, seasonal demand, and market conditions.

## 8. Conclusion

The Sales Forecasting System successfully analyzes historical sales data and predicts future sales using Linear Regression. The forecast indicates a gradual increase in sales from January to June 2026. This project demonstrates how Python, Pandas, NumPy, Matplotlib, and Scikit-learn can be used to support data-driven business planning.
