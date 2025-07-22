# backend/agents/llm_response_agent.py

import streamlit as st
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq


class LLMResponseAgent:
    def __init__(self, retriever):
        self.retriever = retriever
        self.llm = ChatGroq(
            groq_api_key=st.secrets["GROQ_API_KEY"],
            model=st.secrets.get("GROQ_MODEL", "llama3-70b-8192")
        )

        prompt_template = """Use the following context to answer the question:
        {context}

        Question: {question}
        Answer:"""

        prompt = PromptTemplate.from_template(prompt_template)

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.retriever,
            chain_type_kwargs={"prompt": prompt}
        )

    def generate(self, query):
        return self.qa_chain.invoke(query)
