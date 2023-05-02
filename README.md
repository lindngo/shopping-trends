# Shopping Trends Analysis

## Overview

I used numpy, pandas, matplotlib, and seaborn to practice clustering data with Python. I analyzed a dataset that contains customer shopping information to better understand if there were trends present. Furthermore, I generated various scatter plots, dendographs, and line graphs from my code.
 
 ## Dataset
 https://raw.githubusercontent.com/zariable/data/master/shopping_data.csv
 
 ## Dataset Factors
 - CustomerID
 - Gender
 - Age
 - Annual Income: In thousands of dollars
 - Spending Score: How often a person spends money in a mall on a scale of 1 to 100, with 100 being the highest spender
  
 ## Exploratory Data Analysis
 
![image](https://user-images.githubusercontent.com/63205351/231301471-77d719dd-386b-42c1-a2b2-53cbd14d88f5.png)

Initially, I used a dendrogram to determine the number of clusters present. As seen in the above graph, there are 3 or 5 clusters. Because there could be two choices, I will later determine the optimal number of clusters needed for my analysis. In this case, I moved forward with 5 clusters.

![image](https://user-images.githubusercontent.com/63205351/231301497-5c26f26a-2172-446a-b750-32973da4228e.png)

I then applied hierarchial clustering using 5 for the number of clusters, as discovered in the previous dendograph. After plotting my results, this graph confirmed my initial thoughts that the dataset contained 5 distinct clusters.

![image](https://user-images.githubusercontent.com/63205351/231301519-32cdee24-fcb1-4b21-91f3-8ae8c7da9d7e.png)

To determine that I chose the optimal number of clusters, I applied k-means and plotted the results. Using the elbow method, I determined that at point 5, there is an the SSE line begins to flatten, indicating that this is the correct number of clusters.

![image](https://user-images.githubusercontent.com/63205351/231301539-f7eb085c-f476-417c-a7a4-5226afde4312.png)

Lastly, I replotted the initial scatterplot with centers, as seen above. 

## Conclusions

From the above scatterplot, we can derive that there are 5 distinct clusters. These clusters indicate that the typical spending habits of these customers can be described as follows:

1. At ~$30,000 in annual income, there are two types of customers: frugal spenders (spending score = 20) and lavish spenders (spending score = 80).
2. At ~$55,000 in annual income, majority of these customers average a spending score of 50, which means they fall perfectly in the middle of frugal and lavish spending.
3. At ~$90,000 in annual income, we can see that the results are similar to point 1, being that there are two types: frugal spenders (spending score = 20) and lavish spenders (spending score = 80).

In my future analysis, I would be curious to see if there is data on each customers' marital status, family size, quantity of items purchased, frequency of mall visits, and time spent in a mall. I believe that this would provide deeper insight on customer shopping trends.
