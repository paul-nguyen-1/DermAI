from fastapi import FastAPI, Request
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

@app.post("/")
async def generate_message(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    image_url = data.get("image_url")

    llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=GEMINI_API_KEY
    )
    if image_url:
        message = HumanMessage(
            content=[
                {"type": "text", "text": user_message},
                {"type": "image_url", "image_url": image_url}
            ]
        )
    else:
        message = HumanMessage(
            content=[
                {"type": "text", "text": user_message},
            ]
        )

    response = llm.invoke([message])
    return {"message": response.content}
