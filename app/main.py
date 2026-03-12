from fastapi import FastAPI, HTTPException

from app.schemas import QuestionRequest, QuestionResponse
from app.rag import build_index, load_query_engine

app = FastAPI(title="AI Assistant General Knowledge")


@app.get("/")
def root():
    return {"message": "AI Assistant API is running"}


@app.post("/ingest")
def ingest_documents():
    try:
        build_index()
        return {"message": "Documents ingested successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ask", response_model=QuestionResponse)
def ask_question(request: QuestionRequest):
    try:
        query_engine = load_query_engine()
        response = query_engine.query(request.question)
        return QuestionResponse(answer=str(response))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
