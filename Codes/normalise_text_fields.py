for column in df.select_dtypes(include=['object']).columns:
    df[column] = df[column].astype(str).str.lower().str.strip()

print("Text normalization complete. Displaying a sample of normalized columns:")
# Display sample of a few object columns to verify
for col in ['State Name', 'City Name', 'Accident Severity', 'Weather Conditions']:
    if col in df.columns:
        print(f"\n{col}:\n{df[col].value_counts().head(5)}")