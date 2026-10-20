# Life Science Knowledge Assistant (RAG)

A Streamlit application concept that lets users upload life-science PDFs/TXT files, retrieve relevant passages with semantic search, and generate context-grounded answers using a locally running Ollama language model.

> **Project status:** Starter implementation. It has not been executed or tested in this environment. Test the setup and answer quality before presenting it as a completed working application.

## Features
- Upload multiple PDF/TXT study documents
- Extract text and split it into overlapping chunks
- Create embeddings with `sentence-transformers/all-MiniLM-L6-v2`
- Search semantically using FAISS
- Generate answers using a local Ollama model through LangChain
- Show retrieved passages and source filenames
- Prompt the model to acknowledge when uploaded documents do not contain the answer

## Architecture
`PDF/TXT upload → text extraction → chunking → embeddings → FAISS retrieval → Ollama LLM → answer + retrieved evidence`

See [`docs/architecture.md`](docs/architecture.md).

## Requirements
- Python 3.10 or 3.11 recommended
- Ollama installed and running
- Enough RAM and disk space for the chosen local model
- Internet access on first run to download Python packages and the embedding model

## Setup (Windows PowerShell)
1. Install Ollama from https://ollama.com/download.
2. Open PowerShell and download a model, for example:

   ```powershell
   ollama pull llama3.2
   ```

3. Open this project folder in VS Code and create a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   ```

4. Run the app:

   ```powershell
   streamlit run app.py
   ```

5. Open the local URL Streamlit prints in the terminal. Upload documents, click **Build document search index**, then ask a question.

If PowerShell blocks activation, use `.\.venv\Scripts\python.exe -m pip install -r requirements.txt` and `.\.venv\Scripts\python.exe -m streamlit run app.py`.

## Included sample data
`data/sample_documents/` contains original, compact educational notes written for this starter repository. They are demonstration documents, not a comprehensive or authoritative biology reference.

`data/evaluation_questions.csv` contains example questions for manually checking retrieval and answer quality.

## Limitations and responsible use
- This is an educational prototype, not a validated medical or clinical decision system.
- Outputs can be incorrect. Verify important claims against primary literature or textbooks.
- Scanned PDFs may need OCR; this version extracts selectable text only.
- FAISS index is rebuilt in memory when you click the index button; persistence and user/session isolation are not implemented.
- Source references are filenames and chunk numbers, not reliable PDF page-level citations yet.
- Local model quality and speed depend on hardware.
- Review licenses and permissions before redistributing third-party documents or datasets.

## Suggested next improvements
1. Add PDF page-number metadata and precise citations.
2. Persist and reload FAISS indexes.
3. Add a retrieval evaluation script and answer-quality rubric.
4. Add tests for empty PDFs, duplicate files, and unsupported formats.
5. Add a chat history and document removal controls.
6. Record measured latency and evaluation results only after testing.

## Resume guidance
Only describe features you have personally implemented and tested. See [`docs/resume_bullets.md`](docs/resume_bullets.md) for truthful draft wording.
