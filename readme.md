# AI-Powered M&A Due Diligence Assistant

An offline AI-powered M&A Due Diligence Assistant built using Retrieval-Augmented Generation (RAG), FAISS, and Ollama. The application analyzes business documents, answers user queries, and generates professional due diligence reports without relying on cloud APIs.

---

## Overview

This project simplifies the due diligence process by enabling users to upload PDF documents, perform semantic search, interact with a local large language model, and generate structured reports. The entire pipeline runs locally, ensuring data privacy and offline accessibility.

---

## Features

* Upload and analyze PDF documents
* Text extraction using PyMuPDF
* Intelligent document chunking
* Local embeddings using Ollama (`nomic-embed-text`)
* Semantic search with FAISS
* AI-powered question answering using Llama 3.2
* Automated due diligence analysis
* Export reports in PDF and Markdown
* Fully offline architecture

---

## System Architecture

```text
PDF Upload
     │
     ▼
Text Extraction (PyMuPDF)
     │
     ▼
Document Chunking
     │
     ▼
Embeddings (Ollama)
     │
     ▼
FAISS Vector Store
     │
     ▼
Semantic Retrieval
     │
     ▼
Llama 3.2 (RAG)
     │
     ▼
Analysis & Report Generation
```

---

## Tech Stack

**Frontend**

* Streamlit

**Backend**

* Python

**AI**

* Ollama
* Llama 3.2
* nomic-embed-text

**Vector Database**

* FAISS

**PDF Processing**

* PyMuPDF

**Report Generation**

* ReportLab

---

## Project Structure

```text
AI-Powered-MA-Due-Diligence-Assistant/

├── app/
├── data/
├── reports/
├── screenshots/
├── stream_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/AI-Powered-MA-Due-Diligence-Assistant.git
cd AI-Powered-MA-Due-Diligence-Assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install the required Ollama models:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

Run the application:

```bash
streamlit run stream_app.py
```

---

## Sample Questions

* Summarize the document.
* What are the key financial risks?
* Who are the important stakeholders?
* What liabilities are mentioned?
* List important dates.
* Summarize the financial performance.

---

## Future Enhancements

* OCR support for scanned documents
* Multi-document analysis
* Clause extraction
* Source citations with page numbers
* Cloud deployment
* User authentication

---

## Developer

**Ajay Avinash Karthikeyan**

B.Tech – Artificial Intelligence and Machine Learning

Bannari Amman Institute of Technology

---

## License

This project is licensed under the MIT License.
