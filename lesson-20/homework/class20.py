# Using chinook.db write pandas code.

# Customer Purchases Analysis:
# Find the total amount spent by each customer on purchases (considering invoices).
# Identify the top 5 customers with the highest total purchase amounts.
# Display the customer ID, name, and the total amount spent for the top 5 customers.

import sqlite3
import pandas as pd

# Connect to chinook.db
conn = sqlite3.connect('chinook.db')

# Read Invoices and Customers tables into DataFrames
invoices = pd.read_sql_query("SELECT InvoiceId, CustomerId, Total FROM Invoice", conn)
customers = pd.read_sql_query("SELECT CustomerId, FirstName, LastName FROM Customer", conn)

# 1. Calculate total amount spent by each customer
customer_totals = invoices.groupby('CustomerId')['Total'].sum().reset_index()

# 2. Merge with customers to get names
customer_totals = customer_totals.merge(customers, on='CustomerId')

# 3. Sort by total amount spent descending and get top 5
top5 = customer_totals.sort_values('Total', ascending=False).head(5)

# 4. Display the results: CustomerId, Name, Total
top5['FullName'] = top5['FirstName'] + ' ' + top5['LastName']
result = top5[['CustomerId', 'FullName', 'Total']]

print(result)

# 2. Album vs. Individual Track Purchases:
# Determine the percentage of customers who prefer to buy individual tracks instead of full albums.
# A customer is considered to prefer individual tracks if they have purchased only a subset of tracks from an album.
# Provide a summary of the percentage of customers who fall into each category (individual tracks vs. full albums).

import sqlite3
import pandas as pd

# Connect to chinook.db
conn = sqlite3.connect('chinook.db')

# Load tables
tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM Track", conn)
invoice_lines = pd.read_sql_query("SELECT InvoiceLineId, InvoiceId, TrackId FROM InvoiceLine", conn)
invoices = pd.read_sql_query("SELECT InvoiceId, CustomerId FROM Invoice", conn)

# Merge InvoiceLine with Invoice to get CustomerId for each purchased track
purchases = invoice_lines.merge(invoices, on='InvoiceId')[['CustomerId', 'TrackId']]
# Merge to get AlbumId for each purchased track
purchases = purchases.merge(tracks, on='TrackId')[['CustomerId', 'AlbumId', 'TrackId']]

# Get all album track counts
album_track_counts = tracks.groupby('AlbumId')['TrackId'].count().reset_index()
album_track_counts.columns = ['AlbumId', 'NumTracks']

# For each customer-album, count how many tracks of that album they bought
customer_album = purchases.groupby(['CustomerId', 'AlbumId'])['TrackId'].nunique().reset_index()
customer_album = customer_album.merge(album_track_counts, on='AlbumId')
customer_album['FullAlbum'] = customer_album['TrackId'] == customer_album['NumTracks']

# For each customer, did they ever buy a full album?
customer_pref = customer_album.groupby('CustomerId')['FullAlbum'].any().reset_index()
customer_pref['Preference'] = customer_pref['FullAlbum'].apply(
    lambda x: 'Full Album' if x else 'Individual Tracks'
)

# Calculate percentage
summary = customer_pref['Preference'].value_counts(normalize=True) * 100

print("Customer purchase preference (%):")
print(summary)

# Optional: show as DataFrame for easier reading
summary_df = summary.rename_axis('Preference').reset_index(name='Percentage')
print("\nSummary Table:")
print(summary_df)
