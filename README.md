# Natural Language to SQL Query Engine (NL → SQL)

An end-to-end Python project that converts business questions written in natural language into **safe, schema-aware SQL queries**.

The project demonstrates how Generative AI concepts and prompt engineering can simplify database querying while incorporating SQL validation and ambiguity handling.

## Problem Statement

Business users often need database insights but may not have the SQL knowledge required to retrieve them.

This project explores a solution that translates natural language questions into SQL queries while using explicit database schema context and read-only validation to improve query reliability and safety.

## Key Features

- **Natural Language to SQL:** Convert business questions into SQL queries.
- **Schema-Aware Generation:** Inject database schema information into prompts to reduce incorrect table and column references.
- **Ambiguity Handling:** Use explicit assumptions when a question is unclear.
- **SQL Safety Validation:** Validate generated queries against read-only SQL constraints before execution.
- **Modular Architecture:** Separate query generation, validation, and execution responsibilities.

## Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| Database | SQLite |
| Query Language | SQL |
| AI Concepts | Prompt Engineering |
| Version Control | Git & GitHub |

**Planned enhancements:** LangChain and live LLM provider integration.

## Example Business Questions

The system is designed around questions such as:

- Who are the top 5 customers by revenue last year?
- Which products have never been sold?
- What is the monthly sales trend for the last year?
- Which customers have been inactive during the last 6 months?

## System Architecture

```text
Natural Language Question
          |
          v
   Prompt + Database Schema
          |
          v
      SQL Generation
          |
          v
     SQL Validation
          |
          v
    Query Execution
          |
          v
      Query Results
```

## LLM Integration Approach

The architecture is designed to support integration with external LLM providers.

For development and demonstration purposes, the LLM layer is currently mocked. This avoids external API quota dependencies while allowing the query-generation and validation workflow to be developed and demonstrated.

Live LLM integration is a planned enhancement.

## Future Improvements

- Integrate LangChain SQLChain.
- Connect real LLM providers.
- Support multiple database systems.
- Improve query result formatting.
- Build a CLI or web-based interface.

## Project Highlights

- Explores natural-language interfaces for relational databases.
- Applies schema-aware prompt construction.
- Incorporates read-only SQL validation.
- Demonstrates modular design for an AI-assisted backend workflow.

## Author

**Yeshwanth Aaron**

- GitHub: https://github.com/yaaronn
- Portfolio: https://yaaron.site
- LinkedIn: https://www.linkedin.com/in/yeshwanth-aaron-7441a1205/
