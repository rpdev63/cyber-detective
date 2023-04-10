from app.db import connect_to_db, read_sql_file

print("Create database and table if necessary")

# Connect to the database
conn = connect_to_db()
# Read the SQL query from a file
sql = read_sql_file('app/schema.sql')
# Execute the SQL query
for statement in sql.split(';'):
    conn.cursor().execute(statement)
conn.close()