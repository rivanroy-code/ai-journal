# AI Journal

AI Journal is a next-generation personal journaling platform with an AI companion that deeply understands you. Users can write daily entries and converse with an AI that remembers their entire life context, providing insights, reflections, and emotional guidance. It functions like a personal therapist, coach, and life assistant in one.

## Key Features
- Daily Journaling — Capture thoughts, feelings, and experiences securely.
- AI Companion — Chat with an AI that remembers all your past entries.
- Context-Aware Memory Retrieval — The AI references past events, themes, and people to deliver personalised guidance.
- Secure Storage — Fully encrypted journal data.
- Future Roadmap: weekly AI summaries, mood tracking, memory graph visualisation, AI personas (therapist, coach, friend), and mobile app support.

## Tech Stack
| Layer | Technology |
|-------|------------|
| Backend | Python, FastAPI, SQLAlchemy |
| Frontend | Next.js, React, Tailwind CSS |
| Database | PostgreSQL (Supabase) |
| AI / Memory Engine | OpenAI GPT models, ChromaDB / Pinecone |
| Deployment | Railway / Render (backend), Vercel (frontend) |

## Getting Started
Clone the repository:
git clone https://github.com/your-username/ai-journal.git
cd ai-journal

Backend setup:
pip install -r backend/requirements.txt

Create backend/.env:
DATABASE_URL=your_postgres_url
OPENAI_API_KEY=your_openai_key
VECTOR_DB_API_KEY=your_vector_db_key

Run backend:
uvicorn backend.main:app --reload

Frontend setup:
cd frontend
npm install

Create frontend/.env.local:
NEXT_PUBLIC_API_URL=http://localhost:8000

Run frontend:
npm run dev

## Project Structure
/backend        → FastAPI services, models, routes  
/frontend       → Next.js client UI  
/infrastructure → Deployment configs, CI/CD, infra scripts  

## Roadmap
- AI-powered summaries and progress reports  
- Cross-device sync  
- Mobile app  
- End-to-end encryption  
- Persona switching for the AI  
- Journaling streaks & milestone system  

## Author
Built by **Rivan Roy** as a software engineering and AI-driven mental well-being project.
