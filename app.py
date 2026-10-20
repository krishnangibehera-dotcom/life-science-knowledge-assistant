import os
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Life Science Knowledge Assistant", page_icon="🧬", layout="wide")
st.title("🧬 Life Science Knowledge Assistant")
st.write("Ask questions about your biology PDFs and text documents. Answers are generated from retrieved document passages.")

DATA_DIR = Path("data")
SUPPORTED = {".pdf", ".txt"}

@st.cache_resource
def load_embedding_model():
    from langchain_huggingface import HuggingFaceEmbeddings
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def read_uploaded_file(uploaded):
    suffix = Path(uploaded.name).suffix.lower()
    if suffix == ".txt":
        return uploaded.getvalue().decode("utf-8", errors="ignore")
    if suffix == ".pdf":
        from pypdf import PdfReader
        import io
        reader = PdfReader(io.BytesIO(uploaded.getvalue()))
        return "\n".join((page.extract_text() or "") for page in reader.pages)
    return ""

def split_text(text, chunk_size=900, overlap=150):
    text = " ".join(text.split())
    if not text:
        return []
    chunks, start = [], 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        if end == len(text):
            break
        start = max(0, end - overlap)
    return chunks

def build_retriever(uploaded_files):
    from langchain_core.documents import Document
    from langchain_community.vectorstores import FAISS
    all_docs = []
    for uploaded in uploaded_files:
        text = read_uploaded_file(uploaded)
        for idx, chunk in enumerate(split_text(text)):
            all_docs.append(Document(
                page_content=chunk,
                metadata={"source": uploaded.name, "chunk": idx + 1}
            ))
    if not all_docs:
        return None
    embeddings = load_embedding_model()
    vectorstore = FAISS.from_documents(all_docs, embeddings)
    return vectorstore.as_retriever(search_kwargs={"k": 4})

def answer_question(question, retriever, model_name):
    from langchain_ollama import ChatOllama
    from langchain_core.prompts import ChatPromptTemplate
    docs = retriever.invoke(question)
    if not docs:
        return "I could not find relevant information in the uploaded documents.", []
    context = "\n\n".join(
        f"[Source: {d.metadata.get('source', 'unknown')}, chunk {d.metadata.get('chunk', '?')}]\n{d.page_content}"
        for d in docs
    )
    prompt = ChatPromptTemplate.from_template(
        """You are a careful life-sciences study assistant.
Answer using ONLY the supplied context. If the context does not contain enough evidence,
say so clearly instead of inventing an answer. Explain technical terms simply.
Do not give personal medical diagnosis or treatment advice.

Context:
{context}

Question: {question}

Answer with a concise explanation and a Sources section naming the documents used."""
    )
    llm = ChatOllama(model=model_name, temperature=0)
    response = (prompt | llm).invoke({"context": context, "question": question})
    return response.content, docs

with st.sidebar:
    st.header("Settings")
    model_name = st.text_input("Ollama model name", value="llama3.2")
    st.caption("The model must already be installed locally with Ollama.")
    st.markdown("[Ollama installation guide](https://ollama.com/download)")

uploaded_files = st.file_uploader(
    "Upload life-science documents (PDF or TXT)",
    type=["pdf", "txt"],
    accept_multiple_files=True,
    help="Use course notes, review papers you have permission to use, or your own study materials."
)

if uploaded_files:
    st.success(f"{len(uploaded_files)} document(s) selected.")
    if st.button("Build document search index", type="primary"):
        with st.spinner("Extracting text and building the semantic search index..."):
            try:
                st.session_state["retriever"] = build_retriever(uploaded_files)
                st.session_state["indexed_names"] = [f.name for f in uploaded_files]
                if st.session_state["retriever"]:
                    st.success("Index built. Ask a question below.")
                else:
                    st.warning("No extractable text was found. Try a text-based PDF or TXT file.")
            except Exception as e:
                st.error(f"Could not build index: {e}")
                st.info("Check that dependencies are installed and the embedding model can be downloaded.")
else:
    st.info("Upload one or more documents to begin.")

question = st.text_input("Ask a question", placeholder="e.g., What are the main steps of PCR?")
if st.button("Submit question"):
    if not question.strip():
        st.warning("Enter a question first.")
    elif "retriever" not in st.session_state:
        st.warning("Upload documents and build the index first.")
    else:
        with st.spinner("Searching documents and generating an answer with Ollama..."):
            try:
                answer, sources = answer_question(question, st.session_state["retriever"], model_name)
                st.subheader("Answer")
                st.write(answer)
                with st.expander("Retrieved passages"):
                    for i, doc in enumerate(sources, 1):
                        st.markdown(f"**{i}. {doc.metadata.get('source', 'unknown')} — chunk {doc.metadata.get('chunk', '?')}**")
                        st.write(doc.page_content)
            except Exception as e:
                st.error(f"Answer generation failed: {e}")
                st.info("Make sure Ollama is running and the selected model has been downloaded.")
