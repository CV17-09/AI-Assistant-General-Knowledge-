🤖 AI Assistant – General Knowledge (Javier)

A personal AI assistant built to help with learning, planning, writing, productivity, and decision-making while grounding every response in your uploaded documents.

Instead of guessing, Javier uses Retrieval-Augmented Generation (RAG) to search your files first, then generate smarter and more reliable answers.

✨ Features

📄 Document Ingestion
Upload and process files such as PDF, DOCX, and TXT

🧠 Semantic Search
Find relevant information based on meaning, not just keywords

📚 Grounded Question Answering
Answers based on your own uploaded documents

⚡ FastAPI Backend
Modern REST API for fast and scalable access

🗂️ Local Vector Storage
Uses Chroma for storing searchable embeddings locally

🔍 Smart Retrieval Pipeline
Combines LlamaIndex + OpenAI for context-aware answers

🏗️ Architecture
User Question
     ↓
⚡ FastAPI Backend
     ↓
🧠 LlamaIndex Retrieval Engine
     ↓
🗂️ Chroma Vector Database
     ↓
🤖 OpenAI Embeddings + Model
     ↓
✅ Grounded Answer

🛠️ Tech Stack

🐍 Python
⚡ FastAPI
🧠 LlamaIndex
🤖 OpenAI API
🗂️ Chroma Vector Database
📄 PyPDF
📝 python-docx

📂 Project Structure

AI-Assistant-General-Knowledge/
│── app/
│   ├── main.py
│   ├── rag.py
│   ├── loaders.py
│   ├── config.py
│   └── schemas.py
│
│── documents/
│── chroma_db/
│── requirements.txt
│── README.md
└── LICENSE

🚀 How to Run
1️⃣ Clone the Repository
git clone https://github.com/yourusername/AI-Assistant-General-Knowledge.git
cd AI-Assistant-General-Knowledge

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Environment Variables

Create a .env file:

OPENAI_API_KEY=your_api_key_here
5️⃣ Start the Backend
uvicorn app.main:app --reload

6️⃣ Open API Docs
http://127.0.0.1:8000/docs

📬 Example API Request
POST /ask
{
  "question": "What is this document about?"
}

🌟 Future Improvements

🧠 Add conversation memory
📌 Add source citations
💻 Build frontend (React / Streamlit)
📂 Support multiple document collections
🔐 Add user authentication
☁️ Deploy to cloud
