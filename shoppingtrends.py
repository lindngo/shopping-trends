## Clustering Customers on Shopping Trends

import warnings
warnings.filterwarnings("ignore")
from sys import displayhook
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Loading data
shopping_data = pd.read_csv('https://raw.githubusercontent.com/zariable/data/master/shopping_data.csv')
shopping_data.rename(
    columns={
        'CustomerID': 'customer_id',
        'Genre': 'genre',
        'Age': 'age',
        'Annual Income (k$)': 'annual_income',
        'Spending Score (1-100)': 'spending_score'
    },
    inplace=True
)
displayhook(shopping_data.head())

# Keeping only annual_income and spending_score for clustering
shopping_data = shopping_data.drop(['customer_id', 'genre', 'age'], axis = 1)
shopping_data

# Using dendrogram to find number of clusters
import scipy.cluster.hierarchy as shc

plt.figure(figsize=(10, 10))  
dend = shc.dendrogram(shc.linkage(shopping_data, method='ward'))
plt.title('Dendrogram')  
plt.xlabel('CustomerID')
plt.ylabel('Height')
plt.show()

# Using number of clusters from dendrogram to perform hierarchial clustering 
from sklearn.cluster import AgglomerativeClustering

hc = AgglomerativeClustering(n_clusters = 5, affinity='euclidean', linkage='ward')  
y_ward = hc.fit_predict(shopping_data)  

plt.scatter(shopping_data.iloc[:,0], shopping_data.iloc[:,1], c=y_ward, s=50)
plt.title('Clustering based on Annual Income and Spending Score')
plt.xlabel('Annual Income (in thousands of $)')
plt.ylabel('Spending Score (0-100)')
plt.show()

# Performing K-means Clustering to visualize results
# Specifically, finding best value of K between 2 and 10 by analyzing Sum of Squared Error (SSE)
from sklearn.cluster import KMeans

knumber = range(2, 11)
sse = []

for x in knumber:
  kmeans = KMeans(n_clusters = x)
  kmeans.fit(shopping_data)
  sse.append(kmeans.inertia_)

print(sse)

plt.plot(sse)
plt.title('Sum of Squared Error (SSE) in relationship to Number of K')
plt.xlabel('Number of K')
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8], ['2', '3', '4', '5', '6', '7', '8', '9', '10'])
plt.ylabel('SSE')
plt.show()

# Using scatterplot to visualize results, based on best K value from previous step
kmeans = KMeans(n_clusters=5)
kmeans.fit(shopping_data)
y_kmeans = kmeans.predict(shopping_data)

plt.scatter(shopping_data.iloc[:, 0], shopping_data.iloc[:, 1], c=y_kmeans, s=50)

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.title('Clustering with Centers based on Annual Income and Spending Score')
plt.xlabel('Annual Income (in thousands of $)')
plt.ylabel('Spending Score (0-100)')
plt.show()