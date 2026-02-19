import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Read schema.sql
with open("schema.sql", "r") as f:
    schema = f.read()

# Execute schema
cursor.executescript(schema)

# Save and close
conn.commit()
conn.close()

print("Database created successfully!")
