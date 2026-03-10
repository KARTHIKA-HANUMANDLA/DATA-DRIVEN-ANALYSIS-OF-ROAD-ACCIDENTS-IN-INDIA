import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create a box plot using sns.boxplot()
plt.figure(figsize=(10, 6))
sns.boxplot(x='Accident Severity', y='Speed Limit (km/h)', data=df, palette='viridis')

# 2. Set the title of the plot
plt.title('Speed Limit (km/h) vs. Accident Severity')

# 3. Label the x-axis and y-axis
plt.xlabel('Accident Severity')
plt.ylabel('Speed Limit (km/h)')

# 4. Ensure the plot layout is tight
plt.tight_layout()

# 5. Display the plot
plt.show()