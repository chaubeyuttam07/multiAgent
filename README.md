# Agentic RAG Chatbot for Multi-Format Document QA

## Overview

This project implements an agent-based Retrieval-Augmented Generation (RAG) chatbot designed to answer questions using documents in various formats. The architecture incorporates a Model Context Protocol (MCP) for communication between agents.

## Features

- **Multi-Format Support:** Upload and parse documents in PDF, PPTX, CSV, DOCX, and TXT.
- **Agentic Architecture:**
  - **IngestionAgent:** Parses and preprocesses documents.
  - **RetrievalAgent:** Handles embeddings and semantic retrieval.
  - **LLMResponseAgent:** Forms queries and generates answers using LLMs.
- **User Interface:** Allows document uploads, multi-turn questions, and response display with source context.
- **Scalable and Modular Design**

## Installation

1. **Clone the Repository:**

   ```bash
   git clone  https://github.com/chaubeyuttam07/multiAgent.git
   cd multiAgent
   ```

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    pip install -r requirements.txt
   ```

   ```bash
   python src/ui/app.py
   ```

### Instructions

- Replace `<your-repo-URL>` with your actual GitHub repository URL.
- Update any placeholder text such as email addresses.
- Customize sections as needed to suit your specific project nuances.

Let me know if you need any further customization!
