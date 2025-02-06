import os
import pdfplumber
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain.llms import GPT4All  # or use llama-cpp-python for Llama models

# Configuration
PDF_FOLDER = "./pdfs"  # Folder containing PDFs
EMBEDDING_MODEL = "all-MiniLM-L6-v2"  # Local model for embeddings
VECTOR_DB_PATH = "./faiss_index"

# Load the embedding model
embedder = SentenceTransformer(EMBEDDING_MODEL)

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text

def process_pdfs():
    """Extracts and embeds text from all PDFs."""
    texts = []
    file_paths = []
    for file in os.listdir(PDF_FOLDER):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(PDF_FOLDER, file)
            text = extract_text_from_pdf(pdf_path)
            texts.append(text)
            file_paths.append(pdf_path)
    return texts, file_paths

def create_faiss_index(texts):
    """Embeds text and stores it in FAISS."""
    embeddings = embedder.encode(texts, convert_to_numpy=True)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    faiss.write_index(index, VECTOR_DB_PATH)
    return index

def search(query, index, texts):
    """Retrieves the most relevant PDF sections based on a query."""
    query_embedding = embedder.encode([query], convert_to_numpy=True)
    _, idxs = index.search(query_embedding, 3)  # Retrieve top 3 results
    results = [texts[i] for i in idxs[0]]
    return "\n\n---\n\n".join(results)

def chat_loop(index, texts):
    """Runs a simple chatbot interface."""
    model = GPT4All("mistral-7b.gguf")  # Adjust model name if using GPT4All or Llama
    print("Chatbot ready! Type 'exit' to quit.")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        context = search(query, index, texts)
        response = model.invoke(f"Context: {context}\nUser Question: {query}")
        print("AI:", response.strip())

if __name__ == "__main__":
    texts, file_paths = process_pdfs()
    index = create_faiss_index(texts)
    chat_loop(index, texts)
