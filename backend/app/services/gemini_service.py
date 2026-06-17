import google.generativeai as genai
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

class GeminiService:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    async def parse_resume(self, resume_text: str):
        prompt = f"Parse the following resume and return a JSON object with skills, experience, and education:\n\n{resume_text}"
        response = self.model.generate_content(prompt)
        return response.text

    async def generate_cover_letter(self, resume_content: str, job_description: str):
        prompt = f"Generate a personalized cover letter based on the following resume and job description:\n\nResume:\n{resume_content}\n\nJob Description:\n{job_description}"
        response = self.model.generate_content(prompt)
        return response.text

    async def analyze_ats_score(self, resume_content: str, job_description: str):
        prompt = f"Analyze the following resume against the job description. Provide an ATS score (0-100), identify missing keywords, and suggest improvements in JSON format.\n\nResume:\n{resume_content}\n\nJob Description:\n{job_description}"
        response = self.model.generate_content(prompt)
        return response.text

gemini_service = GeminiService()
