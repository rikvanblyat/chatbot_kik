import streamlit as st
import os
import json
import re
from PyPDF2 import PdfReader
import docx
import pandas as pd
import difflib
from gpt_module import ask_gpt

st.set_page_config(page_title="Chatbot PTJ", layout="centered")

# ===== Styling CSS =====
st.markdown(
    """
    <style>
    @keyframes blink {
        0% { opacity: 1; }
        50% { opacity: 0; }
        100% { opacity: 1; }
    }
    .stTextInput input::placeholder {
        animation: blink 1s step-start 0s infinite;
        color: #ccc;
    }
    body {
        background-color: #113C25;
        font-family: 'Segoe UI', sans-serif;
        color: #fff;
    }
    .block-container { padding: 2rem; }
    .stApp { background-color: #113C25; color: #fff; }
    .header {
        background-color: #D4AF37;
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
    }
    .footer {
        margin-top: 3rem;
        text-align: center;
        font-size: 0.9rem;
        color: #ccc;
    }
    .stTextInput > div > div > input {
        border: 2px solid #D4AF37;
        border-radius: 8px;
        font-size: 1rem;
        padding: 0.5rem;
        color: #333;
        background-color: #fff;
        caret-color: #50C878;
    }
    .stButton > button {
        background-color: #50C878;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        padding: 0.6rem 1.2rem;
        font-size: 1rem;
    }
    .stButton > button:hover {
        background-color: #45a770;
    }
    .custom-answer {
        background-color: #d4edda;
        color: #333;
        border-left: 6px solid #50C878;
        padding: 1rem;
        border-radius: 8px;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .custom-warning {
        background-color: #fff3cd;
        color: #333 !important;
        border-left: 6px solid #ffecb5;
        padding: 1rem;
        border-radius: 8px;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===== Load Mapping File =====
with open("file_mapping.json", "r", encoding="utf-8") as f:
    file_mapping = json.load(f)

# ===== Load FAQ Data =====
faq_file = "faq.json"
if os.path.exists(faq_file):
    with open(faq_file, "r", encoding="utf-8") as f:
        faq_data = json.load(f)
else:
    faq_data = []

# ===== Search Functions =====
def search_faq(question, faq_data):
    question = question.lower()
    for item in faq_data:
        soalan = item['soalan'].lower()
        if question in soalan or soalan in question or any(word in soalan for word in question.split()):
            return [{
                "Isi": item['jawapan'],
                "Contoh": f"Sebagai contoh, {item['jawapan']}",
                "Dokumen": "FAQ Rasmi Chatbot"
            }]
    return []

def extract_rujukan(text, page_num):
    klausa = re.search(r"Klausa\s*(\d+\.\d+)", text)
    para = re.search(r"(Perenggan|Para)\s*(\d+\.\d+)", text)
    general = re.search(r"(\d+\.\d+)", text)

    if klausa:
        return f"SPANM Bil.5/2023, Klausa {klausa.group(1)}, Muka Surat {page_num}"
    elif para:
        return f"SPANM Bil.5/2023, Para {para.group(2)}, Muka Surat {page_num}"
    elif general:
        return f"SPANM Bil.5/2023, Para {general.group(1)}, Muka Surat {page_num}"
    else:
        return f"SPANM Bil.5/2023, Muka Surat {page_num}"

def fuzzy_match(query, text, threshold=0.55):
    ratio = difflib.SequenceMatcher(None, query.lower(), text.lower()).ratio()
    return ratio >= threshold

def search_pdf(keyword, file_path):
    reader = PdfReader(file_path)
    results = []
    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text and fuzzy_match(keyword, text):
            snippet = text.strip().replace("\n", " ")
            filename = os.path.basename(file_path)
            dokumen_name = file_mapping.get(filename, filename)
            rujukan = extract_rujukan(text, page_num)
            results.append({
                "Isi": f"{snippet}",
                "Contoh": f"Sebagai contoh, {snippet[:80]}...",
                "Dokumen": f"Sila rujuk {rujukan}"
            })
    return results

def search_docx(keyword, file_path):
    doc = docx.Document(file_path)
    results = []
    for para in doc.paragraphs:
        if fuzzy_match(keyword, para.text):
            text = para.text.strip()
            filename = os.path.basename(file_path)
            dokumen = file_mapping.get(filename, filename)
            results.append({
                "Isi": f"{text}",
                "Contoh": f"Sebagai contoh, {text[:80]}...",
                "Dokumen": f"Sila rujuk {dokumen}"
            })
    return results

def search_xlsx(keyword, file_path):
    results = []
    excel = pd.ExcelFile(file_path)
    for sheet in excel.sheet_names:
        df = excel.parse(sheet)
        for row in df.itertuples():
            row_text = " ".join([str(cell) for cell in row[1:] if pd.notnull(cell)])
            if fuzzy_match(keyword, row_text):
                filename = os.path.basename(file_path)
                dokumen = file_mapping.get(filename, filename)
                results.append({
                    "Isi": f"{row_text}",
                    "Contoh": f"Sebagai contoh, {row_text[:80]}...",
                    "Dokumen": f"Sila rujuk {dokumen}"
                })
    return results

def search_all_sources(keyword, faq_data, directory="./dokumen"):
    results = []
    results.extend(search_faq(keyword, faq_data))

    if os.path.exists(directory):
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if file.lower().endswith(".pdf"):
                results.extend(search_pdf(keyword, file_path))
            elif file.lower().endswith(".docx"):
                results.extend(search_docx(keyword, file_path))
            elif file.lower().endswith(".xlsx"):
                results.extend(search_xlsx(keyword, file_path))

    return results

# ===== Streamlit UI =====
st.markdown('<div class="header">Chatbot FAQ & Carian Dokumen PTJ</div>', unsafe_allow_html=True)
st.markdown("### Sila taip soalan atau kata kunci anda di sini:")
user_input = st.text_input("Contoh: Baucar Panjar | Kuasa Pegawai | Definisi Perbelanjaan")

if st.button("Cari"):
    if user_input:
        with st.spinner("Sedang mencari..."):
            results = search_all_sources(user_input, faq_data)
            if results:
                for res in results:
                    st.markdown(f"""
                    <div class=\"custom-answer\">
                    <b>Jawapan:</b><br>{res['Isi']}<br><br>
                    <b>Contoh:</b><br>{res['Contoh']}<br><br>
                    <b>{res['Dokumen']}</b>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                with st.spinner("Menjana jawapan melalui AI..."):
                    gpt_answer = ask_gpt(user_input)
                    st.markdown(f"""
                    <div class=\"custom-answer\">
                    {gpt_answer}
                    </div>
                    """, unsafe_allow_html=True)
    else:
        st.warning("Sila taip soalan atau kata kunci anda dahulu.")

st.markdown('<div class="footer">© 2025 Chatbot KIK - InnoSpark (JANM Pulau Pinang)</div>', unsafe_allow_html=True)
