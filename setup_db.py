import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()

# Create tables
cur.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount REAL,
    order_date TEXT
)
""")

# Insert sample data
cur.executemany(
    "INSERT INTO customers VALUES (?, ?)",
    [
        (1, "Alice"),
        (2, "Bob"),
        (3, "Charlie")
    ]
)

cur.executemany(
    "INSERT INTO orders VALUES (?, ?, ?, ?)",
    [
        (1, 1, 500.0, "2024-01-10"),
        (2, 1, 300.0, "2024-02-12"),
        (3, 2, 700.0, "2024-03-01"),
        (4, 3, 200.0, "2024-03-15")
    ]
)

conn.commit()
conn.close()

print("Database setup complete.")

