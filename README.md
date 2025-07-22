# Agentic RAG Chatbot for Multi-Format Document QA

## Overview

This project implements an agent-based Retrieval-Augmented Generation (RAG) chatbot that answers questions using documents of various formats. It utilizes Langchain for building language model applications, LangGraph for orchestrating language model interactions, and Streamlit for the UI.

## Features

- **Multi-Format Support:** Upload and parse documents in PDF, PPTX, CSV, DOCX, and TXT.
- **Agentic Architecture:**
  - **IngestionAgent:** Parses and preprocesses documents.
  - **RetrievalAgent:** Handles embeddings and semantic retrieval.
  - **LLMResponseAgent:** Forms queries using retrieved context and generates answers.
- **User Interface:** Built with Streamlit for seamless interaction and visualization.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone  https://github.com/chaubeyuttam07/multiAgent.git
   cd multiAgent
   ```
2. **Setup the Environment variable:**

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    pip install -r requirements.txt
   ```
3. **Run the Project:**

   ```bash
    streamlit run src/ui/app.py
   ```




