# Tron Address Info Microservice

This microservice provides information about a Tron network address, including its bandwidth, energy, and TRX balance. It exposes two API endpoints for querying address info and retrieving the history of requests with pagination.

---

## Features

- **POST** endpoint to query Tron address info by address.
- **GET** endpoint to retrieve the latest request logs with pagination.
- Saves each request in the database with the requested wallet address.
- Built with:
  - FastAPI
  - SQLAlchemy ORM
  - tronpy (for interacting with Tron network)
  - Pytest (unit and integration tests)

---

## Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd <repo-folder>
```

2. Create and activate a virtual environment:
```python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

3. To activate the Poetry virtual environment shell:
`poetry shell`

4. Install dependencies:

`poetry install`

---

## Configuration

- Configure the database connection URL in `app/database.py` or via environment variables as needed.
- Ensure your environment has internet access to connect to Tron network nodes.

---

## Running the Service

After activating the Poetry shell and installing dependencies, start the FastAPI server with:

```bash
poetry run uvicorn app.main:app --reload
```

The API will be accessible at:
http://127.0.0.1:8000

Testing

Run tests using Poetry:
```
poetry run pytest
```

Tests include:

    Integration tests for API endpoints (tests/test_api.py).

    Unit tests for database operations (tests/test_db.py).

Dependencies

    FastAPI
    SQLAlchemy
    tronpy
    Pytest