import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('bankdatabase.db')  # Replace with your database name
cursor = conn.cursor()

# Execute a query to select all data from a table
cursor.execute("SELECT * FROM bankdata")  # Replace with your table name

# Fetch all rows
rows = cursor.fetchall()

# Print the data
for row in rows:
    print(row)

# Close the connection
conn.close()
