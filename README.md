# AI Assistant – General Knowledge (Javier)

A personal AI assistant designed to help with learning, planning, writing, and decision-making while grounding responses in user-provided documents.

The assistant uses **Retrieval-Augmented Generation (RAG)** to search and reason over uploaded documents.

---

## Features

- Document ingestion (PDF, DOCX, TXT)
- Semantic search using embeddings
- Local vector database with Chroma
- FastAPI backend for API access
- Question answering grounded in personal documents

---

## Architecture

User Question
↓  
FastAPI Backend  
↓  
LlamaIndex Retrieval  
↓  
Chroma Vector Database  
↓  
OpenAI Embeddings + Model  
↓  
Grounded Answer  

---

## Tech Stack

- Python
- FastAPI
- LlamaIndex
- OpenAI API
- Chroma Vector Database
- PyPDF
- python-docx

---

## Project Structure

AI-Assistant-General-Knowledge
│
├── app
│ ├── main.py
│ ├── rag.py
│ ├── loaders.py
│ ├── config.py
│ └── schemas.py
│
├── documents
├── chroma_db
├── requirements.txt
├── README.md
└── LICENSE  


---

## How to Run

1. Clone the repository

2. Create virtual environment

3. Install dependencies

4. Add environment variables

Create `.env

5. Start the backend

6. Open API docs

---

## Example API Request

---
POST /ask
{
"question": "What is this document about?"
}

---

## Future Improvements

- Add conversation memory
- Add source citations
- Build a frontend interface (React / Streamlit)
- Support multiple document collections


