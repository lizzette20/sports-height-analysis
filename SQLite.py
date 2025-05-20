 # Imports the SQLite module, which allows interaction with SQLite databases
import sqlite3

# Connects to the SQLite database
sqlconnect = sqlite3.connect('billboard_spotify.db')  # ✅ Connection established

# Saves the df3 DataFrame to the table in the database
df3.to_sql('tracks', sqlconnect, if_exists='replace', index=False)  # ✅ DataFrame saved to table

# Checks and prints all table names in the database to confirm the table was created
cursor = sqlconnect.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables in database:", cursor.fetchall())  # ✅ Shows existing tables

# Retrieves and prints the first 5 rows of the table as a quick preview
preview = pd.read_sql_query("SELECT * FROM tracks LIMIT 5;", sqlconnect)
print(preview)
