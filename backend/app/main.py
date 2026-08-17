from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Knowledge(BaseModel):
    content: str


knowledge_data = []


@app.post("/knowledge")
def create_knowledge(knowledge: Knowledge):
    knowledge_data.append(knowledge.content)

    return {
        "message": "Knowledge received successfully!",
        "content": knowledge.content
    }


@app.get("/knowledge")
def get_knowledge():
    return {
        "knowledge": knowledge_data
    }