import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('finalListFuseBridge.csv')

# Remove duplicate addresses in the SENDER_WALLET column
df_cleaned = df.drop_duplicates(subset='SENDER_WALLET')

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('cleaned_file.csv', index=False)

print("Duplicates have been removed and the cleaned file has been saved to 'cleaned_file.csv'")
