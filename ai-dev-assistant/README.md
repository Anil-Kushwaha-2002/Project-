# AI Coding Assistant (Real AI Developer Tool)
The goal is to make an assistant that understands an entire codebase, not just a single prompt.

Features we will build

1️⃣ AI understands entire project
2️⃣ Vector database for code search
3️⃣ Chat with codebase
4️⃣ Multi-file debugging
5️⃣ Copilot-style suggestions

# 1️⃣ High-Level Architecture (RAG)
This architecture is called RAG (Retrieval Augmented Generation).
```
User (Streamlit UI)
        │
        ▼
FastAPI Backend
        │
        ▼
Code Parser
        │
        ▼
Embedding Model
        │
        ▼
Vector Database (FAISS)
        │
        ▼
Relevant Code Context
        │
        ▼
LLM (Ollama)
        │
        ▼
AI Response
```

# 2️⃣ Project Folder Structure
The codebase folder will contain the project the AI reads.
```
ai-dev-assistant/
│
├── backend/
│   ├── server.py
│   ├── code_loader.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── requirements.txt
│
├── frontend/
│   └── app.py
│
├── codebase/
│   ├── sample1.py
│   ├── sample2.py
│
└── README.md
```
# 3️⃣ Required Libraries
| Library               | Purpose                   |
| --------------------- | ------------------------- |
| sentence-transformers | convert code → embeddings |
| faiss                 | vector database           |
| ollama                | run LLM                   |
| fastapi               | backend API               |

# 4️⃣ Code_Loader (Read Entire Project)
Purpose:-
- ✔ reads all project files
- ✔ sends them to AI

# 5️⃣ Create Embeddings
Embeddings convert code → numerical vectors.
Example:-
- def login(user,password)
becomes:-
- [0.12, -0.53, 0.91, ...]

# 6️⃣ Vector_Store Vector Database (FAISS)
This allows semantic code search.

# 7️⃣ Backend Server

# 8️⃣ Frontend UI

# 9️⃣ Example Questions
You can ask:-
- Explain how authentication works in this project
- How does the API work ?
- Refactor the database connection code
- Find bugs in the login function

# 🔟 What Makes This Project Powerful
This project demonstrates real AI engineering skills:
| Feature          | Industry Use    |
| ---------------- | --------------- |
| RAG architecture | ChatGPT plugins |
| Vector search    | GitHub Copilot  |
| Code embeddings  | AI dev tools    |
| Local LLM        | privacy AI      |

# 🏆 Why This Is Strong
### This project shows:-
- 1. LLM integration
- 2. RAG pipelines
- 3. vector databases
- 4. code analysis AI

### Very valuable for:-
- 1. AI engineer
- 2. ML engineer
- 3. LLM engineer