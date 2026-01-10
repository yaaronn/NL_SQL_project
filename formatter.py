def print_table(columns, rows):
    if not rows:
        print("No results found.")
        return

    col_widths = [
        max(len(str(col)), max(len(str(row[i])) for row in rows))
        for i, col in enumerate(columns)
    ]

    # Header
    header = " | ".join(col.ljust(col_widths[i]) for i, col in enumerate(columns))
    separator = "-+-".join("-" * w for w in col_widths)

    print(header)
    print(separator)

    # Rows
    for row in rows:
        print(
            " | ".join(str(value).ljust(col_widths[i]) for i, value in enumerate(row))
        )
