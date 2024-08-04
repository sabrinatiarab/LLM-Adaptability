import fitz  # PyMuPDF

def load_document(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

import requests
import json

def generate_questions(api_key, document_text, question, num_questions=5):
    url = "https://saas.cakra.ai/genv2/llms"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model_name": "brain-v2",
        "messages": [
            {
                "role": "system",
                "content": "Anda merupakan guru bahasa Indonesia"
            },
            {
                "role": "user",
                "content": f"Rangkum teks yang diberikan dalam bahasa Indonesia '{document_text}'"
            }
        ],
        "max_new_tokens": 500,
        "do_sample": False,
        "temperature": 0.7,
        "top_k": 50,
        "top_p": 1.0
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response = response.json()

    data = {
        "model_name": "brain-v2",
        "messages": [
            {
                "role": "system",
                "content": response.get("choices", [])[0].get("content", "")
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "max_new_tokens": 500,
        "do_sample": False,
        "temperature": 0.7,
        "top_k": 50,
        "top_p": 1.0
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

# api_key = "4a3b78a8-bb82-4379-8171-742d98f760c4"
# response = generate_questions(api_key, document_text)
# print(response)

def parse_questions(response):
    questions = response.get("choices", [])
    parsed_questions = []
    for question in questions:
        content = question.get("content", "")
        parsed_questions.append(content)
    return parsed_questions

import streamlit as st

st.title("Generator Pertanyaan Pilihan Ganda")
uploaded_file = st.file_uploader("Upload Buku (PDF)", type="pdf")

api_key = st.text_input("Masukkan API Key", type="password")

question = st.text_input(
    "Ask something about the article",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file,
)

if api_key and question and uploaded_file is not None:
    document_text = load_document(uploaded_file)
    st.write("Buku berhasil diupload dan diproses.")
 
    if st.button("Generate"):
        if api_key:
            response = generate_questions(api_key, document_text, question)
            parsed_questions = parse_questions(response)
            for i, question in enumerate(parsed_questions, 1):
                st.write(f"**Pertanyaan {i}:**\n{question}\n")
        else:
            st.error("Masukkan API Key terlebih dahulu.")