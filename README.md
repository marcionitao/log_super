# Log Super

Welcome to **Log Super**, a modern API designed for efficient user management.

## 🚀 About the Project

**Log Super** is a backend application built with a focus on performance and modernity, offering endpoints for user administration. The project follows development best practices, using current tools from the Python ecosystem to ensure quality, speed, and ease of maintenance.

## 🛠️ Technologies

This project is set up using the following technologies and tools:

- **[Python](https://www.python.org/)** (>= 3.14): The base language of the project, using modern features.
- **[FastAPI](https://fastapi.tiangolo.com/)**: A high-performance web framework for building APIs, based on open standards (OpenAPI and JSON Schema).
- **[Poetry](https://python-poetry.org/)**: A robust tool for dependency management and packaging.
- **[Pydantic](https://docs.pydantic.dev/)**: Data validation and settings management using type hints.
- **[Ruff](https://docs.astral.sh/ruff/)**: An extremely fast code linter and formatter, replacing tools like Flake8 and Black.
- **[Pytest](https://docs.pytest.org/)**: A mature framework for running automated tests.
- **[Taskipy](https://github.com/taskipy/taskipy)**: A simple task runner to automate recurring commands (like running the server or tests).

## 📦 Install

Make sure you have **Python** and **Poetry** installed in your environment.

1. Clone the repository and enter the directory:

   ```bash
   git clone <repository-url>
   cd log_super
   ```

1. Install the project dependencies:

   ```bash
   poetry install
   ```

## ▶️ How to Run

Thanks to `taskipy`, you can run the development server with a simple command configured in `pyproject.toml`:

```bash
task run
```

This will launch the FastAPI application. You will be able to access:

- **API**: `http://127.0.0.1:8000`
- **Interactive Documentation (Swagger UI)**: `http://127.0.0.1:8000/docs`
- **Alternative Documentation (ReDoc)**: `http://127.0.0.1:8000/redoc`

## 🧪 Development and Quality

The project already has code quality tools configured.

- **Linting e Formatação**: Managed by `ruff`.
- **Testes**: Run via `pytest` (with plugin `pytest-cov` installed).
