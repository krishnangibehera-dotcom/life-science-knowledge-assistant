# Life Science Knowledge Assistant (RAG)

A Python-based Retrieval-Augmented Generation (RAG) project concept for searching life-science learning materials and generating context-grounded answers using a locally hosted language model.

## Project Overview

Life-science students often need to search across multiple study documents to find relevant information quickly. This project explores a document-question-answering workflow that combines semantic search with a local large language model (LLM).

Users can upload supported study documents, retrieve relevant text passages, and use the retrieved context to formulate answers.

**Project status:** Starter implementation; execution and answer quality have not yet been verified.

## Key Features

- PDF and TXT document ingestion workflow
- Text extraction and overlapping text chunking
- Semantic embeddings using Sentence Transformers
- Similarity search using FAISS
- Local LLM integration through Ollama
- Streamlit-based user interface
- Display of retrieved evidence and source filenames
- Sample evaluation questions for manual assessment

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Interactive web interface |
| Sentence Transformers | Text embeddings |
| FAISS | Similarity-based retrieval |
| Ollama | Local language-model serving |
| LangChain | LLM integration |
| Pandas | Evaluation data handling |

## Project Architecture

Document Upload → Text Extraction → Text Chunking → Embedding Generation → FAISS Retrieval → Local LLM → Context-Grounded Answer

The retrieval component is designed to find relevant passages before the language model generates an answer.

## Repository Structure

```text
life-science-knowledge-assistant/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   ├── evaluation_questions.csv
│   └── sample_documents/
│       ├── central_dogma.txt
│       ├── ecology_basics.txt
│       ├── immune_system_basics.txt
│       └── pcr_basics.txt
└── docs/
    ├── architecture.md
    ├── evaluation_plan.md
    └── resume_bullets.md
```

## Sample Data

The repository contains original educational notes covering:

- Central dogma of molecular biology
- Basic ecology concepts
- Immune system fundamentals
- PCR principles

The evaluation CSV contains example questions for manually assessing document retrieval and answer relevance.

These files are demonstration materials, not a comprehensive scientific reference or a validated benchmark dataset.

## Setup and Usage

### Prerequisites

- Python 3.10 or 3.11 recommended
- Ollama installed
- Sufficient memory and disk space for the selected local model
- Internet access for initial dependency and model downloads

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/krishnangibehera-dotcom/life-science-knowledge-assistant.git
   cd life-science-knowledge-assistant
   ```

2. Create and activate a virtual environment on Windows:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Install Ollama from https://ollama.com/download.

5. Download the example model:

   ```powershell
   ollama pull llama3.2
   ```

6. Launch the application:

   ```powershell
   streamlit run app.py
   ```

7. Open the local URL displayed in the terminal, upload supported documents, build the document search index, and ask a question.

**Note:** These are the intended setup instructions. Successful installation and execution have not yet been confirmed.

## Evaluation Plan

The included evaluation questions can be used to assess:

- Whether relevant passages are retrieved
- Whether answers are supported by retrieved evidence
- Whether the system acknowledges missing information
- Whether irrelevant documents affect the response
- Response latency and resource requirements

No quantitative performance results are reported because formal testing has not yet been completed.

## Limitations

- The application has not yet been fully tested.
- Scanned PDFs may require OCR support.
- Retrieval quality depends on document content, chunking, and embedding quality.
- Local LLM performance depends on hardware and model selection.
- Answers may be inaccurate and should be checked against reliable textbooks and primary literature.
- This is an educational prototype, not a medical or clinical decision-support system.

## Future Improvements

- Add automated retrieval and answer-quality evaluation
- Improve source citations with document page numbers
- Persist and reload the vector index
- Add document management and chat history
- Add automated tests and error handling
- Benchmark latency and retrieval quality on a documented test set

## Disclaimer

This project is intended for educational and learning purposes only. It is not a substitute for scientific verification, professional advice, or clinical decision-making.
