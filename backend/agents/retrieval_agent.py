from ..vector_store.langchain_vector_store import VectorStoreWrapper

class RetrievalAgent:
    def __init__(self):
        self.vstore = VectorStoreWrapper()

    def build_index(self, docs):
        self.vstore.create_index(docs)

    def retrieve_context(self, query):
        return self.vstore.search(query, k=3)
