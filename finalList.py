import pandas as pd

# Function to process individual CSV files
def process_csv(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Group by SENDER_WALLET and sum the counts
    df = df.groupby('SENDER_WALLET')['COUNT'].sum().reset_index()

    return df

# List of file paths
file_paths = [
    "angle/results/final_unique_senders.csv",
    "aptosBridge/results/final_unique_senders.csv",
    "btcb/results/final_unique_senders.csv",
    "core/results/final_unique_senders.csv",
    "gaszip/results/final_unique_senders.csv",
    "harmony/results/final_unique_senders.csv",
    "kingdom/results/final_unique_senders.csv",
    "l2marathon/results/final_unique_senders.csv",
    "l2pass/results/final_unique_senders.csv",
    "l2telegraph/results/final_unique_senders.csv",
]

# Initialize an empty DataFrame to store the concatenated data
final_df = pd.DataFrame()

# Iterate over the file paths
for file_path in file_paths:
    # Process the CSV file
    df = process_csv(file_path)

    # Concatenate the processed DataFrame with the final DataFrame
    final_df = pd.concat([final_df, df], ignore_index=True)

# Remove duplicates based on SENDER_WALLET
final_df = final_df.groupby('SENDER_WALLET')['COUNT'].sum().reset_index()

# Filter out rows where COUNT is higher than 1
final_df = final_df[final_df['COUNT'] > 2]

# Sort the final DataFrame by COUNT in descending order
final_df = final_df.sort_values(by='COUNT', ascending=False)

# Save the final DataFrame to a CSV file
final_df.to_csv('final_counts.csv', index=False)

print("Final CSV file created successfully.")
