# Project Guidelines

- Use Python 3.14 and `uv` for the project environment and commands.
- Run the tests from the repository root with `uv run --group dev pytest src/tests`.
- Add meaningful tests for behavior and edge cases when changing code.
- When changing behavior, check coverage for the affected module with `coverage.py`.
