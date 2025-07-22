import streamlit as st
from ingestion.parse_pdf import extract_text_from_pdf
from ingestion.parse_pptx import extract_text_from_pptx
from ingestion.parse_csv import read_csv
from ingestion.parse_docx import extract_text_from_docx
from response.response_agent import ResponseAgent

st.title("Document QA Chatbot")

uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'pptx', 'csv', 'docx', 'txt'])

if uploaded_file:
    file_type = uploaded_file.type
    text = ""

    if file_type == 'application/pdf':
        text = extract_text_from_pdf(uploaded_file)
    elif file_type == 'application/vnd.openxmlformats-officedocument.presentationml.presentation':
        text = extract_text_from_pptx(uploaded_file)
    elif file_type == 'text/csv':
        text = read_csv(uploaded_file)
    elif file_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        text = extract_text_from_docx(uploaded_file)

    st.write("Extracted Text:")
    st.write(text)

    if text:
        agent = ResponseAgent()
        question = st.text_input("Ask a question about the document:")
        if question:
            answer = agent.generate_response(question, text)
            st.write("Answer:")
            st.write(answer)