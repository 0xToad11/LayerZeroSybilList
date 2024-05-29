import pandas as pd

# Set the chunk size
chunk_size = 1000000
file_path = 'snapshot1_transactions.csv'
output_file_path = 'testBridge/data/testBridge_txs.csv'

# Open the CSV file in chunks
for i, chunk in enumerate(pd.read_csv(file_path, chunksize=chunk_size)):
    print(f"Processing rows {i*chunk_size}-{(i+1)*chunk_size}...")

    # Drop rows with missing values in the 'PROJECT' column
    chunk = chunk.dropna(subset=['PROJECT'])

    # Search for rows with "fuse bridge" in the PROJECT column within the subset
    fuse_bridge_rows = chunk[chunk['PROJECT'].str.contains('Testnet', na=False, case=False)]

    # Append the matching rows to the CSV file
    fuse_bridge_rows.to_csv(output_file_path, mode='a', index=False, header=not i)

    print(f"Finished processing rows {i*chunk_size}-{(i+1)*chunk_size}. Appended results to {output_file_path}")

print("Processing complete.")
