import seaborn as sns
import matplotlib.pyplot as plt

# 1. Accident counts by 'State Name'
state_accident_counts = df['State Name'].value_counts()

# 2. Create a bar plot for state-wise accident counts
plt.figure(figsize=(12, 6))
sns.barplot(x=state_accident_counts.index, y=state_accident_counts.values)
plt.title('Total Accidents by State Name')
plt.xlabel('State Name')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# 3. Accident counts by 'City Name'
city_accident_counts = df['City Name'].value_counts()

# Consider displaying only the top 20 cities for better readability
top_cities = city_accident_counts.head(20)

# 4. Create a bar plot for city-wise accident counts
plt.figure(figsize=(12, 6))
sns.barplot(x=top_cities.index, y=top_cities.values)
plt.title('Top 20 Cities by Accident Count')
plt.xlabel('City Name')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()