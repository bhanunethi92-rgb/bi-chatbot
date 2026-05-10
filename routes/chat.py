from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from routes.upload import data_store
from services.ai_service import chat_with_data

router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@router.post("/chat")
def chat(request: ChatRequest):
    if "df" not in data_store:
        raise HTTPException(status_code=400, detail="Please upload a file first!")

    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty!")

    answer = chat_with_data(request.question, data_store["summary"])

    return {
        "question": request.question,
        "answer": answer
    }