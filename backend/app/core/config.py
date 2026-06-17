from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Job Application Agent"
    API_V1_STR: str = "/api/v1"
    
    # Supabase
    SUPABASE_URL: str = "https://placeholder.supabase.co"
    SUPABASE_KEY: str = "placeholder"
    SUPABASE_JWT_SECRET: str = "placeholder"
    
    # Gemini
    GEMINI_API_KEY: str = "placeholder"
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
