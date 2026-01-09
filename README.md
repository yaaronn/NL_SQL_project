# NL → SQL Query Engine

An end-to-end Natural Language to SQL (NL→SQL) system that converts
business questions into safe, schema-aware SQL queries.

## Problem Statement
Business users often struggle to write SQL. This project demonstrates
how Generative AI can translate natural language questions into
correct and safe SQL queries.

## Features
- Natural language to SQL conversion
- Explicit schema injection to avoid hallucinations
- Assumption-based ambiguity handling
- Read-only SQL validation for safety
- Modular, production-style architecture

## Tech Stack
- Python
- SQL (SQLite)
- Prompt Engineering
- Git & GitHub
- (Planned) LangChain + LLM integration

## Example Questions
- Top 5 customers by revenue last year
- Products that were never sold
- Monthly sales trend for the last year
- Inactive customers in the last 6 months

## Architecture
NL Question → Prompt + Schema → SQL Generation → SQL Validation → Execution

## Future Improvements
- LangChain SQLChain integration
- Support for multiple databases
- Query result formatting
- User interface (CLI / Web).
## LLM Integration Note
The system is designed to integrate with real LLM providers.
For development and demonstration purposes, the LLM layer is mocked
to avoid external API quota dependency while preserving architecture.

