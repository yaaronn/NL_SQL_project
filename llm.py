def generate_sql_from_llm(prompt: str, retries: int = 2) -> str:
    """
    Mocked LLM response with retry support.
    """

    for attempt in range(1, retries + 1):
        try:
            # Mocked SQL (deterministic)
            return """
            SELECT
                c.customer_id,
                SUM(o.amount) AS total_revenue
            FROM customers c
            JOIN orders o
                ON c.customer_id = o.customer_id
            GROUP BY c.customer_id
            ORDER BY total_revenue DESC
            LIMIT 5;
            """
        except Exception as e:
            if attempt == retries:
                raise RuntimeError(
                    f"LLM failed after {retries} attempts"
                ) from e
