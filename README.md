# seshajalam-.g-wasserstoff-AiInternTask

Absolutely! Here's a complete and well-structured `README.md` file tailored to your project — based on your Streamlit app for uploading documents, extracting text, embedding it, and performing semantic search using FAISS.

---

## 📄 `README.md`

```markdown
# 📚 Gen-AI Document Research & Theme Identifier

This is a **Streamlit-based Generative AI application** built as part of the Wasserstoff Internship Task. The app allows users to upload documents (PDFs and scanned images), extract text using OCR, build a semantic index, and query the documents using a large language model approach with vector search.

---

## 🚀 Features

- ✅ Upload and process PDFs or scanned image files (PNG, JPG)
- ✅ Perform text extraction (OCR for images, parsing for PDFs)
- ✅ Build a **FAISS-based semantic search index** using `sentence-transformers`
- ✅ Search across all uploaded documents using natural language queries
- ✅ Display relevant document chunks with document source references
- 🚧 Coming Soon: Theme summarization + Groq LLM integration for answer generation

---

## 📁 Folder Structure

```

chatbot\_theme\_identifier/
├── main.py                  # Streamlit app entry point
├── requirements.txt         # All required Python libraries
├── backend/
│   ├── document\_loader.py   # Extracts text using OCR or PDF parsing
│   └── vector\_store.py      # Embedding + FAISS index for semantic search
├── data/                    # Stores uploaded files
└── README.md                # This file

````

---

## ⚙️ Setup Instructions

### 1. ✅ Clone the Repository or Download the Files

If using Git:

```bash
git clone <your-repo-url>
cd chatbot_theme_identifier
````

### 2. ✅ Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # Mac/Linux
```

### 3. ✅ Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. ✅ Install Tesseract OCR

* [Windows Installer](https://github.com/tesseract-ocr/tesseract/wiki)
* Make sure to set the correct path to `tesseract.exe` in `document_loader.py`:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## ▶️ Running the App

In your terminal or CMD:

```bash
streamlit run main.py
```

---

## 🧠 Technologies Used

* 🐍 Python 3.11
* 🧾 Streamlit
* 📄 PyMuPDF (PDF text extraction)
* 📸 Tesseract OCR (image text extraction)
* 🤗 SentenceTransformers (`all-MiniLM-L6-v2`)
* 🔍 FAISS (vector search)

---

## 🧪 Example Use Case

1. Upload 2+ documents (PDF or scanned images).
2. Click **"Build Search Index"**.
3. Enter a natural question like:

   * *"What penalty was imposed under SEBI Act?"*
   * *"What is the main issue discussed across these documents?"*
4. View the top relevant text chunks from the documents with source names.

---

## ✅ Coming Up

* 🧠 Integration with Groq's LLM (LLAMA 3) for generating answers with citations
* 📌 Theme identification across multiple documents
* 🗺️ Visual citation mapping interface

---

## 📬 Contact

For questions or support, reach out to:
**Divyansh Sharma – Wasserstoff**
📧 Email: [divyansh.sharma@thewasserstoff.com](mailto:divyansh.sharma@thewasserstoff.com)

---

## 📄 License

This project is for academic and internship evaluation purposes only.

```

---

Let me know if you’d like a shorter version or want to include images/screenshots in the README. You can also customize the *“Coming Up”* section based on your progress.
```
