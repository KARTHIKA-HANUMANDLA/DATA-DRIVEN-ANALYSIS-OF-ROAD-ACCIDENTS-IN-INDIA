import seaborn as sns
import matplotlib.pyplot as plt

# 1. Yearly Accident Trends
yearly_accident_counts = df['Year'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
sns.barplot(x=yearly_accident_counts.index, y=yearly_accident_counts.values, palette='viridis')
plt.title('Total Accidents by Year')
plt.xlabel('Year')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Monthly Accident Trends
monthly_accident_counts = df['Month'].value_counts()

# Define chronological order for months
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

# Reindex to ensure chronological order for plotting
monthly_accident_counts = monthly_accident_counts.reindex(month_order, fill_value=0)

plt.figure(figsize=(12, 6))
sns.barplot(x=monthly_accident_counts.index, y=monthly_accident_counts.values, palette='magma')
plt.title('Total Accidents by Month')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()