import streamlit as st
from backend.document_loader import process_uploaded_file
from backend.vector_store import VectorStore

st.set_page_config(page_title="Document Extractor & Search", layout="wide")
st.title("📄 Document Upload, Extract, and Semantic Search")

uploaded_docs = {}
vector_store = VectorStore()

uploaded_files = st.file_uploader("📁 Upload your documents here", 
                                  type=["pdf", "png", "jpg", "jpeg"], 
                                  accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_name, extracted_text = process_uploaded_file(file)
        uploaded_docs[file_name] = extracted_text
        st.markdown(f"**{file_name}**")
        with st.expander("Show Extracted Text"):
            st.text(extracted_text[:3000] + ("..." if len(extracted_text) > 3000 else ""))

if uploaded_docs:
    if st.button("Build Search Index"):
        st.write("Building index... This may take a moment.")
        vector_store.build_index(list(uploaded_docs.values()), list(uploaded_docs.keys()))
        st.success("Index built successfully!")

if vector_store.index:
    query = st.text_input("Enter your query to search the documents:")
    if query:
        results = vector_store.search(query, top_k=5)
        st.write(f"Top {len(results)} relevant chunks:")
        for i, res in enumerate(results, 1):
            st.markdown(f"**Result {i} from {res['source_doc']}:**")
            st.write(res["chunk"])
            st.markdown("---")
