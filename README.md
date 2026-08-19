# Document Q&A

A small beginner-friendly Generative AI application that lets a user upload a `.txt` document and ask questions about its content.

## What it demonstrates

- Python application development
- Reading and handling text data
- REST API communication
- JSON request/response handling
- LLM prompting
- Basic document question answering
- Streamlit UI
- Environment-variable based API key handling

## How it works

```text
Text document
     ↓
Streamlit upload
     ↓
Python reads document
     ↓
Document context + question
     ↓
LLM API
     ↓
Answer displayed in the UI
```

This is intentionally a small first version. It does not claim to be a full production RAG system.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Abuzrskf/document-qa.git
cd document-qa
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Copy `.env.example` to `.env` and add your own API key.

**Never commit `.env` to GitHub.**

### 5. Run

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

## Example

Upload the included `sample/sample_notes.txt` and ask:

> What are the main topics covered in the document?

## Limitations

The first version sends a bounded section of the uploaded text as context. Very large documents are not supported yet.

## Future improvements

- Better text chunking
- Keyword-based or embedding-based retrieval
- PDF support
- Source/context display
- Conversation history
- More robust error handling

## Tech Stack

Python • Streamlit • REST API • JSON • LLM API
