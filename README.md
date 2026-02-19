# AI-Assistant-General-Knowledge-

A general-purpose personal AI assistant designed to help with daily tasks, learning, career, planning, writing, and decision-making, while grounding answers in your own documents and remembering personal preferences over time.
The system uses Retrieval-Augmented Generation (RAG) to ground responses in user-provided documents. Uploaded materials such as PDFs, notes, and project files are processed, chunked, embedded, and stored in a vector database. When a user submits a query, the system retrieves the most relevant document segments and injects them into the prompt before generating a response. This approach improves factual accuracy, reduces hallucinations, and ensures context-aware assistance.

Programming Language: Python

Backend Framework: FastAPI

Framework: LlamaIndex

Embeddings: OpenAI Embeddings API 

Vector Database : Chroma (local) 

Relational Database:  PostgreSQL

Document Processing: PyPDF, python-docx

Optional Frontend: Streamlit (initial prototype), React (planned upgrade)
