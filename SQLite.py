# Import SQLite
import sqlite3
# Create a connection to SQLite database
conn = sqlite3.connect('athlete_heights.db')

# Save each team's data into a separate table in the database
men_swim.to_sql('mens_swimming', conn, if_exists='replace', index=False)
women_swim.to_sql('womens_swimming', conn, if_exists='replace', index=False)
men_volley.to_sql('mens_volleyball', conn, if_exists='replace', index=False)
women_volley.to_sql('womens_volleyball', conn, if_exists='replace', index=False)

# Check that tables are created
cursor = conn.cursor()
cursor.execute("Select name from sqlite_master where type='table';")
print("Tables in database:", cursor.fetchall())
pd.read_sql_query("SELECT * FROM mens_swimming WHERE Height > 72", conn)
