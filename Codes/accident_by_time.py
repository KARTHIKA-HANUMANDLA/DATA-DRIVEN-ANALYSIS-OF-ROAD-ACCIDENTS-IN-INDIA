import matplotlib.pyplot as plt
import seaborn as sns
from datetime import time

# 1. Define time bins and their corresponding time ranges
def get_time_segment(time_obj):
    if time(6, 0) <= time_obj < time(12, 0):
        return 'Morning'
    elif time(12, 0) <= time_obj < time(18, 0):
        return 'Afternoon'
    elif time(18, 0) <= time_obj < time(22, 0):
        return 'Evening'
    else:
        return 'Night'

# 2. Create a new categorical column 'Time Segment'
df['Time Segment'] = df['Time of Day'].apply(get_time_segment)

# Define a specific order for the time segments
time_segment_order = ['Morning', 'Afternoon', 'Evening', 'Night']

# 3. Calculate the frequency of accidents for each 'Time Segment'
time_segment_counts = df['Time Segment'].value_counts().reindex(time_segment_order)

# 4. Create a bar plot to visualize these frequencies
plt.figure(figsize=(10, 6))
sns.barplot(x=time_segment_counts.index, y=time_segment_counts.values, color='purple')

# 5. Set the title of the plot
plt.title('Accidents by Time of Day Segment')

# 6. Label the x-axis and y-axis
plt.xlabel('Time Segment')
plt.ylabel('Number of Accidents')

# 7. Rotate the x-axis labels if necessary (not strictly needed for 4 categories, but good practice)
plt.xticks(rotation=0)

# 8. Ensure the plot layout is tight
plt.tight_layout()

# Display the plot
plt.show()