"""
===============================================================================
COFFEE SHOP CUSTOMER CLUSTERING - K-MEANS ANALYSIS
===============================================================================
Project: Customer Segmentation using K-Means Clustering
Course: AIGC 5503 - AI for Business Decision Making
Institution: Humber Polytechnic
Date: June 2026

Description:
    This script performs customer segmentation analysis on coffee shop data
    using K-Means clustering. It includes:
    - Data loading and exploration
    - Feature standardization
    - Optimal cluster determination (Elbow Method & Silhouette Score)
    - Visualization and cluster analysis
    - Business insights and recommendations

Author: Your Name
Student ID: N10020731
===============================================================================
"""

# ===== IMPORTS =====
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import warnings
warnings.filterwarnings('ignore')

# ===== CONFIGURATION =====
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
np.random.seed(42)


# ===== HELPER FUNCTIONS =====
def load_data(filepath):
    """Load customer data from CSV file."""
    print(f"📥 Loading data from {filepath}...")
    df = pd.read_csv(filepath)
    print(f"✅ Loaded {len(df)} customers with {len(df.columns)} features\n")
    return df


def explore_data(df):
    """Display basic information about the dataset."""
    print("="*80)
    print("DATA EXPLORATION")
    print("="*80)
    print(f"\n📊 Dataset Shape: {df.shape}")
    print(f"\n📋 First 5 Rows:")
    print(df.head())
    print(f"\n📈 Statistical Summary:")
    print(df.describe())
    print(f"\n🔍 Missing Values:")
    print(df.isnull().sum())
    print()


def prepare_data(df, features):
    """Standardize selected features."""
    print(f"🔧 Preparing data with features: {features}")
    X = df[features].copy()
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    print("✅ Data standardized (mean≈0, std≈1)\n")
    return X_scaled, scaler, X


def elbow_method(X_scaled, k_range=range(2, 11)):
    """
    Calculate WCSS for different k values.
    
    WCSS = Within-Cluster Sum of Squares
    Helps identify the "elbow point" where WCSS improvement plateaus.
    """
    print("="*80)
    print("ELBOW METHOD")
    print("="*80)
    print("🔄 Testing different k values...")
    
    wcss = []
    
    for k in k_range:
        kmeans = KMeans(
            n_clusters=k,
            init='k-means++',
            random_state=42,
            n_init=10
        )
        kmeans.fit(X_scaled)
        wcss.append(kmeans.inertia_)
        print(f"   k={k}: WCSS = {kmeans.inertia_:.2f}")
    
    return wcss


def silhouette_method(X_scaled, k_range=range(2, 11)):
    """
    Calculate Silhouette Score for different k values.
    
    Silhouette Score measures both:
    - Cohesion: how close points are to their own cluster
    - Separation: how far clusters are from each other
    
    Range: -1 to +1 (higher is better)
    """
    print("\n" + "="*80)
    print("SILHOUETTE SCORE METHOD")
    print("="*80)
    print("🎯 Calculating Silhouette Scores...")
    
    silhouette_scores = []
    
    for k in k_range:
        kmeans = KMeans(
            n_clusters=k,
            init='k-means++',
            random_state=42,
            n_init=10
        )
        labels = kmeans.fit_predict(X_scaled)
        score = silhouette_score(X_scaled, labels)
        silhouette_scores.append(score)
        print(f"   k={k}: Silhouette Score = {score:.4f}")
    
    best_k = k_range[silhouette_scores.index(max(silhouette_scores))]
    best_score = max(silhouette_scores)
    print(f"\n🏆 BEST k: {best_k} (score = {best_score:.4f})\n")
    
    return silhouette_scores, best_k, best_score


def plot_elbow(k_range, wcss):
    """Visualize Elbow Method."""
    plt.figure(figsize=(10, 6))
    plt.plot(k_range, wcss, marker='o', linewidth=2, markersize=8, color='steelblue')
    plt.xlabel('Number of Clusters (k)', fontsize=12)
    plt.ylabel('WCSS (Inertia)', fontsize=12)
    plt.title('Elbow Method: Finding Optimal k', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.xticks(k_range)
    plt.axvline(x=3, color='red', linestyle='--', alpha=0.7, label='Potential Elbow')
    plt.legend()
    plt.tight_layout()
    plt.savefig('results/elbow_method.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("💾 Saved: results/elbow_method.png")


def plot_silhouette(k_range, silhouette_scores, best_k, best_score):
    """Visualize Silhouette Scores."""
    plt.figure(figsize=(10, 6))
    plt.plot(k_range, silhouette_scores, marker='s', linewidth=2, 
             markersize=8, color='darkgreen')
    plt.xlabel('Number of Clusters (k)', fontsize=12)
    plt.ylabel('Silhouette Score', fontsize=12)
    plt.title('Silhouette Score: Finding Optimal k', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.xticks(k_range)
    plt.plot(best_k, best_score, marker='*', markersize=25, color='red', 
             label=f'Best: k={best_k}')
    plt.legend()
    plt.tight_layout()
    plt.savefig('results/silhouette_score.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("💾 Saved: results/silhouette_score.png")


def final_clustering(X_scaled, optimal_k):
    """Run K-Means with optimal k value."""
    print("="*80)
    print(f"FINAL CLUSTERING (k={optimal_k})")
    print("="*80)
    
    kmeans_final = KMeans(
        n_clusters=optimal_k,
        init='k-means++',
        random_state=42,
        n_init=10
    )
    cluster_labels = kmeans_final.fit_predict(X_scaled)
    
    print(f"✅ Clustering complete!")
    print(f"\n📊 Cluster Distribution:")
    unique, counts = np.unique(cluster_labels, return_counts=True)
    for cluster, count in zip(unique, counts):
        print(f"   Cluster {cluster}: {count} customers ({count/len(cluster_labels)*100:.1f}%)")
    
    final_score = silhouette_score(X_scaled, cluster_labels)
    print(f"\n🎯 Final Silhouette Score: {final_score:.4f}\n")
    
    return kmeans_final, cluster_labels, final_score


def visualize_clusters(X_scaled, cluster_labels, kmeans_final, optimal_k):
    """Create cluster visualization."""
    print("📈 Creating visualization...")
    
    plt.figure(figsize=(12, 8))
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#95E1D3', '#F38181'][:optimal_k]
    
    for i in range(optimal_k):
        cluster_points = X_scaled[cluster_labels == i]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], 
                   c=colors[i], label=f'Cluster {i}', s=100, alpha=0.7, 
                   edgecolors='black', linewidth=1.5)
    
    plt.scatter(kmeans_final.cluster_centers_[:, 0], 
               kmeans_final.cluster_centers_[:, 1], 
               c='yellow', marker='*', s=500, edgecolors='black', linewidth=2,
               label='Centroids', zorder=5)
    
    plt.xlabel('Monthly Spend (Standardized)', fontsize=12)
    plt.ylabel('Visit Frequency (Standardized)', fontsize=12)
    plt.title(f'Customer Segments (k={optimal_k})', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('results/cluster_visualization.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("💾 Saved: results/cluster_visualization.png\n")


def analyze_clusters(df, cluster_labels, optimal_k):
    """Analyze and display cluster characteristics."""
    print("="*80)
    print("CLUSTER ANALYSIS")
    print("="*80)
    
    df['cluster'] = cluster_labels
    
    for cluster_num in range(optimal_k):
        cluster_data = df[df['cluster'] == cluster_num]
        
        print(f"\n🎯 CLUSTER {cluster_num}")
        print("-" * 80)
        print(f"   Size: {len(cluster_data)} customers ({len(cluster_data)/len(df)*100:.1f}%)")
        print(f"\n   💰 Monthly Spend:")
        print(f"      Average: ${cluster_data['monthly_spend'].mean():.2f}")
        print(f"      Range: ${cluster_data['monthly_spend'].min():.2f} - ${cluster_data['monthly_spend'].max():.2f}")
        
        print(f"\n   📍 Visit Frequency:")
        print(f"      Average: {cluster_data['visit_frequency'].mean():.1f} visits/month")
        print(f"      Range: {cluster_data['visit_frequency'].min()} - {cluster_data['visit_frequency'].max()} visits")
        
        print(f"\n   🛍️ Avg Order Value:")
        print(f"      ${cluster_data['avg_order_value'].mean():.2f}")
        
        loyalty_pct = cluster_data['loyalty_member'].mean() * 100
        print(f"\n   🎟️ Loyalty Members: {loyalty_pct:.1f}%")


def generate_recommendations(df, cluster_labels, optimal_k):
    """Generate marketing recommendations for each cluster."""
    print("\n" + "="*80)
    print("MARKETING RECOMMENDATIONS")
    print("="*80)
    
    recommendations = {
        0: {
            'name': 'Budget-Conscious Occasional Buyers',
            'strategy': '20% off coupons, Happy Hour promos, Entry-level combos',
            'action': 'Send weekly discount emails'
        },
        1: {
            'name': 'Premium Loyal Regulars',
            'strategy': 'VIP perks, Exclusive drinks, Personal recommendations',
            'action': 'Free premium drink monthly, Priority ordering'
        },
        2: {
            'name': 'Moderate Frequency Customers',
            'strategy': 'Loyalty rewards, Limited-time offers, Engagement programs',
            'action': 'Bonus points campaigns, Seasonal specials'
        }
    }
    
    for cluster_num in range(min(optimal_k, 3)):
        if cluster_num in recommendations:
            rec = recommendations[cluster_num]
            print(f"\n📌 {rec['name'].upper()}")
            print(f"   Strategy: {rec['strategy']}")
            print(f"   Action: {rec['action']}")


def save_results(df, output_file='clustered_customers.csv'):
    """Save clustered data to CSV."""
    df.to_csv(output_file, index=False)
    print(f"\n✅ Results saved to '{output_file}'")


# ===== MAIN EXECUTION =====
def main():
    """Execute the complete clustering analysis pipeline."""
    
    print("\n" + "="*80)
    print("☕ COFFEE SHOP CUSTOMER CLUSTERING PROJECT")
    print("="*80 + "\n")
    
    # Step 1: Load data
    df = load_data('coffee_customers.csv')
    explore_data(df)
    
    # Step 2: Prepare data
    features = ['monthly_spend', 'visit_frequency']
    X_scaled, scaler, X = prepare_data(df, features)
    
    # Step 3: Determine optimal k
    k_range = range(2, 11)
    wcss = elbow_method(X_scaled, k_range)
    silhouette_scores, best_k, best_score = silhouette_method(X_scaled, k_range)
    
    # Step 4: Visualize methods
    plot_elbow(k_range, wcss)
    plot_silhouette(k_range, silhouette_scores, best_k, best_score)
    
    # Step 5: Final clustering
    kmeans_final, cluster_labels, final_score = final_clustering(X_scaled, best_k)
    
    # Step 6: Visualize clusters
    visualize_clusters(X_scaled, cluster_labels, kmeans_final, best_k)
    
    # Step 7: Analysis
    analyze_clusters(df, cluster_labels, best_k)
    
    # Step 8: Recommendations
    generate_recommendations(df, cluster_labels, best_k)
    
    # Step 9: Save results
    save_results(df)
    
    print("\n" + "="*80)
    print("🎉 PROJECT COMPLETE!")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
