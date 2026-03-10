import matplotlib.pyplot as plt
import seaborn as sns

# 1. Calculate the frequency of each unique 'Weather Conditions'
weather_accident_counts = df['Weather Conditions'].value_counts()

# 2. Create a bar plot to visualize these frequencies
plt.figure(figsize=(10, 6))
sns.barplot(x=weather_accident_counts.index, y=weather_accident_counts.values, color='steelblue')

# 3. Set the title of the plot
plt.title('Accidents by Weather Condition')

# 4. Label the x-axis and y-axis
plt.xlabel('Weather Condition')
plt.ylabel('Number of Accidents')

# 5. Rotate the x-axis labels
plt.xticks(rotation=45, ha='right')

# 6. Ensure the plot layout is tight
plt.tight_layout()

# 7. Display the plot
plt.show()