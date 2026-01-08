from schema import SCHEMA
from prompt import PROMPT_TEMPLATE
from validator import is_safe_sql


def generate_sql(prompt: str) -> str:
    """
    Placeholder for LLM call.
    For now, we return a hardcoded SQL for testing.
    """
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


def main():
    question = input("Ask a business question: ")

    prompt = PROMPT_TEMPLATE.format(
        schema=SCHEMA,
        question=question
    )

    print("\n--- PROMPT SENT TO LLM ---")
    print(prompt)

    sql = generate_sql(prompt)

    print("\n--- GENERATED SQL ---")
    print(sql)

    if is_safe_sql(sql):
        print("\nSQL passed safety validation ✅")
    else:
        print("\nUnsafe SQL detected ❌")


if __name__ == "__main__":
    main()
