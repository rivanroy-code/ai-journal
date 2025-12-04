# Infrastructure — AI Journal

The infrastructure layer contains deployment configuration, CI/CD workflows, and environment setup for the entire AI Journal system. It ensures smooth deployment of the frontend, backend, database, and vector database.

## Responsibilities
- Deployment scripts/configs
- Database provisioning and migrations
- Vector database setup
- CI/CD automation (GitHub Actions)
- Environment configuration

## Tech Stack
- Vercel (frontend hosting)
- Railway / Render (backend hosting)
- Supabase / PostgreSQL (database)
- Pinecone / ChromaDB (vector memory store)
- GitHub Actions (CI/CD automation)

## Setup Instructions
1. Connect the GitHub repo to Vercel, Railway/Render, and Supabase.
2. Add the necessary production environment variables.
3. Push changes — CI/CD will automatically deploy.
4. Review deployment logs in GitHub Actions.

## Folder Structure
- `ci-cd/` — GitHub Actions workflows.
- `docker/` — Dockerfiles if needed.
- `configs/` — Environment & deployment configuration files.

## Notes
`.env` files must never be committed. Use encrypted environment variables in hosting platforms. Databases and vector DBs should be configured before deploying production builds.
