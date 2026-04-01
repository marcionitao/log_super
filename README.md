# Log Super

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.14+-blue?style=flat&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.128.0+-blue?style=flat&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat" alt="License">
</p>

Welcome to **Log Super**, a modern and high-performance API designed for efficient user management.

## 📖 About the Project

**Log Super** is a backend application built with a focus on performance, security, and scalability. It provides a complete set of RESTful endpoints for user administration, including:

- User creation, reading, updating, and deletion (CRUD)
- Secure authentication with password hashing (Argon2)
- Data validation using Pydantic models
- Database migrations with Alembic

The project follows development best practices, using modern tools from the Python ecosystem to ensure code quality, speed, and ease of maintenance.

## 🛠️ Technologies

This project uses the following technologies and tools:

| Category | Technology | Description |
|----------|------------|-------------|
| **Language** | [Python](https://www.python.org/) (>= 3.14) | Modern Python with latest features |
| **Framework** | [FastAPI](https://fastapi.tiangolo.com/) | High-performance web framework |
| **Database** | [SQLAlchemy](https://www.sqlalchemy.org/) + SQLite | ORM and database |
| **Migrations** | [Alembic](https://alembic.sqlalchemy.org/) | Database migration tool |
| **Validation** | [Pydantic](https://docs.pydantic.dev/) | Data validation using type hints |
| **Security** | [pwdlib](https://pypi.org/project/pwdlib/) | Password hashing (Argon2) |
| **Package Manager** | [Poetry](https://python-poetry.org/) | Dependency management |
| **Testing** | [Pytest](https://docs.pytest.org/) + pytest-cov | Testing framework with coverage |
| **Code Quality** | [Ruff](https://docs.astral.sh/ruff/) | Linter and formatter |
| **Task Runner** | [Taskipy](https://github.com/taskipy/taskipy) | Automate recurring commands |

## 🚀 Getting Started

### Prerequisites

- Python >= 3.14
- Poetry (for dependency management)

### Installation

1. Clone the repository and navigate to the project directory:

   ```bash
   git clone <repository-url>
   cd log_super
   ```

2. Install the dependencies:

   ```bash
   poetry install
   ```

### Running the Application

Start the development server with:

```bash
task run
```

The API will be available at:

| Service | URL |
|---------|-----|
| **API Base URL** | `http://127.0.0.1:8000` |
| **Swagger UI** | `http://127.0.0.1:8000/docs` |
| **ReDoc** | `http://127.0.0.1:8000/redoc` |
| **OpenAPI Schema** | `http://127.0.0.1:8000/openapi.json` |

### Interactive Documentation

- **Swagger UI**: Visit `http://127.0.0.1:8000/docs` to explore and test the API interactively.
- **ReDoc**: Visit `http://127.0.0.1:8000/redoc` for an alternative API documentation view.

## 🧪 Testing

Run the tests with coverage:

```bash
task test
```

Generate and open the coverage report:

```bash
task test_cov
```

## 📁 Project Structure

```
log_super/
├── src/log_super/       # Main application source code
│   ├── app.py          # FastAPI application instance
│   ├── models.py       # SQLAlchemy models
│   ├── schemas.py      # Pydantic schemas (DTOs)
│   ├── security.py     # Authentication & password handling
│   ├── database.py     # Database connection
│   └── settings.py     # Application settings
├── migrations/         # Alembic database migrations
├── tests/              # Test suite
│   ├── conftest.py    # Pytest fixtures
│   ├── test_app.py    # Application tests
│   └── test_db.py     # Database tests
├── pyproject.toml      # Project configuration
└── README.md          # This file
```

## 🔧 Available Commands

| Command | Description |
|---------|-------------|
| `task run` | Start the development server |
| `task test` | Run tests with coverage |
| `task test_cov` | Generate and open coverage report |
| `task migrate` | Create a new migration (usage: `task migrate -- your message`) |
| `task migrate_up` | Apply all pending migrations |

## 📤 Pushing to GitHub

To push your changes to GitHub, follow these steps:

1. Initialize the repository (if not already initialized):
   ```bash
   git init
   ```

2. Add the remote origin (replace `<your-username>` and `<your-repo>`):
   ```bash
   git remote add origin https://github.com/<your-username>/<your-repo>.git
   ```

3. Stage your changes:
   ```bash
   git add .
   ```

4. Create a commit with a descriptive message:
   ```bash
   git commit -m "Your commit message"
   ```

5. Push to the remote repository:
   ```bash
   git push -u origin main
   ```

> **Note**: If you're working on a feature branch, replace `main` with your branch name.

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Built with ❤️ by [Márcio](mailto:marcionitao@gmail.com)
