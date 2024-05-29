Description

This project aims to identify Sybil clusters within the LayerZero ecosystem. Using data provided by LayerZero, we first converted UTC timestamps to numeric date formats in seconds, facilitating analysis with the sklearn library. Initially, the data was filtered by individual protocols, and then further segmented by blockchain. The objective was to detect clusters of wallets engaging with the LayerZero protocol in a suspiciously synchronized manner, indicative of bot activity. Parameters for clustering were set with an EPS of 1, meaning transactions had to occur within 1 second of each other (basically same block), and a minimum cluster size of 10, meaning at least 10 wallets had to make identical transactions within that time frame (same block). This rigorous approach helps flag potential Sybil clusters.


Detailed Methodology & Walkthrough
Methodology:

1. **Data Preparation:**
   - Initially, the LayerZero data was organized into separate datasets per project, including Angle, AptosBridge, BtcB, Core, Gaszip, Harmony, Kingdom, L2marathon, L2pass, and L2telegraph. It is possible to add data from more protocols to filter out additional sybils.
   - Each project's data was then further divided based on the blockchain source.

2. **Timestamp Conversion:**
   - UTC timestamps were converted into a numeric format representing time in seconds. This conversion was essential for compatibility with the sklearn library, facilitating time-based analysis.

3. **Identification of Suspicious Clusters:**
   - The primary objective was to detect clusters of wallets interacting with a single protocol on a specific blockchain source within one blocktime.
   - The clustering algorithm parameters were set as follows:
     - EPS (epsilon) was set to 1, indicating that transactions needed to occur within 1 second of each other, effectively representing the same blocktime.
     - The minimum cluster size was set to 10, requiring at least 10 wallets to make identical interactions with the same protocol on the same source chain within the same blocktime. Such synchronized interactions are typically indicative of automated bot activity.

4. **Cluster Refinement:**
   - Duplicate addresses within clusters were removed to ensure accuracy.
   - Addresses that were already on the initial list from LayerZero have been removed.
   - Clusters smaller than 5 were eliminated from the analysis to minimize false positives.

5. **Sybil Detection:**
   - To further reduce false positives, addresses across all datasets were aggregated.
   - Addresses appearing more than three times across all datasets were flagged as potential Sybil wallets.

6. **Exclusion Criteria:**
   - Certain protocols, namely Merkly and Stargate, were excluded from the analysis. This decision was based on the high volume of transactions on these protocols, which could potentially lead to false positives when filtering transactions within the same blocktime, protocol, and source chain.
   - Emphasis was placed on smaller protocols to mitigate false positives. Cross-referencing data from multiple smaller protocols allowed for a more robust analysis.

7. **Stringent Criteria for Sybil Labeling:**
   - Only wallets exhibiting behavior consistent with bot activity were labeled as Sybil.
   - Criteria for identifying Sybil wallets included:
     - Activity across multiple protocols and chains.
     - Usage of more than 5 wallets within the same blocktime.
     - Occurrence of suspicious activity more than once.

Walkthrough:

1. **Data Segmentation:** 
   - The LayerZero data was divided into distinct projects and further segmented by blockchain source.

2. **Timestamp Conversion:**
   - UTC timestamps were transformed into numeric formats for time-based analysis.

3. **Clustering Analysis:**
   - Using sklearn, clusters of suspicious activities were identified based on predefined parameters.

4. **Refinement and Sybil Detection:**
   - Addresses that were already on the initial list from LayerZero have been removed.
   - Duplicate addresses were removed, and clusters smaller than 5 were discarded to refine the analysis.
   - Aggregating addresses and applying stringent criteria facilitated the detection of potential Sybil wallets.

6. **Exclusion of Certain Protocols:**
   - Protocols with high transaction volumes were excluded to prevent false positives.

7. **Final Evaluation:**
   - The methodology ensured thorough scrutiny of wallet activity, focusing on behaviors indicative of automated bot activity, thus minimizing the risk of false positives.

You can find the code for this project on my GitHub repository https://github.com/0xToad11/LayerZeroSybilList. While I haven't uploaded the CSV files directly, I have them all, including the intermediate steps/lists and the final list. If you need access to these files for verification or further analysis, feel free to reach out. The data is organized by clusters per protocol per source blockchain, along with a final list where they were cross-referenced for accuracy. This structure ensures transparency and allows for easy replication of the analysis.

I have taken a very conservative approach in my analysis to ensure accuracy. I hope this method meets your expectations. If you would prefer a less conservative approach or even more stringent criteria, please let me know. I can easily adjust the parameters to suit your needs. It is also possible to add data from more protocols to filter out additional sybils. (Right now limited to Angle, AptosBridge, BtcB, Core, Gaszip, Harmony, Kingdom, L2marathon, L2pass, and L2telegraph)

Reward Address (If Eligible)
0x14a61fD089E24732dEe4bBAC37fD8B5F28CD23a0

