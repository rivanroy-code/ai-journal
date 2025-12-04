# Frontend — AI Journal

The frontend is the user interface for the AI Journal app. It is built using Next.js and Tailwind CSS, with ShadCN for UI components. It communicates with the FastAPI backend for authentication, journal operations, and AI chat responses.

## Tech Stack
- Next.js
- React
- Tailwind CSS
- ShadCN UI
- Axios / Fetch API

## Setup Instructions
1. Install dependencies using `npm install`.
2. Create a `.env.local` file with:
   - `NEXT_PUBLIC_API_URL`
3. Start the development server using `npm run dev`, then visit `http://localhost:3000`.

## Folder Structure
- `pages/` — App routes such as login, dashboard, chat, journal.
- `components/` — Reusable UI components.
- `styles/` — Tailwind and global styles.
- `lib/` — API utilities.
- `hooks/` — Custom React hooks.

## Notes
All frontend API calls are routed to the FastAPI backend. The interface is optimised for quick iteration and a clean modern look using Tailwind and ShadCN.
