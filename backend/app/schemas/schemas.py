from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict, Any
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

class ResumeBase(BaseModel):
    file_name: str
    file_path: str

class ResumeCreate(ResumeBase):
    user_id: str

class ResumeResponse(ResumeBase):
    id: str
    parsed_content: Optional[Dict[str, Any]] = None
    ats_score: Optional[int] = None
    created_at: datetime

class JobBase(BaseModel):
    title: str
    company: str
    location: Optional[str] = None
    description: Optional[str] = None
    job_url: str

class JobResponse(JobBase):
    id: str
    source: Optional[str] = None
    posted_at: Optional[datetime] = None

class ApplicationBase(BaseModel):
    job_id: str
    resume_id: str
    cover_letter_id: Optional[str] = None
    status: str = "applied"

class ApplicationResponse(ApplicationBase):
    id: str
    applied_at: datetime
