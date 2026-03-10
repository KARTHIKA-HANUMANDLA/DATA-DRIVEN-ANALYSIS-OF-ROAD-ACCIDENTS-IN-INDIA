initial_rows_before_duplicates = df.shape[0]
df.drop_duplicates(inplace=True)
final_rows_after_duplicates = df.shape[0]

duplicate_rows_removed = initial_rows_before_duplicates - final_rows_after_duplicates
print(f"Initial number of rows: {initial_rows_before_duplicates}")
print(f"Number of rows after removing duplicates: {final_rows_after_duplicates}")
print(f"Number of duplicate rows removed: {duplicate_rows_removed}")

print("\nFirst few rows of DataFrame after removing duplicates:")
print(df.head())