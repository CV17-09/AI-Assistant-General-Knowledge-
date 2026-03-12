import chromadb
from llama_index.core import VectorStoreIndex, StorageContext, Document
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.settings import Settings

from app.config import OPENAI_API_KEY, CHROMA_PATH
from app.loaders import load_documents


def get_vector_store():
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    chroma_collection = chroma_client.get_or_create_collection("knowledge_base")
    return ChromaVectorStore(chroma_collection=chroma_collection)


def build_index():
    raw_docs = load_documents("documents")

    if not raw_docs:
        raise ValueError("No supported documents found in the documents folder.")

    documents = [
        Document(text=doc["text"], metadata={"filename": doc["filename"]})
        for doc in raw_docs
    ]

    embed_model = OpenAIEmbedding(
        api_key=OPENAI_API_KEY,
        model="text-embedding-3-small",
    )

    Settings.embed_model = embed_model

    vector_store = get_vector_store()
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
        embed_model=embed_model,
    )
    return index


def load_query_engine():
    embed_model = OpenAIEmbedding(
        api_key=OPENAI_API_KEY,
        model="text-embedding-3-small",
    )

    Settings.embed_model = embed_model

    vector_store = get_vector_store()
    index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store,
        embed_model=embed_model,
    )

    return index.as_query_engine(similarity_top_k=3)
