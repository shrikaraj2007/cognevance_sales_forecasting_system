
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load cleaned sales data
df = pd.read_csv("cleaned_sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
# Create time index
df["Month_Number"] = range(1, len(df) + 1)

# Prepare data
X = df[["Month_Number"]]
y = df["Sales"]

# Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Predict historical sales
df["Predicted_Sales"] = model.predict(X)

# Forecast next 6 months
future_months = range(len(df) + 1, len(df) + 7)

future_df = pd.DataFrame({
    "Month_Number": future_months
})

future_df["Predicted_Sales"] = model.predict(
    future_df[["Month_Number"]]
)

# Create future dates
last_date = pd.to_datetime(df["Date"].iloc[-1])

future_df["Date"] = pd.date_range(
    start=last_date + pd.DateOffset(months=1),
    periods=6,
    freq="MS"
)

print("Next 6 Months Sales Forecast:")
print(future_df[["Date", "Predicted_Sales"]])

# Save forecast results
future_df[["Date", "Predicted_Sales"]].to_csv(
    "sales_forecast.csv",
    index=False
)

# Plot actual and predicted sales
plt.figure(figsize=(10, 5))

plt.plot(
    df["Date"],
    df["Sales"],
    marker="o",
    label="Actual Sales"
)

plt.plot(
    df["Date"],
    df["Predicted_Sales"],
    linestyle="--",
    label="Predicted Sales"
)

plt.plot(
    future_df["Date"],
    future_df["Predicted_Sales"],
    marker="o",
    linestyle="--",
    label="Forecast"
)

plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Sales Forecasting using Linear Regression")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("sales_forecast_chart.png")
plt.close()

print("\nForecast chart created successfully!")
print("Forecast data saved successfully!")
