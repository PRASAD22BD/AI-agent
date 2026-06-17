# Production Setup Guide

## 1. Supabase Setup
- Create a new project in Supabase.
- Run the SQL in `supabase/schema.sql` in the SQL Editor.
- Enable Google OAuth in Authentication settings if needed.

## 2. Gemini API
- Get an API key from [Google AI Studio](https://aistudio.google.com/).

## 3. n8n Setup
- Deploy n8n (Render will handle this).
- Import the JSON workflows from `n8n/workflows/`.
- Configure the Supabase and Gemini credentials in n8n.

## 4. Render Deployment
- Connect your GitHub repository to Render.
- Render will automatically detect the `render.yaml` and prompt you for environment variables.
- Fill in the variables as defined in `.env.example`.

## 5. Playwright Worker
- The Playwright worker runs as a background service.
- Ensure the `PLAYWRIGHT_WORKER_URL` in n8n points to the Render service URL for Playwright.

## Local Development
1. Install dependencies:
   - Backend: `pip install -r backend/requirements.txt`
   - Frontend: `npm install`
2. Start services:
   - Backend: `uvicorn app.main:app --reload` (from `backend` folder)
   - Frontend: `npm run dev` (from `frontend` folder)
