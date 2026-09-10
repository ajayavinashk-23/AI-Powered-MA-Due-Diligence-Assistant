import streamlit as st

from app.pdf_service import save_uploaded_files, extract_document
from app.chunk_service import create_chunks
from app.embedding_service import EmbeddingService
from app.vector_service import VectorStore
from app.analyzer import DocumentAnalyzer
from app.rag_service import RAGService
from app.report_service import ReportService

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI-Powered M&A Due Diligence Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI-Powered M&A Due Diligence Assistant")

st.caption(
"Offline RAG-based Document Analysis System"
)
st.sidebar.title("AI Due Diligence")

st.sidebar.info(
"""
Offline RAG Assistant

Built using:

• Streamlit

• Ollama

• FAISS

• PyMuPDF

• Custom Chunking
"""
)
st.write("Upload one or more PDF documents and analyze them using AI.")

# --------------------------------------------------
# Upload Section
# --------------------------------------------------

uploaded_files = st.file_uploader(
    "Upload PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    paths = save_uploaded_files(uploaded_files)

    st.success(f"✅ Successfully uploaded {len(paths)} document(s).")

    embedding_service = EmbeddingService()
    vector_db = VectorStore(embedding_service)

    for path in paths:

        document = extract_document(path)

        chunks = create_chunks(document)

        vector_db.add_chunks(chunks)

    vector_db.save()

    st.success("✅ Documents indexed successfully.")
    st.divider()

    st.header("📊 Document Dashboard")

    total_pages = 0
    total_words = 0
    total_characters = 0
    total_chunks = 0

    documents = []

    for path in paths:

        document = extract_document(path)

        chunks = create_chunks(document)

        documents.append(document["filename"])

        total_pages += document["pages"]
        total_words += document["words"]
        total_characters += document["characters"]
        total_chunks += len(chunks)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Pages", total_pages)
    c2.metric("Words", total_words)
    c3.metric("Characters", total_characters)
    c4.metric("Chunks", total_chunks)

    st.write("### Uploaded Documents")

    for doc in documents:
        st.write("✔", doc)

        # ---------------------------------------------
        # Tabs
        # ---------------------------------------------
    dashboard = {

        "pages": total_pages,

        "words": total_words,

        "characters": total_characters,

        "chunks": total_chunks

    }

    st.session_state["dashboard"] = dashboard

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📄 Document",
            "📊 AI Analysis",
            "💬 AI Assistant",
            "📑 Report"
        ]
    )

    # ==========================================================
    # TAB 1
    # ==========================================================

    with tab1:

        st.header("Document Information")

        for path in paths:

            document = extract_document(path)

            chunks = create_chunks(document)

            st.subheader(document["filename"])

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Pages", document["pages"])
            col2.metric("Words", document["words"])
            col3.metric("Characters", document["characters"])
            col4.metric("Chunks", len(chunks))

            with st.expander("📄 Document Preview", expanded=False):

                st.text_area(
                    label="",
                    value=document["text"][:4000],
                    height=350,
                    disabled=True
                )

            st.divider()

    # ==========================================================
    # TAB 2
    # ==========================================================

    with tab2:

        st.header("📊 AI Due Diligence Analysis")

        st.info(
            "Generate an automatic due diligence summary of the uploaded documents."
        )

        if st.button("Generate Analysis", use_container_width=True):

            analyzer = DocumentAnalyzer()

            with st.spinner("📊 Generating Due Diligence Analysis..."):

                report = analyzer.analyze()
                st.session_state["analysis"] = report

            st.success("Analysis Complete")

            st.subheader("Executive Summary")
            st.info(report["Executive Summary"])

            st.subheader("Financial Highlights")
            st.success(report["Financial Highlights"])

            st.subheader("Risk Analysis")
            st.warning(report["Risk Analysis"])

            st.subheader("Important Parties")
            st.info(report["Important Parties"])

            st.subheader("Important Dates")
            st.info(report["Important Dates"])

    # ==========================================================
    # TAB 3
    # ==========================================================

    with tab3:

        st.header("💬 AI Due Diligence Assistant")

        question = st.text_input(
            "Ask a question...",
            placeholder="Example: What are the financial risks?"
        )

        if st.button("Ask AI", use_container_width=True):

            if question.strip() == "":

                st.warning("Please enter a question.")

            else:

                rag = RAGService()

                with st.spinner("🤖 AI is analyzing the document..."):

                    result = rag.ask(question)

                with st.chat_message("assistant"):

                    st.markdown(result["answer"])

                st.subheader("Retrieved Sources")

                for i, chunk in enumerate(result["sources"]):

                    with st.expander(
                        f"Source {i+1} (Score: {round(chunk['score'],4)})"
                    ):

                        st.caption(f"Similarity Score : {chunk['score']:.3f}")

                        st.markdown("---")

                        st.write(chunk["text"])
    with tab4:

        st.header("📑 Due Diligence Report")

        st.info(
            "Generate a professional Due Diligence Report."
        )

        if st.button(
            "Generate Report",
            use_container_width=True
        ):

            if "analysis" not in st.session_state:

                st.warning(
                    "Please generate AI Analysis first."
                )

            else:

                service = ReportService()

                markdown = service.generate_report(

                    st.session_state["dashboard"],

                    st.session_state["analysis"]

                )

                md_path = service.save_markdown(markdown)

                pdf_path = service.save_pdf(

                    st.session_state["dashboard"],

                    st.session_state["analysis"]

                )

                st.success(
                    "Report Generated Successfully!"
                )

                with open(
                    pdf_path,
                    "rb"
                ) as pdf:

                    st.download_button(

                        label="📄 Download PDF Report",

                        data=pdf,

                        file_name="Due_Diligence_Report.pdf",

                        mime="application/pdf",

                        use_container_width=True

                    )

                with open(
                    md_path,
                    "r",
                    encoding="utf-8"
                ) as md:

                    st.download_button(

                        label="📝 Download Markdown Report",

                        data=md.read(),

                        file_name="Due_Diligence_Report.md",

                        mime="text/markdown",

                        use_container_width=True

                    )

st.divider()

st.caption(
"""
AI-Powered M&A Due Diligence Assistant

Built using

• Streamlit
• Ollama
• FAISS
• PyMuPDF

Developed by Ajay Avinash Karthikeyan
"""
)