# Sybil Hunting with LayerZero Data

## Project Overview

This project aims to identify Sybil clusters within the LayerZero ecosystem. Using data provided by LayerZero, we divided the dataset by individual projects and converted UTC timestamps to a more suitable format for analysis. Subsequently, the data was segmented by blockchain. Leveraging the `sklearn` clustering library, we identified clusters of suspicious activities, ultimately flagging potential Sybil clusters.

## Methodology

### Data Preparation

1. **Data Segmentation**:
    - The initial dataset from LayerZero was divided into 12 separate projects.
    - Each project's data was further split based on the blockchain.

2. **Timestamp Conversion**:
    - UTC timestamps in the dataset were converted to a more analysis-friendly format.

### Clustering Analysis

1. **Library Utilization**:
    - The `sklearn` library's clustering algorithms were employed to detect clusters of suspicious activities.

2. **Parameter Setting**:
    - **Minimum Cluster Size**: Set to 20. Only clusters with 20 or more data points were considered.
    - **EPS (Epsilon)**: Set to 100. This parameter defines the maximum distance between two samples for them to be considered as in the same neighborhood.

3. **Cluster Identification**:
    - Clustering was performed individually for each project's data. Data was seperated by project and then by blockchain. Clustering identification was based on a small time window where the same wallets repeatedly interacted with a certain project on a certain blockchain.

### Results Aggregation

1. **Result Merging**:
    - Results from the 12 projects and all their txs on the different blockchains were combined to create a comprehensive list of wallets identified as part of a cluster.

2. **Cluster Count Calculation**:
    - For each wallet, the number of times it was categorized as part of a cluster was calculated.

3. **Threshold Setting**:
    - A threshold of 20 was established. Wallets flagged as part of a cluster at least 20 times were deemed Sybil clusters. (being flagged once was already a clear sign of being a sybil, 20 times being flagged is extensive)

## Why This Method is Effective

1. **Focused Analysis**:
    - By dividing the data by projects and blockchains, we ensure that the clustering analysis is more precise and context-specific.

2. **Robust Clustering Parameters**:
    - Setting a minimum cluster size and EPS ensures that only significant clusters are identified, reducing noise and false positives.

3. **Comprehensive Aggregation**:
    - Combining results across multiple projects and blockchains and applying a threshold adds a layer of verification, ensuring that only consistently flagged wallets are marked as Sybil clusters.

4. **Threshold Accuracy**:
    - Setting a threshold at 20 for cluster occurrences ensures high confidence in the identification of Sybil clusters, balancing accuracy and safety.

## Conclusion

This project offers a structured and methodical approach to identifying Sybil clusters within the LayerZero ecosystem. By leveraging robust data segmentation, precise clustering parameters, and thorough result aggregation, we ensure reliable detection of Sybil activities. This methodology provides a strong foundation for further analysis and mitigation of Sybil attacks.