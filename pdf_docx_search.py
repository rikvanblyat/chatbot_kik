# pdf_docx_search.py
import os
import re
import streamlit as st
from PyPDF2 import PdfReader
import docx

# Fungsi untuk ekstrak teks dari PDF
def extract_text_from_pdf(pdf_file):
    pdf = PdfReader(pdf_file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text() + "\n"
    return text

# Fungsi untuk ekstrak teks dari DOCX
def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

# Fungsi untuk cari keyword dalam teks
def search_keywords(text, keyword):
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    matches = pattern.finditer(text)
    results = []
    for match in matches:
        start = max(match.start() - 100, 0)
        end = min(match.end() + 100, len(text))
        snippet = text[start:end]
        results.append(snippet.strip())
    return results

# Fungsi utama untuk Streamlit
def pdf_docx_search_interface():
    st.subheader("🔍 Cari dalam Dokumen Pekeliling (PDF/DOCX)")
    uploaded_file = st.file_uploader("Muat Naik Dokumen (PDF/DOCX)", type=["pdf", "docx"])

    if uploaded_file:
        with st.spinner("Memproses fail..."):
            if uploaded_file.name.endswith(".pdf"):
                text = extract_text_from_pdf(uploaded_file)
            elif uploaded_file.name.endswith(".docx"):
                text = extract_text_from_docx(uploaded_file)
            else:
                st.warning("Format fail tidak disokong.")
                return

            st.success("Dokumen berjaya diproses!")

            keyword = st.text_input("Masukkan kata kunci atau soalan untuk dicari...", placeholder="Contoh: Baucar Panjar", key="pdf_docx_search")
            if keyword:
                results = search_keywords(text, keyword)
                if results:
                    st.markdown("**Hasil Carian:**")
                    for i, res in enumerate(results, 1):
                        st.markdown(f"**{i}.** ...{res}...")
                else:
                    st.warning("Tiada hasil ditemui.")

