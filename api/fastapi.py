from fastapi import FastAPI
from pydantic import BaseModel
from pipeline.run_pipeline import run_query

app = FastAPI(
    title="Enterprise RAG System",
    description="Api based RAG application",
    version="1.0"
)

class QueryRequest(BaseModel):
    question:str

@app.get("/")
def home():
    return {"Message": "App is running successfully"}

@app.post("/ask")
def generate_answer(request:QueryRequest):
    
    answer = run_query(request.question)
    return (
        {   "Question": request.question,
            "Answer":   answer
        }
    )