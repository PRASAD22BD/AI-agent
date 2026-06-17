from fastapi import FastAPI, BackgroundTasks
from playwright.async_api import async_playwright
import asyncio

app = FastAPI()

async def apply_to_job(job_url: str, resume_path: str, cover_letter: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        print(f"Applying to {job_url}...")
        await page.goto(job_url)
        
        # This is a generic placeholder. In reality, you'd need site-specific logic.
        # Example for a generic "Apply" button:
        try:
            await page.click('text=Apply')
            await asyncio.sleep(2)
            # Upload resume
            # await page.set_input_files('input[type="file"]', resume_path)
            # Fill cover letter
            # await page.fill('textarea', cover_letter)
            # await page.click('button[type="submit"]')
        except Exception as e:
            print(f"Failed to apply: {e}")
        
        await browser.close()

@app.post("/apply")
async def start_application(data: dict, background_tasks: BackgroundTasks):
    job_url = data.get("job_url")
    resume_path = data.get("resume_path")
    cover_letter = data.get("cover_letter")
    
    background_tasks.add_task(apply_to_job, job_url, resume_path, cover_letter)
    
    return {"status": "Application started in background"}

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 3000))
    uvicorn.run(app, host="0.0.0.0", port=port)
