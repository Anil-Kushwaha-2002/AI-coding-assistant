from fastapi import FastAPI
from pydantic import BaseModel
import ollama

app = FastAPI()

class CodeRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {"message": "AI Coding Assistant API running"}


@app.post("/generate")
def generate_code(req: CodeRequest):

    try:

        response = ollama.chat(
            model="tinyllama",
            messages=[
                {"role": "user", "content": req.prompt}
            ]
        )

        return {
            "result": response["message"]["content"]
        }

    except Exception as e:

        return {
            "error": str(e)
        }