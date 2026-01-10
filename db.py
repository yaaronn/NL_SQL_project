import sqlite3

def execute_sql(sql: str):
    try:
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute(sql)
        results = cur.fetchall()
        conn.close()
        return results

    except sqlite3.Error as e:
        raise RuntimeError(f"Database error: {e}")
