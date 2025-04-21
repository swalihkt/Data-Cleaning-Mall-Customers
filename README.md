##  Data Cleaning Project – Mall Customers Dataset

###  About the Project
This project focuses on cleaning and preprocessing the **Mall Customers Dataset** using Python (Pandas). The goal was to ensure the dataset is clean, consistent, and ready for further analysis.

---

###  Dataset Used
- **Name:** Mall_Customers.csv  
- **Source:** Kaggle  
- **Rows:** 200  
- **Columns:** 5  
- **Features:** CustomerID, Gender, Age, Annual Income (k$), Spending Score (1-100)

---

###  Steps Performed

1. **Loaded the Dataset**  
   Used `pandas.read_csv()` to load the raw data from the CSV file.

2. **Checked for Missing Values**  
   Used `.isnull().sum()` – No missing values found.

3. **Removed Duplicates**  
   Used `.drop_duplicates()` – No duplicates found.

4. **Standardized Text Values**  
   Converted all entries in the **Gender** column to lowercase using `.str.lower()`.

5. **Renamed Columns**  
   Made all column names lowercase and replaced spaces with underscores using:
   ```python
   data.columns = data.columns.str.lower().str.replace(' ', '_')
Verified Data Types
Used .dtypes – All data types were already appropriate.

Saved Cleaned Dataset
Saved the cleaned file to:
C:/Users/Kurien/Documents/Cleaned_Mall_Customers.csv

### Challenges Faced

- No major challenges encountered since the dataset was relatively clean.

---

### Files Included

- **Cleaned_Mall_Customers.csv** – Cleaned dataset.
- **data_cleaning_mall_customers.py** – Python code used for cleaning.
- **README.md** – Project explanation.
