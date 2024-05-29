import os
import pandas as pd

# Function to process individual CSV files
def process_csv(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Remove duplicates based on SENDER_WALLET
    df = df.drop_duplicates(subset='SENDER_WALLET')

    return df

# Path to the folder containing CSV files
folder_path = 'data4'

# Initialize an empty DataFrame to store the concatenated data
final_df = pd.DataFrame()

# Iterate over all files in the folder
for file in os.listdir(folder_path):
    # Check if the file is a CSV file and contains 'unique' in its name
    if file.endswith('.csv') and 'unique' in file:
        file_path = os.path.join(folder_path, file)
        
        # Process the CSV file
        df = process_csv(file_path)

        # Concatenate the processed DataFrame with the final DataFrame
        final_df = pd.concat([final_df, df], ignore_index=True)

# Count occurrences of each SENDER_WALLET to identify clusters
cluster_counts = final_df['SENDER_WALLET'].value_counts()


# Add a COUNT column to track occurrences of each SENDER_WALLET across CSV files
final_df['COUNT'] = final_df.groupby('SENDER_WALLET')['SENDER_WALLET'].transform('size')

# Sort the final DataFrame by COUNT in descending order
final_df = final_df.sort_values(by='COUNT', ascending=False)

# Save the final DataFrame to a CSV file
final_df.to_csv('results/final_unique_senders.csv', index=False)

print("Final CSV file created successfully.")
