def generate_sql_from_llm(prompt: str) -> str:
    """
    Mocked LLM response.
    This simulates SQL generation without external API dependency.
    """

    # You can change this SQL to test different NL→SQL cases
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
