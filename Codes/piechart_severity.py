import matplotlib.pyplot as plt

# 1. Calculate the frequency of each unique 'Accident Severity' category
accident_severity_counts = df['Accident Severity'].value_counts()

# 2. Create a pie chart from these frequencies
plt.figure(figsize=(8, 8))
plt.pie(accident_severity_counts, labels=accident_severity_counts.index, autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'skyblue', 'lightgreen'])

# 3. Add a title to the pie chart
plt.title('Percentage Distribution of Accident Severity')

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# 5. Display the plot
plt.show()