import os
from glob import glob
from langchain_community.document_loaders import (
    PyPDFLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredPowerPointLoader,
    CSVLoader,
    TextLoader,
)

class IngestionAgent:
    def __init__(self, folder='data'):
        self.folder = folder

    def parse_documents(self):
        all_docs = []
        # Recursively find supported files
        file_patterns = ["*.pdf", "*.docx", "*.pptx", "*.csv", "*.txt", "*.md"]
        all_files = []
        for pattern in file_patterns:
            all_files.extend(glob(os.path.join(self.folder, "**", pattern), recursive=True))

        if not all_files:
            print(f"[WARN] No supported documents found in folder: {self.folder}")

        for file_path in all_files:
            try:
                ext = os.path.splitext(file_path)[1].lower()
                if ext == '.pdf':
                    loader = PyPDFLoader(file_path)
                elif ext == '.docx':
                    loader = UnstructuredWordDocumentLoader(file_path)
                elif ext == '.pptx':
                    loader = UnstructuredPowerPointLoader(file_path)
                elif ext == '.csv':
                    loader = CSVLoader(file_path)
                elif ext in ['.txt', '.md']:
                    loader = TextLoader(file_path, encoding="utf-8")
                else:
                    print(f"[SKIP] Unsupported file type: {file_path}")
                    continue

                docs = loader.load()
                all_docs.extend(docs)
                print(f"[INFO] Loaded {len(docs)} docs from: {file_path}")

            except Exception as e:
                print(f"[ERROR] Failed to load {file_path}: {e}")

        return all_docs
