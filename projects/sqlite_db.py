
# Importing libraries
import sqlite3
import pandas as pd

# SQLite database connection
new_connection = sqlite3.connect(r'C:\Users\user\Desktop\Applied Python Files\demo5.db')

# Loading data into DataFrame
demo_data = pd.read_csv('demo5.csv')

# Write the data to a sqlite table
demo_data.to_sql('demo5', new_connection, if_exists = 'replace', index = False)

# Close connection to SQLite database
new_connection.close()