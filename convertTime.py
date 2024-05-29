import pandas as pd

# Read the CSV file
df = pd.read_csv('data/angle_txs.csv')

# Convert the date column to timestamps
df['SOURCE_TIMESTAMP_UTC'] = pd.to_datetime(df['SOURCE_TIMESTAMP_UTC'])

# Convert timestamps to numeric values (seconds since the epoch)
df['SOURCE_TIMESTAMP_NUMERIC'] = (df['SOURCE_TIMESTAMP_UTC'] - pd.Timestamp("1970-01-01")) // pd.Timedelta(seconds=1)

df_sorted = df.sort_values(by='SOURCE_TIMESTAMP_NUMERIC')

# Save the modified DataFrame to a new CSV file
df.to_csv('data/angle_numeric_dates.csv', index=False)
