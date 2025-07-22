from .ingestion_agent import IngestionAgent
from .retrieval_agent import RetrievalAgent
from .llm_response_agent import LLMResponseAgent

class CoordinatorAgent:
    def __init__(self):
        self.ingestor = IngestionAgent()
        self.retriever_agent = RetrievalAgent()
        self.llm_agent = None

    def process_documents(self):
        docs = self.ingestor.parse_documents()
        self.retriever_agent.build_index(docs)
        self.llm_agent = LLMResponseAgent(self.retriever_agent.vstore.db.as_retriever())

    def ask(self, query):
        return self.llm_agent.generate(query)
