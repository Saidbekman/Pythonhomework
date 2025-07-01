# Homework Assignment 1: Analyzing Sales Data

# You are given a dataset containing sales data for an e-commerce website. The dataset (task\sales_data.csv) has the following columns:

# Date: Date of the sale.
# Product: Name of the product sold.
# Category: Category to which the product belongs.
# Quantity: Number of units sold.
# Price: Price per unit.

import pandas as pd

df = pd.read_csv('task/sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])  # Ensure Date column is datetime

print(df.head())             # View first few rows
print(df.info())             # Check data types
print(df.describe())         # Statistical summary of numeric fields

df['Total_Sales'] = df['Quantity'] * df['Price']

sales_over_time = df.groupby('Date')['Total_Sales'].sum()

# Plotting
import matplotlib.pyplot as plt
sales_over_time.plot(figsize=(12,6), title='Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales Amount')
plt.grid(True)
plt.show()

top_products = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).head(10)
print(top_products)

category_sales = df.groupby('Category')['Total_Sales'].sum().sort_values(ascending=False)
print(category_sales)

df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total_Sales'].sum()

monthly_sales.plot(kind='bar', figsize=(12,6), title='Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales Amount')
plt.tight_layout()
plt.show()

Tasks:

# Group the data by the Category column and calculate the following aggregate statistics for each category:
# Total quantity sold.
# Average price per unit.
# Maximum quantity sold in a single transaction.
# Identify the top-selling product in each category based on the total quantity sold.
# Find the date on which the highest total sales (quantity * price) occurred.

import pandas as pd

# Load the data
df = pd.read_csv('task/sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Add total sales column
df['Total_Sales'] = df['Quantity'] * df['Price']

# 1️⃣ Group by Category - Aggregate statistics
category_stats = df.groupby('Category').agg(
    Total_Quantity_Sold=('Quantity', 'sum'),
    Average_Price_Per_Unit=('Price', 'mean'),
    Max_Quantity_Single_Transaction=('Quantity', 'max')
).reset_index()

print("Category-wise Aggregate Statistics:")
print(category_stats)

# 2️⃣ Top-selling product in each category based on total quantity sold
top_selling_by_category = (
    df.groupby(['Category', 'Product'])['Quantity']
    .sum()
    .reset_index()
    .sort_values(['Category', 'Quantity'], ascending=[True, False])
)

# Get the top-selling product per category
top_products = top_selling_by_category.groupby('Category').first().reset_index()

print("\nTop-Selling Product in Each Category:")
print(top_products)

# 3️⃣ Date with highest total sales
daily_sales = df.groupby('Date')['Total_Sales'].sum()
max_sales_date = daily_sales.idxmax()
max_sales_value = daily_sales.max()

print(f"\n📅 Date with highest total sales: {max_sales_date.date()} — ${max_sales_value:.2f}")

# Homework Assignment 2: Examining Customer Orders

# You have a dataset (task\customer_orders.csv) containing information about customer orders. The dataset has the following columns:

# OrderID: Unique identifier for each order.
# CustomerID: Unique identifier for each customer.
# Product: Name of the product ordered.
# Quantity: Number of units ordered.
# Price: Price per unit.
# Tasks:

# Group the data by CustomerID and filter out customers who have made less than 20 orders.
# Identify customers who have ordered products with an average price per unit greater than $120.
# Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.

import pandas as pd

# Load the dataset
df = pd.read_csv('task/customer_orders.csv')

# Add total price per row
df['TotalPrice'] = df['Quantity'] * df['Price']

# 1️⃣ Customers with 20 or more orders
customer_order_counts = df.groupby('CustomerID')['OrderID'].count()
active_customers = customer_order_counts[customer_order_counts >= 20].index
filtered_customers = df[df['CustomerID'].isin(active_customers)]

print("Customers with ≥20 orders:")
print(filtered_customers['CustomerID'].unique())

# 2️⃣ Customers with average price per unit > $120
avg_price_per_customer = df.groupby('CustomerID')['Price'].mean()
high_value_customers = avg_price_per_customer[avg_price_per_customer > 120].index

print("\nCustomers with average unit price > $120:")
print(high_value_customers.tolist())

# 3️⃣ Total quantity and total price by product, filter total quantity < 5
product_totals = df.groupby('Product').agg(
    Total_Quantity=('Quantity', 'sum'),
    Total_Revenue=('TotalPrice', 'sum')
).reset_index()

filtered_products = product_totals[product_totals['Total_Quantity'] >= 5]

print("\nProducts with total quantity ≥5 units:")
print(filtered_products)

# Homework Assignment 3: Population Salary Analysis

# "task\population.db" sqlite database has population table.
# "task\population salary analysis.xlsx" file defines Salary Band categories.
# Read the data from population table and calculate following measures:
# Percentage of population for each salary category;
# Average salary in each salary category;
# Median salary in each salary category;
# Number of population in each salary category;
# Calculate the same measures in each State
# Note: Use SQL only to select data from database. All the other calculations should be done in python.

# Connect to SQLite database
conn = sqlite3.connect('task/population.db')

# Read the population table using SQL
query = "SELECT * FROM population"
population_df = pd.read_sql_query(query, conn)

conn.close()  # Close the connection

# Load salary bands
salary_bands = pd.read_excel('task/population salary analysis.xlsx')

# Expecting salary_bands to have two columns: 'Band' and 'Range' (or Min & Max)
# For more precise binning, convert it into a proper bin structure

# Let's assume the file has 'Min', 'Max', and 'Band' columns
bins = salary_bands[['Min', 'Max']].values.flatten()
labels = salary_bands['Band'].tolist()

# Create bin edges and labels
edges = list(salary_bands['Min']) + [salary_bands['Max'].iloc[-1]]

# Assign salary bands
population_df['Salary Band'] = pd.cut(
    population_df['Salary'],
    bins=edges,
    labels=labels,
    include_lowest=True,
    right=False
)

# Group by Salary Band
band_group = population_df.groupby('Salary Band')

salary_summary = band_group['Salary'].agg(
    Population_Count='count',
    Average_Salary='mean',
    Median_Salary='median'
)

# Add percentage of total
total_population = len(population_df)
salary_summary['Population_%'] = (salary_summary['Population_Count'] / total_population) * 100

print("Overall Salary Band Summary:")
print(salary_summary)

# Group by both State and Salary Band
state_band_group = population_df.groupby(['State', 'Salary Band'])

state_summary = state_band_group['Salary'].agg(
    Population_Count='count',
    Average_Salary='mean',
    Median_Salary='median'
).reset_index()

# Add population percentage per state
state_totals = population_df.groupby('State').size()
state_summary['Population_%'] = state_summary.apply(
    lambda row: (row['Population_Count'] / state_totals[row['State']]) * 100,
    axis=1
)

print("\nSalary Band Summary by State:")
print(state_summary)
