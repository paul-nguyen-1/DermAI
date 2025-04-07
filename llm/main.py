from fastapi import FastAPI, Request
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = FastAPI()

@app.post("/")
async def generate_message(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    model = genai.GenerativeModel(os.getenv("GEMINI_VERSION", "gemini-1.5-flash"))
    response = model.generate_content(user_message)

    return {"message": response.text}
