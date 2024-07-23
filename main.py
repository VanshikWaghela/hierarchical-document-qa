import os
import streamlit as st
from content_extraction import extract_content, create_context
from hierarchical_indexer import HierarchicalIndexer
from retrieval import setup_retrieval
from qa_system import setup_qa_system, answer_question
from langchain_google_genai import GoogleGenerativeAI

# Set your Google API key
GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def main():
    st.title("Textbook QA System")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file:
        # Save uploaded file temporarily
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Load PDF and extract content
        pages, text_splitter = extract_content(uploaded_file.name)

        # Create hierarchical index
        indexer = HierarchicalIndexer()
        tree = indexer.build_index(pages)

        # Create context and split into chunks
        context = create_context(tree)
        texts = text_splitter.split_text(context)

        # Setup retrieval system
        vector_index = setup_retrieval(texts, GOOGLE_API_KEY)

        # Setup QA system
        model = GoogleGenerativeAI(model="models/text-bison-001")
        qa_chain = setup_qa_system(model, vector_index)

        # Streamlit user interface
        question = st.text_input("Enter your question about the textbook:")
        if question:
            answer = answer_question(qa_chain, question)
            st.write(f"Question: {question}")
            st.write(f"Answer: {answer}")

            st.write("Relevant Content:")
            relevant_docs = vector_index.get_relevant_documents(question)
            for i, doc in enumerate(relevant_docs):
                st.write(f"- Content: {doc.page_content[:100]}...")
                st.write(f"  Metadata: {doc.metadata}")

if __name__ == "__main__":
    main()