# Backend — AI Journal

The backend powers the core functionality of the AI Journal app. It handles user authentication, journal storage, vector embedding generation, AI memory retrieval, and API routes consumed by the frontend. It is built using Python and FastAPI, with PostgreSQL as the main database and a vector database (Pinecone or Chroma) for embedding storage.

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- PostgreSQL
- Pinecone / ChromaDB

## Setup Instructions
1. Create a Python virtual environment and activate it.
2. Install backend dependencies using `pip install -r requirements.txt`.
3. Create a `.env` file with:
   - `DATABASE_URL`
   - `OPENAI_API_KEY`
   - `VECTOR_DB_API_KEY`
4. Start the development server with `uvicorn main:app --reload`.

## Folder Structure
- `main.py` — FastAPI entrypoint.
- `routes/` — API endpoints.
- `models/` — Database tables using SQLAlchemy.
- `crud/` — Database operations.
- `services/` — AI logic, embeddings, and vector DB integration.
- `schemas/` — Pydantic models for validation.

## Notes
The backend stores journal entries in PostgreSQL and embeddings in a vector database for long-term contextual memory. It exposes a clean REST API for the Next.js frontend.
