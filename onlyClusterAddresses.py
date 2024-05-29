import pandas as pd
import os

# Input directory
input_dir = 'data3'

# Output file path
output_file = 'results/onlyClusterAddresses.csv'

# Create the output directory if it does not exist
os.makedirs('results', exist_ok=True)

# Get the list of all CSV files in the input directory
input_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.csv')]

# Initialize an empty DataFrame to collect the results
result_df = pd.DataFrame(columns=['SENDER_WALLET'])

# Process each input file
for file in input_files:
    try:
        # Read the CSV file
        df = pd.read_csv(file)
        
        # Filter rows where Cluster_Label is not -1
        filtered_df = df[df['Cluster_Label'] != -1]
        
        # Append the SENDER_WALLET column to the result DataFrame
        result_df = pd.concat([result_df, filtered_df[['SENDER_WALLET']]], ignore_index=True)
    
    except Exception as e:
        print(f"An error occurred while processing {file}: {e}")

# Save the result to the output file
result_df.to_csv(output_file, index=False)

print(f"Output saved to {output_file}")
