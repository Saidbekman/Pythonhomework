# Homework 1:

# import pandas as pd

# data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} df = pd.DataFrame(data)

# Rename column names using function. "First Name" --> "first_name", "Age" --> "age
# Print the first 3 rows of the DataFrame
# Find the mean age of the individuals
# Select and print only the 'Name' and 'City' columns
# Add a new column 'Salary' with random salary values
# Display summary statistics of the DataFrame

import pandas as pd
import numpy as np

# Step 1: Create the DataFrame
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Step 2: Rename columns using a function
df.rename(columns=lambda x: x.lower().replace(" ", "_"), inplace=True)

# Step 3: Print the first 3 rows
print("First 3 rows of the DataFrame:")
print(df.head(3))

# Step 4: Find the mean age
mean_age = df['age'].mean()
print("\nMean age of individuals:", mean_age)

# Step 5: Select and print only the 'first_name' and 'city' columns
print("\nSelected columns (first_name and city):")
print(df[['first_name', 'city']])

# Step 6: Add a new column 'salary' with random salary values
np.random.seed(0)  # for reproducibility
df['salary'] = np.random.randint(50000, 100000, size=len(df))

# Step 7: Display summary statistics of the DataFrame
print("\nSummary statistics:")
print(df.describe())

# Homework 2:

# Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. Use below table.
# Month	Sales	Expenses
# Jan	5000	3000
# Feb	6000	3500
# Mar	7500	4000
# Apr	8000	4500
# Calculate and display the maximum sales and expenses.
# Calculate and display the minimum sales and expenses.
# Calculate and display the average sales and expenses.

import pandas as pd

# Step 1: Create the DataFrame
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}
sales_and_expenses = pd.DataFrame(data)

# Step 2: Calculate and display maximum sales and expenses
max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()
print("Maximum Sales:", max_sales)
print("Maximum Expenses:", max_expenses)

# Step 3: Calculate and display minimum sales and expenses
min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()
print("\nMinimum Sales:", min_sales)
print("Minimum Expenses:", min_expenses)

# Step 4: Calculate and display average sales and expenses
avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()
print("\nAverage Sales:", avg_sales)
print("Average Expenses:", avg_expenses)

# Homework 3:

# Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.
# Category	January	February	March	April
# Rent	1200	1300	1400	1500
# Utilities	200	220	240	250
# Groceries	300	320	330	350
# Entertainment	150	160	170	180
# Calculate and display the maximum expense for each category.
# Calculate and display the minimum expense for each category.
# Calculate and display the average expense for each category.
# In this task, use .set_index method to make Category column as index.

# Try this code, learn it and use it in the task.

# expenses.set_index('Category')

import pandas as pd

# Step 1: Create the DataFrame
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)

# Step 2: Set 'Category' as index
expenses = expenses.set_index('Category')

# Step 3: Calculate and display maximum expense for each category
max_expenses = expenses.max(axis=1)
print("Maximum expense for each category:")
print(max_expenses)

# Step 4: Calculate and display minimum expense for each category
min_expenses = expenses.min(axis=1)
print("\nMinimum expense for each category:")
print(min_expenses)

# Step 5: Calculate and display average expense for each category
avg_expenses = expenses.mean(axis=1)
print("\nAverage expense for each category:")
print(avg_expenses)
