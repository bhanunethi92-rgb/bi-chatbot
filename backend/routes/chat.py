from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.ai_service import chat_with_data
import traceback

router = APIRouter()

# Local data store
data_store = {}

class ChatRequest(BaseModel):
    question: str

@router.post("/chat")
def chat(request: ChatRequest):
    try:
        from routes.upload import data_store as upload_store
        
        if "df" not in upload_store:
            raise HTTPException(status_code=400, detail="Please upload a file first!")

        answer = chat_with_data(request.question, upload_store["summary"])

        return {
            "question": request.question,
            "answer": answer
        }
    except HTTPException:
        raise
    except Exception as e:
        print("CHAT ERROR:", str(e))
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))