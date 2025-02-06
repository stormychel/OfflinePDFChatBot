# 📖 Offline PDF AI Chatbot

This project allows you to chat with an **offline AI model** that understands your **PDF library**. It extracts text from PDFs, stores embeddings for efficient retrieval, and responds intelligently based on document content.

## 🚀 Features
- **Extract text** from PDFs automatically.
- **Generate embeddings** to store document knowledge.
- **Use FAISS** for fast similarity search.
- **Run locally** with an offline LLM (Llama 3, Mistral, GPT4All).
- **Chat in a CLI** and get relevant answers based on PDFs.

---

## 🛠️ Installation
### **1️⃣ Install Dependencies**
Run the following command to install required Python packages:
```bash
pip install pdfplumber sentence-transformers faiss-cpu langchain gpt4all
```

### **2️⃣ Download a Local LLM**
You need an offline AI model to generate responses. Download a model like **Mistral** or **Llama 3**:
```bash
# Using GPT4All
mkdir -p ~/.gpt4all
cd ~/.gpt4all
wget https://gpt4all.io/models/mistral-7b.gguf
```
Or, use **Ollama** to manage local models:
```bash
brew install ollama
ollama run mistral
```

---

## 📂 Usage
### **1️⃣ Add PDFs to `pdfs/` Folder**
Place all your PDFs inside the `pdfs/` directory:
```bash
mkdir pdfs
mv your_documents/*.pdf pdfs/
```

### **2️⃣ Run the Script**
Execute the script to process PDFs and launch the chatbot:
```bash
python offline_pdf_ai.py
```

### **3️⃣ Chat with the AI**
Once the script is running, type your queries:
```bash
You: What does the document say about AI ethics?
AI: AI ethics involve...
```
To exit, type `exit`.

---

## 🛠️ How It Works
1. **Extracts text** from PDFs using `pdfplumber`.
2. **Embeds text** using `sentence-transformers`.
3. **Stores embeddings** in FAISS for fast retrieval.
4. **Retrieves relevant text** when you ask a question.
5. **Uses a local AI model** to generate responses.

---

## 📌 Notes
- **Performance depends on the model size**: Smaller models (Mistral-7B) run faster but may be less accurate.
- **For better retrieval**: Ensure PDFs have clear structure (e.g., well-formed paragraphs).
- **You can swap models**: Modify the script to use `llama-cpp-python` or any other local LLM.

---

## 💡 Future Improvements
- [ ] Add a web-based UI.
- [ ] Enable multi-threaded query handling.
- [ ] Optimize text chunking for large documents.

---

### ✉️ Need Help?
https://www.michelstorms.com

