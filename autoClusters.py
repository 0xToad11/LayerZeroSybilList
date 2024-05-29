import os
import pandas as pd
from sklearn.cluster import DBSCAN

# Input and output directories
input_dir = 'data2'
output_dir = 'data3'

# Create the output directory if it does not exist
os.makedirs(output_dir, exist_ok=True)

# List all CSV files in the input directory
input_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

# Process each CSV file
for input_file in input_files:
    try:
        # Construct full file path
        input_path = os.path.join(input_dir, input_file)
        
        # Read the CSV file
        df = pd.read_csv(input_path)
        
        # Check if the DataFrame is empty
        if df.empty:
            print(f"{input_file} is empty. Skipping.")
            continue
        
        # Extract the numeric timestamps
        timestamps = df['SOURCE_TIMESTAMP_NUMERIC'].values.reshape(-1, 1)
        
        # Define DBSCAN parameters
        eps = 1  # maximum distance between two samples to be considered as neighbors (300 seconds = 5 minutes)
        min_samples = 10  # minimum number of samples in a cluster
        
        # Initialize DBSCAN
        dbscan = DBSCAN(eps=eps, min_samples=min_samples)
        
        # Fit DBSCAN to the data
        dbscan.fit(timestamps)
        
        # Get cluster labels (-1 represents noise)
        labels = dbscan.labels_
        
        # Add cluster labels to the DataFrame
        df['Cluster_Label'] = labels

        # Filter out noise points (cluster label = -1)
        clustered_df = df[df['Cluster_Label'] != -1]
        
        # Sort clusters by cluster label in descending order
        sorted_clusters = clustered_df.sort_values(by='Cluster_Label', ascending=False)
        
        # # Sort clusters by cluster label in descending order
        # sorted_clusters = df.sort_values(by='Cluster_Label', ascending=False)
        
        # Construct the output file name
        output_file = f"{os.path.splitext(input_file)[0]}_cluster.csv"
        output_path = os.path.join(output_dir, output_file)
        
        # Save the sorted DataFrame to the new CSV file
        sorted_clusters.to_csv(output_path, index=False)

        print(f"Processed {input_file} and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred while processing {input_file}: {e}")
