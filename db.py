import sqlite3

def execute_sql(sql: str):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()

    cur.execute(sql)
    results = cur.fetchall()

    conn.close()
    return results
