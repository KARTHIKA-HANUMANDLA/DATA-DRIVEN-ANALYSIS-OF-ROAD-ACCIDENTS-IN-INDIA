import matplotlib.pyplot as plt
import seaborn as sns

# 1. Calculate the frequency of each unique 'Vehicle Type Involved' category
vehicle_type_counts = df['Vehicle Type Involved'].value_counts()

# 2. Create a bar plot to visualize these frequencies
plt.figure(figsize=(12, 6))
sns.barplot(x=vehicle_type_counts.index, y=vehicle_type_counts.values, color='lightgreen')

# 3. Set the title of the plot
plt.title('Accidents by Vehicle Type Involved')

# 4. Label the x-axis and y-axis
plt.xlabel('Vehicle Type Involved')
plt.ylabel('Number of Accidents')

# 5. Rotate the x-axis labels to improve readability
plt.xticks(rotation=45, ha='right')

# 6. Ensure the plot layout is tight
plt.tight_layout()

# 7. Display the plot
plt.show()