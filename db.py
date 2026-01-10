import sqlite3

def execute_sql(sql: str):
    try:
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]

        conn.close()
        return columns, rows

    except sqlite3.Error as e:
        raise RuntimeError(f"Database error: {e}")
