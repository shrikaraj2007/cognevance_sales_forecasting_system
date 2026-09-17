import pandas as pd

# Historical monthly sales data
data = {
    "Date": pd.date_range(start="2024-01-01", periods=24, freq="MS"),
    "Sales": [
        12000, 12500, 13200, 12800, 14000, 14500,
        15000, 14800, 15500, 16200, 17000, 17800,
        18000, 18500, 19200, 18800, 20000, 20800,
        21500, 22000, 22800, 23500, 24200, 25000
    ]
}

df = pd.DataFrame(data)

# Save dataset
df.to_csv("sales_data.csv", index=False)

print("Sales dataset created successfully!")
print("\nDataset:")
print(df)

print("\nDataset Shape:", df.shape)
