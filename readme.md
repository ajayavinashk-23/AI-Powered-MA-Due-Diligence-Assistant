# AI-Powered M&A Due Diligence Assistant

An offline AI-powered M&A Due Diligence Assistant that uses Retrieval-Augmented Generation (RAG) to analyze business documents, answer questions, identify key risks, and generate structured due diligence reports.

The system runs locally using Ollama, FAISS, and Llama 3.2, allowing sensitive business documents to be processed without relying on external cloud AI APIs.

## Overview

M&A due diligence requires reviewing large amounts of financial, legal, and business documentation. This project provides a local AI-assisted workflow for extracting information from PDF documents and retrieving relevant information using semantic search.

Users can upload a document, ask questions about its contents, perform automated due diligence analysis, and export the results as PDF or Markdown reports.

## Key Features

* PDF document upload and analysis
* Text extraction using PyMuPDF
* Intelligent document chunking
* Local text embeddings using `nomic-embed-text`
* Semantic search using FAISS
* Retrieval-Augmented Generation (RAG)
* Question answering using Llama 3.2
* Automated due diligence analysis
* Financial and risk-oriented document analysis
* PDF and Markdown report generation
* Fully local and offline AI pipeline

## System Architecture

```text
                    PDF Document
                         |
                         v
                 Text Extraction
                    PyMuPDF
                         |
                         v
                  Text Chunking
                         |
                         v
               Text Embeddings
              Ollama / nomic-embed-text
                         |
                         v
                  FAISS Index
                         |
                         v
                 Semantic Retrieval
                         |
                         v
                  Relevant Chunks
                         |
                         v
                  RAG Prompt
                         |
                         v
                   Llama 3.2
                         |
                         v
              Analysis / Q&A Output
                         |
                         v
               Report Generation
                  PDF / Markdown
```

## How It Works

### 1. Document Processing

The uploaded PDF is processed using PyMuPDF and converted into text.

### 2. Document Chunking

The extracted text is divided into smaller chunks so that relevant sections can be efficiently retrieved.

### 3. Embedding Generation

Each chunk is converted into a numerical vector using the local `nomic-embed-text` embedding model through Ollama.

### 4. Vector Search

The embeddings are stored in a FAISS vector index. When the user asks a question, the question is embedded and the most relevant document chunks are retrieved.

### 5. RAG-based Answer Generation

The retrieved chunks are provided as context to Llama 3.2. The model generates an answer based only on the retrieved document information.

### 6. Due Diligence Analysis

The application can generate structured analysis covering areas such as:

* Executive Summary
* Financial Highlights
* Risk Analysis
* Important Parties
* Important Dates

### 7. Report Generation

The generated analysis can be exported as Markdown and PDF reports.

## Tech Stack

| Component            | Technology                     |
| -------------------- | ------------------------------ |
| Frontend             | Streamlit                      |
| Programming Language | Python                         |
| LLM                  | Llama 3.2                      |
| Embedding Model      | nomic-embed-text               |
| Local AI Runtime     | Ollama                         |
| Vector Database      | FAISS                          |
| PDF Processing       | PyMuPDF                        |
| Report Generation    | ReportLab                      |
| Architecture         | Retrieval-Augmented Generation |

## Project Structure

```text
AI-Powered-MA-Due-Diligence-Assistant/
│
├── app/
│   ├── analyzer.py
│   ├── chunk_service.py
│   ├── config.py
│   ├── embedding_service.py
│   ├── models.py
│   ├── pdf_service.py
│   ├── rag_service.py
│   ├── report_service.py
│   ├── retriever.py
│   ├── utils.py
│   └── vector_service.py
│
├── data/
│   ├── uploads/
│   ├── processed/
│   ├── chunks/
│   └── vector_db/
│
├── reports/
├── stream_app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── readme.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ajayavinashk-23/AI-Powered-MA-Due-Diligence-Assistant.git
cd AI-Powered-MA-Due-Diligence-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows PowerShell**

```powershell
venv\Scripts\Activate.ps1
```

**Windows Command Prompt**

```cmd
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Ollama

Install Ollama and make sure the Ollama service is running.

Pull the required models:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

### 6. Run the application

```bash
streamlit run stream_app.py
```

The application will open in your browser.

## Example Questions

The assistant can answer questions such as:

* Summarize the document.
* What are the key financial risks?
* What liabilities are mentioned?
* Who are the important stakeholders?
* What are the important dates?
* Summarize the financial performance.

## Privacy

The AI processing pipeline is designed to run locally.

Documents are processed using local PDF extraction, embeddings, FAISS retrieval, and the locally hosted Llama 3.2 model through Ollama.

No external OpenAI API is required.

## Current Limitations

* Primarily designed for text-based PDF documents
* OCR for scanned documents is not currently implemented
* Source citations with page numbers are not currently implemented
* Multi-document analysis is not currently implemented

## Future Enhancements

* OCR support for scanned documents
* Multi-document due diligence analysis
* Page-level source citations
* Advanced financial metric extraction
* Clause-level legal analysis
* Document comparison
* User authentication
* Cloud deployment

## Developer

**Ajay Avinash Karthikeyan**

B.Tech – Artificial Intelligence and Machine Learning
Bannari Amman Institute of Technology

## License

This project is licensed under the MIT License.
