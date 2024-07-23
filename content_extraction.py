from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def extract_content(pdf_file):
    pdf_loader = PyPDFLoader(pdf_file)
    pages = pdf_loader.load_and_split()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    
    return pages, text_splitter

def create_context(tree):
    context = "\n\n".join(tree.nodes[node]['data'].content for node in tree.nodes)
    return context