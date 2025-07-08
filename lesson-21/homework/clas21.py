# Homework:
# DataFrame 1: Student Grades
import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)
# Exercise 1: Calculate the average grade for each student.
# Exercise 2: Find the student with the highest average grade.
# Exercise 3: Create a new column 'Total' representing the total marks obtained by each student.
# Exercise 4: Plot a bar chart to visualize the average grades in each subject.

import pandas as pd
import matplotlib.pyplot as plt

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

# 1. Average grade per student
df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis=1)

# 2. Student with the highest average
top_student = df1.loc[df1['Average'].idxmax()]
print("Student with highest average grade:")
print(top_student)

# 3. Total marks per student
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)

# 4. Plot bar chart for subject averages
subject_means = df1[['Math', 'English', 'Science']].mean()
subject_means.plot(kind='bar')
plt.ylabel('Average Grade')
plt.title('Average Grades by Subject')
plt.show()

# DataFrame 2: Sales Data
import pandas as pd
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}
df2 = pd.DataFrame(data2)
# Exercise 1: Calculate the total sales for each product.
# Exercise 2: Find the date with the highest total sales.
# Exercise 3: Calculate the percentage change in sales for each product from the previous day.
# Exercise 4: Plot a line chart to visualize the sales trends for each product over time.

import pandas as pd
import matplotlib.pyplot as plt

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}
df2 = pd.DataFrame(data2)

# 1. Total sales for each product
total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print("Total sales for each product:")
print(total_sales)

# 2. Date with highest total sales
df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
max_sales_date = df2.loc[df2['Total_Sales'].idxmax(), 'Date']
print("Date with highest total sales:", max_sales_date)

# 3. Percentage change in sales for each product
for product in ['Product_A', 'Product_B', 'Product_C']:
    df2[f'{product}_Pct_Change'] = df2[product].pct_change() * 100

print("Percentage change in sales for each product:")
print(df2[['Date', 'Product_A_Pct_Change', 'Product_B_Pct_Change', 'Product_C_Pct_Change']])

# 4. Plot sales trends
plt.figure(figsize=(10, 6))
plt.plot(df2['Date'], df2['Product_A'], marker='o', label='Product_A')
plt.plot(df2['Date'], df2['Product_B'], marker='o', label='Product_B')
plt.plot(df2['Date'], df2['Product_C'], marker='o', label='Product_C')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Trends for Each Product Over Time')
plt.legend()
plt.grid(True)
plt.show()

# DataFrame 3: Employee Information
import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)
# Exercise 1: Calculate the average salary for each department.
# Exercise 2: Find the employee with the most experience.
# Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary in the dataframe.
# Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments.

import pandas as pd
import matplotlib.pyplot as plt

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}
df3 = pd.DataFrame(data3)

# 1. Average salary per department
avg_salary_dept = df3.groupby('Department')['Salary'].mean()
print("Average salary for each department:")
print(avg_salary_dept)

# 2. Employee with most experience
most_exp = df3.loc[df3['Experience (Years)'].idxmax()]
print("Employee with the most experience:")
print(most_exp)

# 3. Salary Increase from minimum
min_salary = df3['Salary'].min()
df3['Salary Increase'] = ((df3['Salary'] - min_salary) / min_salary) * 100
print(df3[['Name', 'Salary', 'Salary Increase']])

# 4. Bar chart: employee count per department
dept_counts = df3['Department'].value_counts()
dept_counts.plot(kind='bar')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.title('Employee Distribution by Department')
plt.show()

# DataFrame 4: Customer Orders
import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)
# Exercise 1: Calculate the total revenue from all orders.
# Exercise 2: Find the most ordered product.
# Exercise 3: Calculate the average quantity of products ordered.
# Exercise 4: Plot a pie chart to visualize the distribution of sales across different products.

import pandas as pd
import matplotlib.pyplot as plt

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

# 1. Total revenue
total_revenue = df4['Total_Price'].sum()
print("Total revenue from all orders:", total_revenue)

# 2. Most ordered product
most_ordered_product = df4.groupby('Product')['Quantity'].sum().idxmax()
print("Most ordered product:", most_ordered_product)

# 3. Average quantity
avg_quantity = df4['Quantity'].mean()
print("Average quantity of products ordered:", avg_quantity)

# 4. Pie chart: sales by product
product_sales = df4.groupby('Product')['Total_Price'].sum()
product_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.ylabel('')
plt.title('Distribution of Sales by Product')
plt.show()
