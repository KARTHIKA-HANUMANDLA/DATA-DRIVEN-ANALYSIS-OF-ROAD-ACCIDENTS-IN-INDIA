import pandas as pd

# 1. Reload the dataset
df = pd.read_excel('/content/accident_prediction_india.xlsx')

# 2. Store the initial number of rows
initial_rows_before_cleaning = df.shape[0]

# 3. Drop any rows that contain missing values (initial handling)
df.dropna(inplace=True)

# 4. Print the number of rows dropped in this step
dropped_rows_initial = initial_rows_before_cleaning - df.shape[0]
print(f"Initial number of rows: {initial_rows_before_cleaning}")
print(f"Number of rows after initial missing value handling: {df.shape[0]}")
print(f"Number of rows dropped during initial missing value handling: {dropped_rows_initial}")

# 5. Convert the 'Time of Day' column to time objects
# Using format='mixed' and errors='coerce' for robust conversion
df['Time of Day'] = pd.to_datetime(df['Time of Day'], errors='coerce', format='mixed').dt.time

# 6. Store the number of rows before dropping NaT values from 'Time of Day'
initial_rows_before_time_nat_drop = df.shape[0]

# 7. Drop any rows where 'Time of Day' resulted in a NaT value
df.dropna(subset=['Time of Day'], inplace=True)

# 8. Print the number of rows dropped due to NaT values in 'Time of Day'
dropped_rows_time_nat = initial_rows_before_time_nat_drop - df.shape[0]
print(f"\nNumber of rows before dropping NaT in 'Time of Day': {initial_rows_before_time_nat_drop}")
print(f"Number of rows after dropping NaT in 'Time of Day': {df.shape[0]}")
print(f"Number of rows dropped due to NaT in 'Time of Day': {dropped_rows_time_nat}")

# 9. Display the first few rows of the cleaned DataFrame
print("\nFirst few rows of the cleaned DataFrame:")
print(df.head())

# 10. Display a summary of the DataFrame
print("\nSummary of the cleaned DataFrame:")
print(df.info())