print("\nSummary Information of the Cleaned DataFrame:")
print(df.info())

print("\n--- Cleaning Summary ---")
print(f"Initial number of rows: 3000") # From initial load
print(f"Initial number of columns: 22") # From initial df.info()
print(f"Final number of rows: {df.shape[0]}")
print(f"Final number of columns: {df.shape[1]}")
print(f"Total rows removed: {3000 - df.shape[0]}")
print(f"Total columns added/removed: {df.shape[1] - 22}")