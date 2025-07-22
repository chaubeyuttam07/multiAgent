from langchain.document_loaders import (
    PyPDFLoader, UnstructuredWordDocumentLoader,
    UnstructuredPowerPointLoader, CSVLoader, TextLoader
)
import os

class IngestionAgent:
    def __init__(self, folder='data'):
        self.folder = folder

    def parse_documents(self):
        all_docs = []
        for file in os.listdir(self.folder):
            file_path = os.path.join(self.folder, file)
            if file.endswith('.pdf'):
                loader = PyPDFLoader(file_path)
            elif file.endswith('.docx'):
                loader = UnstructuredWordDocumentLoader(file_path)
            elif file.endswith('.pptx'):
                loader = UnstructuredPowerPointLoader(file_path)
            elif file.endswith('.csv'):
                loader = CSVLoader(file_path)
            elif file.endswith('.txt') or file.endswith('.md'):
                loader = TextLoader(file_path)
            else:
                continue
            docs = loader.load()
            all_docs.extend(docs)
        return all_docs
