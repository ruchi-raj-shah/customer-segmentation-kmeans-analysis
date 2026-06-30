# customer-segmentation-kmeans-analysis
Customer segmentation using K-Means clustering for coffee shop business analysis

# Coffee Shop Customer Clustering

## Overview
This project performs customer segmentation analysis using K-Means clustering algorithm to identify distinct customer groups in a coffee shop dataset.

## Course Information
- **Course:** AIGC 5503 - AI for Business Decision Making
- **Institution:** Humber Polytechnic
- **Semester:** Spring 2026

## Project Goals
✅ Implement K-Means clustering algorithm
✅ Determine optimal number of clusters using Elbow Method and Silhouette Score
✅ Analyze customer segments for marketing insights
✅ Create visualizations of cluster distribution

## Dataset
- **Customers:** 50
- **Features:** monthly_spend, visit_frequency, avg_order_value, loyalty_member

## Results
- **Optimal k:** 3 clusters
- **Silhouette Score:** 0.7123

## Clusters Identified
1. **Budget-Conscious Occasional Buyers** (30%)
   - Low spend, infrequent visits
   - Strategy: Discount promotions

2. **Premium Loyal Regulars** (36%)
   - High spend, frequent visits
   - Strategy: VIP perks & exclusive offers

3. **Moderate Frequency Customers** (34%)
   - Medium spend, moderate visits
   - Strategy: Loyalty rewards programs

## Technologies Used
- Python 3.x
- Pandas (data manipulation)
- Scikit-learn (K-Means, metrics)
- Matplotlib & Seaborn (visualization)

## Files
- `coffee_customers.csv` - Original dataset
- `kmeans_clustering.py` - Main Python script
- `clustered_customers.csv` - Results with cluster assignments
- `analysis.ipynb` - Jupyter notebook with analysis

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Ensure `coffee_customers.csv` is in the same directory
3. Run: `python kmeans_clustering.py`
4. Or open `analysis.ipynb` in Jupyter Notebook

## Key Findings
- Three distinct customer segments identified
- Cluster 1 (Premiums) has highest lifetime value
- Cluster 0 (Budget) needs engagement strategies
- Silhouette score (0.71) indicates good cluster separation

## Author
Your Name (Student ID: N10020731)

## License
MIT License - Feel free to use and modify
