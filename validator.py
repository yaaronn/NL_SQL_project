def is_safe_sql(sql: str) -> bool:
    """
    Basic safety check to ensure generated SQL is read-only.
    """
    forbidden_keywords = [
        "delete",
        "update",
        "drop",
        "truncate",
        "alter",
        "insert"
    ]

    sql_lower = sql.lower()
    return not any(keyword in sql_lower for keyword in forbidden_keywords)
