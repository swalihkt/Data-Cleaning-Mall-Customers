import pandas as pd

# Step 1: Read the CSV file
data = pd.read_csv('C:/Users/Kurien/Downloads/archive (1)/Mall_Customers.csv')
print(data.head())

# Step 2: Check for missing values
print(data.isnull().sum())

# Step 3: Remove duplicate rows
data = data.drop_duplicates()

# Step 4: Standardize text values
data['Gender'] = data['Gender'].str.lower()

# Step 5: Rename columns
data.columns = data.columns.str.lower().str.replace(' ', '_')

# Step 6: Check data types
print(data.dtypes)

# Step 7: Save the cleaned dataset
data.to_csv("C:/Users/Kurien/Documents/Cleaned_Mall_Customers.csv", index=False)
