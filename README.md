# Shopping Trends Analysis

### Overview

I used numpy, pandas, matplotlib, and seaborn to practice clustering data with Python. I analyzed a dataset that contains consumer shopping information to better understand if there were any trends present. Furthermore, I generated various scatter plots, dendographs, and line graphs from my code.
 
 ### Dataset
 https://raw.githubusercontent.com/zariable/data/master/shopping_data.csv
 
 ### Dataset Factors
 - CustomerID
 - Gender
 - Age
 - Annual Income: In thousands of dollars
 - Spending Score: How often a person spends money in a mall on a scale of 1 to 100, with 100 being the highest spender
  
 ### Conclusion
 
![image](https://user-images.githubusercontent.com/63205351/231275680-0c5b7302-97da-4f8c-94f6-417b5e0f01ca.png)

Initially, I used a dendrogram to determine the number of clusters present. As seen in the above graph, there are 3 or 5 clusters. Because there could be two choices, I will later determine the optimal number of clusters needed for my analysis. In this case, I moved forward with 5 clusters.

![image](https://user-images.githubusercontent.com/63205351/231276541-f7f46ce9-620b-4a93-b0de-fd6e2f600653.png)

I then applied hierarchial clustering using 5 for the number of clusters, as discovered in the previous dendograph. After plotting my results, this graph confirmed my initial thoughts that the dataset contained 5 distinct clusters.

![image](https://user-images.githubusercontent.com/63205351/231276984-fb183a3b-bea3-48c0-9fdd-f5836d5a1fd1.png)

To determine that I chose the optimal number of clusters, I applied k-means and plotted the results. Using the elbow method, I determined that at 5, there is an the SSE line begins to flatten, indicating that this is the correct number of clusters.

![image](https://user-images.githubusercontent.com/63205351/231277838-bd2fdeb4-723e-45d3-bd1e-1dc232da0213.png)

Lastly, I replotted the initial scatterplot with centers.
