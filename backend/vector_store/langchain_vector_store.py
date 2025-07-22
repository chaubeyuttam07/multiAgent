from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

import os

class VectorStoreWrapper:
    def __init__(self, persist_directory="outputs/faiss_index"):
        self.persist_directory = persist_directory
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.db = None

    def create_index(self, docs):
        self.db = FAISS.from_documents(docs, self.embeddings)
        self.db.save_local(self.persist_directory)

    def load_index(self):
        self.db = FAISS.load_local(self.persist_directory, self.embeddings)

    def search(self, query, k=3):
        return self.db.similarity_search(query, k=k)

