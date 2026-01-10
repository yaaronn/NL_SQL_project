from schema import SCHEMA
from prompt import PROMPT_TEMPLATE
from validator import is_safe_sql
from llm import generate_sql_from_llm
from db import execute_sql


def main():
    question = input("Ask a business question: ")

    prompt = PROMPT_TEMPLATE.format(
        schema=SCHEMA,
        question=question
    )

    print("\n--- GENERATED SQL ---")
    sql = generate_sql_from_llm(prompt)
    print(sql)

    if not is_safe_sql(sql):
        print("Unsafe SQL detected ❌")
        return

    print("\n--- QUERY RESULT ---")
    results = execute_sql(sql)
    for row in results:
        print(row)


if __name__ == "__main__":
    main()
