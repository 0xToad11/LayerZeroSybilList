import pandas as pd


# Read the CSV file
df = pd.read_csv('data/angle_numeric_dates.csv')

# Get unique values in the 'SOURCE_CHAIN' column
unique_source_chains = df['SOURCE_CHAIN'].unique()

# Iterate over unique source chains
for source_chain in unique_source_chains:
    # Filter the DataFrame for the current source chain
    source_chain_df = df[df['SOURCE_CHAIN'] == source_chain]
    
    # Save the filtered DataFrame to a CSV file
    output_file_path = f'data2/{source_chain}.csv'
    source_chain_df.to_csv(output_file_path, index=False)
    
    # Print a message indicating the file has been saved
    print(f"Saved the data for source chain '{source_chain}' to {output_file_path}")
