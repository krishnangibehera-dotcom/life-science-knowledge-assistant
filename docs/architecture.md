# Architecture and Design Notes

## Goal
Create a document-grounded question-answering assistant for life-science learning material using retrieval-augmented generation (RAG).

## Data flow
1. **Input:** User uploads PDF or TXT documents.
2. **Extraction:** `pypdf` extracts selectable text from PDFs; TXT files are decoded as UTF-8.
3. **Chunking:** Text is split into overlapping character windows so retrieval can return manageable passages.
4. **Embedding:** `sentence-transformers/all-MiniLM-L6-v2` maps chunks and questions to vectors.
5. **Indexing:** FAISS stores and searches the vectors.
6. **Retrieval:** The four most relevant passages are retrieved for a question.
7. **Generation:** A local Ollama chat model receives the question and retrieved context.
8. **Presentation:** Streamlit displays the answer and the retrieved evidence passages.

## Main components
- `app.py`: UI, document processing, retrieval, and generation
- `requirements.txt`: Python dependencies
- `data/sample_documents/`: original demonstration documents
- `data/evaluation_questions.csv`: manually answerable evaluation prompts
- `docs/`: architecture and resume guidance

## Known engineering trade-offs
- The starter uses a simple character-based splitter. A token-aware or structure-aware splitter may preserve scientific sections better.
- It rebuilds the vector store for each indexing action and does not persist the index.
- Retrieved passages are displayed, but generated source citations are not independently verified.
- Model outputs need human review; RAG reduces but does not eliminate hallucinations.
