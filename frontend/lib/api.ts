import axios from 'axios';

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
});

export const authApi = {
  signup: (data: any) => api.post('/auth/signup', data),
  login: (data: any) => api.post('/auth/login', data),
};

export const resumeApi = {
  upload: (formData: FormData) => api.post('/resumes/upload', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  }),
  optimize: (data: any) => api.post('/resumes/generate-ats', data),
};

export const jobApi = {
  getAll: () => api.get('/jobs'),
  match: (data: any) => api.post('/jobs/match', data),
};

export default api;
