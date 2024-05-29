import pandas as pd

# Read the existing CSV file with the ADDRESS column
existing_df = pd.read_csv('initialList.csv')

# Read the unique_senders.csv file
unique_senders_df = pd.read_csv('btcb/data4/Polygon_unique_senders.csv')

# Ensure columns are correctly named
assert 'ADDRESS' in existing_df.columns, "Existing CSV does not have column 'ADDRESS'"
assert 'SENDER_WALLET' in unique_senders_df.columns, "unique_senders CSV does not have column 'SENDER_WALLET'"

# Create a set of addresses from the existing DataFrame
existing_addresses_set = set(existing_df['ADDRESS'])

# Filter out addresses that are already in the existing file
new_addresses = unique_senders_df[~unique_senders_df['SENDER_WALLET'].isin(existing_addresses_set)]

# Rename the column in new_addresses to match the existing file
new_addresses = new_addresses.rename(columns={'SENDER_WALLET': 'ADDRESS'})

# Concatenate the existing addresses with the new unique addresses
updated_df = pd.concat([existing_df, new_addresses], ignore_index=True)

# Save the updated DataFrame back to the existing CSV file
updated_df.to_csv('initialList.csv', index=False)

print("Existing CSV file updated successfully.")
