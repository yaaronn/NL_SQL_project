from schema import SCHEMA
from prompt import PROMPT_TEMPLATE
from validator import is_safe_sql
from llm import generate_sql_from_llm
from db import execute_sql


def main():
    question = input("Ask a business question: ")

    try:
        prompt = PROMPT_TEMPLATE.format(
            schema=SCHEMA,
            question=question
        )

        sql = generate_sql_from_llm(prompt)

        print("\n--- GENERATED SQL ---")
        print(sql)

        if not is_safe_sql(sql):
            raise ValueError("Unsafe SQL detected")

        results = execute_sql(sql)

        print("\n--- QUERY RESULT ---")
        for row in results:
            print(row)

    except Exception as e:
        print("\n❌ ERROR OCCURRED")
        print(str(e))


if __name__ == "__main__":
    main()
