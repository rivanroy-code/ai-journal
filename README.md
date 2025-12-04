# AI Journal

AI Journal is a next-generation personal journaling platform with an AI companion that truly understands you. Users can write daily entries and engage in conversations with an AI that remembers their full life context, offering insights, reflections, and emotional guidance. Think of it as a personal therapist, coach, and life assistant rolled into one.

---

# Key Features

- **Daily Journaling:** Capture your thoughts, feelings, and experiences with ease.  
- **AI Companion:** Chat with an AI that remembers your past entries and provides personalized responses.  
- **Memory Retrieval:** The AI recalls relevant past events, themes, and people to give contextually accurate advice.  
- **Secure Storage:** All journal data is encrypted and stored safely.  
- **Future Features (Roadmap):**
  - Weekly AI-generated life summaries  
  - Mood tracking & habit correlations  
  - Memory graph of recurring people, events, and themes  
  - AI personas (therapist, motivational coach, soft-supportive friend)  
  - Mobile app integration

---

# Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, FastAPI, SQLAlchemy |
| Frontend | Next.js, React, Tailwind CSS |
| Database | PostgreSQL (Supabase) |
| AI / Memory | OpenAI GPT-4 / GPT-3.5, ChromaDB / Pinecone |
| Deployment | Railway / Render (backend), Vercel (frontend) |

---

# Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/your-username/ai-journal.git
cd ai-journal
```

2. **Install backend dependencies**
```bash
pip install -r backend/requirements.txt
```

3. **Install frontend dependencies**
```bash
cd frontend
npm install
```

## Configure environment variables

# Backend
DATABASE_URL=your_postgres_url
OPENAI_API_KEY=your_openai_key
VECTOR_DB_API_KEY=your_vector_db_key

# Frontend
NEXT_PUBLIC_API_URL=http://localhost:8000

**Run backend**
```bash
uvicorn backend.main:app --reload
```

**Run frontend**
```bash
npm run dev
```
