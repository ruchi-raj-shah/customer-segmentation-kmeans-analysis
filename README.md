# ☕ Coffee Shop Customer Clustering

**K-Means Clustering Analysis for Customer Segmentation**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Overview

This project demonstrates **K-Means clustering** to segment coffee shop customers into distinct groups based on their purchasing behavior. The analysis includes data exploration, optimal cluster determination using both Elbow Method and Silhouette Score, visualization, and business insights.

**Perfect for:**
- 📚 Learning machine learning fundamentals
- 💼 Understanding customer segmentation
- 🎓 Academic projects (AIGC 5503)
- 💻 Building a portfolio project

---

## 🎯 Project Goals

✅ Implement K-Means clustering algorithm  
✅ Determine optimal number of clusters  
✅ Analyze and visualize customer segments  
✅ Extract business-actionable insights  
✅ Create reproducible analysis workflow  

---

## 📊 Dataset

**Source:** Synthetic coffee shop customer data  
**Size:** 50 customers  

### Features:
| Column | Type | Description |
|--------|------|-------------|
| `customer_id` | Integer | Unique customer identifier |
| `monthly_spend` | Float | Total spending per month ($) |
| `visit_frequency` | Integer | Number of visits per month |
| `avg_order_value` | Float | Average order value ($) |
| `loyalty_member` | Boolean | Loyalty program member (1/0) |

---

## 🔍 Analysis Steps

### 1️⃣ Data Preparation
- Load and explore customer data
- Standardize features using StandardScaler
- Handle any missing values

### 2️⃣ Determine Optimal k
- **Elbow Method:** Find the "elbow point" in WCSS curve
- **Silhouette Score:** Measure cluster cohesion & separation (-1 to +1)
- Compare both methods for final decision

### 3️⃣ Clustering
- Run K-Means with optimal k value
- Assign customers to clusters
- Calculate final silhouette score

### 4️⃣ Analysis & Visualization
- Analyze characteristics of each cluster
- Create 2D scatter plots with centroids
- Generate business insights

---

## 📈 Key Results

| Metric | Value |
|--------|-------|
| **Optimal k** | 3 clusters |
| **Final Silhouette Score** | 0.7123 |
| **Total Customers** | 50 |

### 🎯 Three Distinct Customer Segments:

#### **Cluster 0: Budget-Conscious Occasional Buyers** (30%)
- 💰 Avg Monthly Spend: $35.45
- 📍 Avg Visits/Month: 6.3
- 🎟️ Loyalty: 0%
- 📌 **Strategy:** Volume discounts, Happy Hour promotions, Entry-level products
- 💡 **Action:** Send weekly 20% off coupons

#### **Cluster 1: Premium Loyal Regulars** (36%)
- 💰 Avg Monthly Spend: $80.24
- 📍 Avg Visits/Month: 20.1
- 🎟️ Loyalty: 100%
- 📌 **Strategy:** VIP perks, Exclusive drinks, Priority service
- 💡 **Action:** Free premium drink monthly, priority ordering

#### **Cluster 2: Moderate Frequency Customers** (34%)
- 💰 Avg Monthly Spend: $48.57
- 📍 Avg Visits/Month: 11.4
- 🎟️ Loyalty: 15%
- 📌 **Strategy:** Loyalty rewards, Limited-time offers, Engagement programs
- 💡 **Action:** Bonus points campaigns, seasonal specials

---

## 🛠️ Technologies Used

```
Python 3.8+
├── pandas           # Data manipulation
├── numpy            # Numerical computing
├── scikit-learn     # Machine Learning (K-Means, metrics)
├── matplotlib       # Data visualization
└── seaborn          # Statistical visualization
```

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/coffee-shop-customer-clustering.git
cd coffee-shop-customer-clustering
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Verify Installation
```bash
python -c "import pandas, sklearn, matplotlib; print('✅ All packages installed!')"
```

---

## 🚀 How to Run

### Option A: Run Python Script
```bash
python kmeans_clustering.py
```

**Output:**
- Console output with cluster statistics
- 3 visualizations (Elbow Method, Silhouette Score, Clusters)
- CSV file: `clustered_customers.csv`

### Option B: Run Jupyter Notebook
```bash
jupyter notebook notebooks/kmeans_project.ipynb
```

Then click "Run All Cells" (or run cells individually)

---

## 📁 Project Structure

```
coffee-shop-customer-clustering/
│
├── README.md                          # ⭐ Project documentation
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Files to exclude from Git
│
├── kmeans_clustering.py               # Main Python script
├── coffee_customers.csv               # Input dataset
├── clustered_customers.csv            # Output with clusters
│
├── notebooks/
│   └── kmeans_project.ipynb           # Jupyter notebook
│
└── results/
    ├── elbow_method.png               # Elbow Method plot
    ├── silhouette_score.png           # Silhouette Score plot
    └── cluster_visualization.png      # Final clusters plot
```

---

## 📚 How It Works

### K-Means Algorithm Overview

```
Step 1: Initialize k random centroids
        ↓
Step 2: Assign each point to nearest centroid
        ↓
Step 3: Recalculate centroid positions
        ↓
Step 4: Repeat steps 2-3 until convergence
```

### Silhouette Score Explained

```
S(i) = (b - a) / max(a, b)

Where:
  a = average distance to points in same cluster (cohesion)
  b = average distance to points in nearest other cluster (separation)

Range: -1 to +1
  +1.0 = Perfect clustering
  0.0  = Overlapping clusters
  -1.0 = Wrong assignments
```

**Our Score: 0.7123** ✅ = Good cluster separation!

---

## 🔧 Key Code Sections

### Data Standardization
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# Ensures features have equal importance
```

### Finding Optimal k
```python
from sklearn.metrics import silhouette_score

for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, labels)
    # Higher score = better clustering
```

### Running Clustering
```python
kmeans_final = KMeans(n_clusters=3, random_state=42)
cluster_labels = kmeans_final.fit_predict(X_scaled)

df['cluster'] = cluster_labels
# Assign cluster to each customer
```

---

## 📊 Visualizations

### 1. Elbow Method
Shows WCSS (Within-Cluster Sum of Squares) vs number of clusters
- **Look for:** Point where curve flattens
- **Helps decide:** Optimal k value

### 2. Silhouette Score
Shows cluster quality metric for different k values
- **Range:** -1 to +1
- **Best:** k with highest score
- **Ours:** k=3 with score 0.7123

### 3. Cluster Plot
2D scatter plot with:
- 🟥 Red dots = Cluster 0 (Budget Buyers)
- 🟦 Blue dots = Cluster 1 (Premium Regulars)
- 🟩 Green dots = Cluster 2 (Moderate Customers)
- ⭐ Yellow stars = Cluster centers (centroids)

---

## 💡 Business Insights

### For Marketing Teams:
1. **Cluster 0 (Budget):** Target with discounts and value offers
2. **Cluster 1 (Premium):** Invest in retention and exclusive benefits
3. **Cluster 2 (Moderate):** Focus on engagement and cross-selling

### For Product Teams:
- Develop budget-friendly menu items for Cluster 0
- Create exclusive premium drinks for Cluster 1
- Introduce seasonal specials for Cluster 2

### For Finance Teams:
- Cluster 1 generates highest revenue (36% of customers, highest spend)
- Focus retention efforts on Cluster 1 (already 100% loyalty)
- Opportunity to upgrade Cluster 0 to mid-tier

---

## 📖 Learning Resources

**K-Means Clustering:**
- [Scikit-learn Documentation](https://scikit-learn.org/stable/modules/clustering.html#k-means)
- [K-Means Tutorial](https://towardsdatascience.com/k-means-clustering-from-scratch-in-python-45cee75b3e42)

**Silhouette Score:**
- [Understanding Silhouette Score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html)
- [Cluster Evaluation](https://towardsdatascience.com/silhouette-coefficient-validating-clustering-techniques-e976bb81d924)

**Data Science:**
- [Pandas Tutorial](https://pandas.pydata.org/docs/)
- [Scikit-learn Tutorial](https://scikit-learn.org/stable/modules/preprocessing.html)

---

## 🎓 Course Information

- **Course:** AIGC 5503 - AI for Business Decision Making
- **Institution:** Humber Polytechnic
- **Semester:** Spring 2026
- **Student ID:** N10020731

---

## 🤝 Contributing

Found a bug or want to improve this project?

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

You're free to use, modify, and distribute this project!

---

## 🙋 Questions & Support

**Having issues?**
- Check existing GitHub Issues
- Create a new Issue with detailed description
- Include error messages and Python version

**Want to learn more?**
- See `notebooks/kmeans_project.ipynb` for detailed walkthrough
- Check comments in `kmeans_clustering.py`
- Review the course materials in README

---

## 📌 Citation

If you use this project in your work, please cite:

```bibtex
@misc{kmeans_clustering_2026,
  title={Coffee Shop Customer Clustering using K-Means},
  author={Your Name},
  year={2026},
  publisher={GitHub},
  url={https://github.com/YOUR_USERNAME/coffee-shop-customer-clustering}
}
```

---

## ⭐ If This Helped You

Consider giving this repository a **star** ⭐ if it helped you learn!

---

**Last Updated:** June 2026  
**Status:** ✅ Complete & Ready for Use
