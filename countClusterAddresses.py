import pandas as pd

# Input and output file paths
input_file = 'results/onlyClusterAddresses.csv'
output_file = 'results/countClusterAddresses.csv'

# Read the CSV file
df = pd.read_csv(input_file)

# Count the occurrences of each unique wallet address
wallet_counts = df['SENDER_WALLET'].value_counts().reset_index()
wallet_counts.columns = ['SENDER_WALLET', 'count']

# Sort by count in descending order
wallet_counts = wallet_counts.sort_values(by='count', ascending=False)

# Save the result to a new CSV file
wallet_counts.to_csv(output_file, index=False)

print(f"Output saved to {output_file}")
