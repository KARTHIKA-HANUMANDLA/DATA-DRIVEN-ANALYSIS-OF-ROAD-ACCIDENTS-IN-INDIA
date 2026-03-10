initial_rows = df.shape[0]
df.dropna(inplace=True)
final_rows = df.shape[0]

dropped_rows = initial_rows - final_rows
print(f"Initial number of rows: {initial_rows}")
print(f"Number of rows after dropping missing values: {final_rows}")
print(f"Number of rows dropped: {dropped_rows}")