import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st

from backend.agents.coordinator_agent import CoordinatorAgent

st.title("📄 LangChain Agentic RAG Chatbot")

if "agent" not in st.session_state:
    st.session_state.agent = CoordinatorAgent()

uploaded_files = st.file_uploader("Upload documents", type=["pdf", "docx", "pptx", "csv", "txt", "md"], accept_multiple_files=True)

if uploaded_files:
    os.makedirs("data", exist_ok=True)
    for f in uploaded_files:
        with open(os.path.join("data", f.name), "wb") as file:
            file.write(f.getbuffer())
    st.success("Files uploaded!")

if st.button("Process Documents"):
    st.session_state.agent.process_documents()
    st.success("Documents indexed and ready for questions!")

if "agent" in st.session_state:
    query = st.text_input("Ask a question:")
    if query:
        answer = st.session_state.agent.ask(query)
        st.write("### Answer")
        st.write(answer)
