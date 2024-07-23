# Hierarchical Document QA System

This project implements a hierarchical document question-answering system using PDF content extraction, tree-based indexing, and advanced language models for retrieval and answer generation. It features a user-friendly Streamlit interface for easy interaction.

## Setup Instructions

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/hierarchical-document-qa.git
   cd hierarchical-document-qa
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Google API key:
   - Obtain a Google API key from the Google Cloud Console
   - Replace `YOUR_API_KEY_HERE` in `main.py` with your actual API key

## Dependencies

This project requires the following main libraries:
- langchain
- networkx
- PyPDF2
- google-generativeai
- streamlit

A complete list of dependencies can be found in the `requirements.txt` file.

## Running the System

To run the Streamlit app:

1. Navigate to the project directory
2. Run the following command:
   ```
   streamlit run main.py
   ```
3. Open your web browser and go to the URL provided by Streamlit (usually http://localhost:8501)
4. Upload a PDF file using the file uploader in the app
5. Enter your questions about the textbook in the text input field

## User Interface

The system features a web-based user interface built with Streamlit. It allows users to:
- Upload PDF files
- Ask questions about the uploaded document
- View answers and relevant content from the document

## Project Structure

- `content_extraction.py`: Handles PDF loading and text splitting
- `hierarchical_indexer.py`: Implements the tree-based document structure
- `retrieval.py`: Sets up the vector store and retrieval system
- `qa_system.py`: Implements the question-answering chain
- `main.py`: Orchestrates the entire process and implements the Streamlit interface

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

