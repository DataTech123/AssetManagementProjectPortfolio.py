import pandas as pd

# Example,data source connects to an internal asset management at cost and use.
data = {
    'Asset_Account_ID': [1, 2, 3, 4, 5],
    'Name': ['Asset1', 'Asset2', 'Asset3', 'Asset4', 'Asset5'],
    'Depreciation_Value': [100, 200, 150, 180, 220],
    'Cost': [1000, 1500, 1200, 1300, 1600]
}
# Create a dataframe from existing data.
df = pd.DataFrame(data)

# Calculate a net book value of each asset.
df['NBV'] = df['Cost'] - df['Depreciation_Value']

# Calculate a total cost, total depreciation value, and total.
total_cost = df['Cost'].sum()
total_depreciation_value = df['Depreciation_Value'].sum()
total_nbv = df['NBV'].sum()

# Display dataframe and total.
print("Asset Table:")
print(df)
print("\nTotal Cost:", total_cost)
print("Total Depreciation Value:", total_depreciation_value)
print("Total Net Book Value(NBV):", total_nbv)