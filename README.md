# AI Coding Assistant
## 1. Local AI coding assistant built with:

- Backend   --> Python
- API       --> FastAPI (AI backend APIs)
- Model     --> Ollama - Local LLM deployment (tool that runs AI models locally on your computer)
- LLM Model  --> tinyllama, phi3, Code Llama, deepseek-coder (2,3.5,8,6 GB)
- pydantic   --> validates data coming into the API (ensures the request has the ✔correct data type, ✔correct structure, ✔automatic validation)
- uvicorn    --> Backend Server that Runs (FastAPI) API servers
- Streamlit  --> Frontend UI dashboards (create web interfaces quickly)
- Vector DB  --> FAISS
- Embedding  --> sentence-transformers


## 2. Project Workflow
```
User Prompt
   ↓
Streamlit UI (Frontend)
   ↓
FastAPI (Backend)
   ↓
Ollama Model
   ↓
Generated Code
   ↓
UI Display
```

## 3. Run Entire Project
Start 3 terminals-

### Terminal 1
Run Ollama
ollama run codellama

### Terminal 2
Run backend
cd backend
uvicorn server:app --reload

### Terminal 3
Run frontend
cd frontend
streamlit run app.py

#  4. 🚀 Result

You now have a local AI coding assistant like Copilot.
Features:
✔ Code generation
✔ Code explanation
✔ Bug fixing
✔ Algorithm generation

# Key point
- 1. No Need to Run ollama run Because when using Python API, Ollama automatically starts the model.