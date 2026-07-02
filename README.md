# 🤖 Javier – AI Assistant for General Knowledge

> **A Retrieval-Augmented Generation (RAG) AI assistant that answers questions using your own documents instead of relying solely on an LLM's general knowledge. Built with FastAPI, LlamaIndex, OpenAI, and Chroma for accurate, context-aware responses.**

---

# 🚀 Overview

Javier is an AI-powered personal assistant designed to help users learn, research, write, plan, and make informed decisions using their own knowledge base.

Rather than generating answers from memory alone, Javier first searches uploaded documents to retrieve the most relevant information before generating a response. This Retrieval-Augmented Generation (RAG) approach produces more accurate, explainable, and trustworthy answers.

Whether you're searching class notes, technical documentation, research papers, or company files, Javier provides fast and context-aware assistance grounded in your data.

---

# 🎯 Project Goals

- Build a scalable Retrieval-Augmented Generation (RAG) system
- Enable semantic search across uploaded documents
- Improve answer accuracy by grounding responses in retrieved context
- Provide a REST API for AI-powered document question answering
- Demonstrate modern LLM application architecture

---

# ✨ Features

### 📄 Document Ingestion

Upload and process multiple document formats, including:

- PDF
- DOCX
- TXT

---

### 🧠 Semantic Search

Instead of matching keywords, Javier understands the **meaning** of your query and retrieves the most relevant document sections.

---

### 📚 Grounded Question Answering

Every response is generated using information retrieved directly from your uploaded documents, reducing hallucinations and improving reliability.

---

### ⚡ FastAPI Backend

A lightweight, high-performance REST API built with FastAPI enables efficient communication between users and the AI assistant.

---

### 🗂️ Local Vector Database

Document embeddings are stored locally using **Chroma**, allowing for fast semantic retrieval without relying on external databases.

---

### 🔍 Intelligent Retrieval Pipeline

The application combines:

- LlamaIndex
- OpenAI Embeddings
- Chroma Vector Database

to retrieve relevant context before generating responses.

---

# 🏗️ System Architecture

```text
                 User Question
                       │
                       ▼
             ⚡ FastAPI REST API
                       │
                       ▼
         🧠 LlamaIndex Retrieval Engine
                       │
                       ▼
        🗂️ Chroma Vector Database
                       │
                       ▼
        🤖 OpenAI Embeddings + LLM
                       │
                       ▼
          ✅ Context-Aware Response
```

---

# 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Backend development |
| ⚡ FastAPI | REST API framework |
| 🧠 LlamaIndex | Retrieval pipeline |
| 🤖 OpenAI API | Embeddings and answer generation |
| 🗂️ Chroma | Local vector database |
| 📄 PyPDF | PDF document processing |
| 📝 python-docx | Word document parsing |
| 🔐 Python-dotenv | Environment variable management |

---

# 🔄 RAG Workflow

### 1️⃣ Document Upload

Users upload one or more documents to the system.

↓

### 2️⃣ Document Processing

The assistant:

- Extracts document text
- Cleans the content
- Splits it into manageable chunks

↓

### 3️⃣ Embedding Generation

Each chunk is converted into vector embeddings using the OpenAI Embeddings API.

↓

### 4️⃣ Vector Storage

Embeddings are indexed and stored in Chroma for efficient semantic search.

↓

### 5️⃣ User Question

A user submits a natural language question through the API.

↓

### 6️⃣ Context Retrieval

LlamaIndex retrieves the document chunks that are most relevant to the user's question.

↓

### 7️⃣ Answer Generation

The retrieved context is sent to the OpenAI model, which generates a grounded response based on the source documents.

---

# 📂 Project Structure

```text
AI-Assistant-General-Knowledge/
│
├── app/
│   ├── main.py              # FastAPI application
│   ├── rag.py               # Retrieval-Augmented Generation pipeline
│   ├── loaders.py           # Document loaders
│   ├── config.py            # Configuration settings
│   └── schemas.py           # API request/response models
│
├── documents/               # Uploaded documents
│
├── chroma_db/               # Local vector database
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Assistant-General-Knowledge.git

cd AI-Assistant-General-Knowledge
```

---

## 2️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### macOS/Linux

```bash
python -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## 5️⃣ Start the API

```bash
uvicorn app.main:app --reload
```

---

## 6️⃣ Open the Interactive API

After the server starts, visit:

```
http://127.0.0.1:8000/docs
```

FastAPI automatically provides Swagger UI for testing endpoints.

---

# 📬 Example API Request

### Endpoint

```http
POST /ask
```

### Request Body

```json
{
  "question": "What is this document about?"
}
```

### Example Response

```json
{
  "answer": "The uploaded document discusses the architecture of a Retrieval-Augmented Generation system and explains how document retrieval improves answer accuracy."
}
```

---

# 📈 Potential Use Cases

- 📚 Study assistant
- 📄 Research paper exploration
- 🏢 Internal company knowledge base
- ⚖️ Legal document search
- 🩺 Medical document lookup
- 📖 Technical documentation assistant
- 💼 Enterprise knowledge management

---

# 🚀 Future Improvements

- 💬 Multi-turn conversation memory
- 📌 Source citations for every answer
- 🌐 React or Streamlit frontend
- 📂 Multiple document collections
- 👤 User authentication and authorization
- ☁️ Cloud deployment
- 📤 File upload API endpoint
- 🔍 Hybrid keyword + semantic search
- ⚡ Streaming AI responses

---

# 📚 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Large Language Model Integration
- FastAPI Development
- Vector Databases
- Semantic Search
- OpenAI API Integration
- Prompt Engineering
- Document Processing
- REST API Design
- AI Application Development

---

# ⭐ Support

If you found this project useful or interesting, consider giving it a **⭐ Star** on GitHub!

It helps support future development and makes the project easier for others to discover.
