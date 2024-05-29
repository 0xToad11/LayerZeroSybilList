import pandas as pd

# Load the CSV files into pandas DataFrames
initial_list = pd.read_csv('initialList.csv')
merged_wallet_counts = pd.read_csv('testBridge/results/testBridgeTxRemoveDuplicates.csv')

# Extract the addresses from initial_list
addresses_to_remove = initial_list['ADDRESS'].tolist()

# Filter out rows from merged_wallet_counts where SENDER_WALLET is in addresses_to_remove
filtered_wallet_counts = merged_wallet_counts[~merged_wallet_counts['SENDER_WALLET'].isin(addresses_to_remove)]

# Further filter to keep only rows where the count is 10 or higher
# filtered_wallet_counts = filtered_wallet_counts[filtered_wallet_counts['count'] >= 20]

# Save the result to a new CSV file
filtered_wallet_counts.to_csv('finalListTestBridgeAmountTx.csv', index=False)

print("Filtered wallet counts have been saved to 'filtered_wallet_counts.csv'")
