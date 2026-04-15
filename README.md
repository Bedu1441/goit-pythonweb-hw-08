# GoIT Python Web HW-08

REST API for managing contacts using FastAPI and PostgreSQL.

## Features

- Create, read, update, delete contacts
- Search by first name, last name, or email
- Get contacts with upcoming birthdays (next 7 days)
- Swagger (OpenAPI) documentation

## Tech Stack

- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Docker

## Project Structure

- `main.py` — API endpoints
- `models.py` — SQLAlchemy models
- `schemas.py` — Pydantic schemas
- `crud.py` — database logic
- `db.py` — database connection
- `.env` — environment variables

---

## Important Note (ARM Architecture)

This project was developed on a **Windows ARM (ARM64) machine**, which caused compatibility issues with some Python dependencies.

Specifically:

- packages like `httptools` (used by `uvicorn`) require native C compilation
- ARM architecture does not always have prebuilt wheels
- installation failed due to missing Microsoft C++ Build Tools and lack of ARM support

### Solution

To ensure stability and avoid platform-specific issues:

- the application is fully containerized using **Docker**
- all dependencies are installed inside a Linux container
- FastAPI runs reliably regardless of the host architecture

This approach reflects real-world backend development practices.

---

## Environment Variables

Example `.env`:

```env
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_HOST=host.docker.internal
POSTGRES_PORT=5433
Run Project

Build and run:

docker compose up --build

Open Swagger:

http://localhost:8010/docs
API Endpoints
POST /contacts — create contact
GET /contacts — get all contacts
GET /contacts/{id} — get one contact
PUT /contacts/{id} — update contact
DELETE /contacts/{id} — delete contact
GET /search?query= — search contacts
GET /birthdays — upcoming birthdays
Notes
PostgreSQL runs in Docker (external container)
API connects via host.docker.internal
All CRUD operations are implemented using SQLAlchemy ORM
Data validation handled by Pydantic
Conclusion

The project demonstrates:

REST API development with FastAPI
database integration with PostgreSQL
ORM usage (SQLAlchemy)
containerized deployment using Docker
handling platform-specific issues (ARM architecture)
```
