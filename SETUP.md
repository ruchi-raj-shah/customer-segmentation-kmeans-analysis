# 🚀 Quick Start Guide

## 5-Minute Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/coffee-shop-customer-clustering.git
cd coffee-shop-customer-clustering
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Analysis
```bash
python kmeans_clustering.py
```

**That's it!** You should see:
- ✅ Cluster analysis output
- 📊 3 visualization plots
- 📁 `clustered_customers.csv` file with results

---

## 📖 Alternative: Run with Jupyter Notebook

```bash
jupyter notebook notebooks/kmeans_project.ipynb
```

Then click "Run All Cells" (or run individually)

---

## 📁 File Descriptions

| File | Purpose |
|------|---------|
| `README.md` | Complete project documentation |
| `requirements.txt` | Python package dependencies |
| `.gitignore` | Files excluded from Git |
| `kmeans_clustering.py` | Main Python script |
| `coffee_customers.csv` | Sample customer dataset |
| `notebooks/` | Jupyter notebook with analysis |
| `results/` | Output visualizations |

---

## ⚠️ Troubleshooting

**"ModuleNotFoundError: No module named 'pandas'"**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**"No such file: coffee_customers.csv"**
- Make sure the CSV file is in the same directory as the script

**"Permission denied when running script"**
```bash
python kmeans_clustering.py  # Use python instead of ./
```

---

## 🎯 What to Expect

**Console Output:**
```
================================================================================
☕ COFFEE SHOP CUSTOMER CLUSTERING PROJECT
================================================================================

📥 Loading data from coffee_customers.csv...
✅ Loaded 50 customers with 5 features

🔧 Preparing data with features: ['monthly_spend', 'visit_frequency']
✅ Data standardized (mean≈0, std≈1)

[Elbow Method Results...]
[Silhouette Score Results...]

📈 Creating visualization...
💾 Saved: results/elbow_method.png
💾 Saved: results/silhouette_score.png
💾 Saved: results/cluster_visualization.png

✅ Results saved to 'clustered_customers.csv'

🎉 PROJECT COMPLETE!
================================================================================
```

**Generated Files:**
- `results/elbow_method.png` - WCSS vs k plot
- `results/silhouette_score.png` - Silhouette vs k plot
- `results/cluster_visualization.png` - Final cluster plot
- `clustered_customers.csv` - Data with cluster assignments

---

## 📚 Learn More

- **K-Means Theory:** See README.md section "How It Works"
- **Code Comments:** Check `kmeans_clustering.py` for detailed explanations
- **Business Insights:** See README.md section "Key Results"
- **Full Documentation:** Read `README.md`

---

## 💡 Next Steps

1. ✅ Run the script
2. ✅ Examine the output visualizations
3. ✅ Review `clustered_customers.csv`
4. ✅ Read through the code comments
5. ✅ Modify parameters and experiment!

**Try changing:**
- Different k values in the script
- Different feature combinations
- Different clustering algorithms (see Scikit-learn docs)

---

**Questions? Check README.md or create an Issue on GitHub!**
