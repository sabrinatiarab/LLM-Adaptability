import requests
import json

def generate_questions(api_key, document_text, num_questions=5):
    url = "https://saas.cakra.ai/genv2/llms"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    instructions = (
        f"Berdasarkan teks berikut, buatlah {num_questions} pertanyaan pilihan ganda dalam bahasa Indonesia. "
        "Setiap pertanyaan harus memiliki 4 pilihan jawaban (A, B, C, D) dan menunjukkan pilihan jawaban yang benar. "
        "Teks: "
    )
    data = {
        "model_name": "brain-v2",
        "messages": [
            {
                "role": "system",
                "content": "Anda adalah asisten AI yang dapat membantu membuat pertanyaan pilihan ganda."
            },
            {
                "role": "user",
                "content": instructions + document_text
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

def parse_questions(response):
    questions = response.get("choices", [])
    parsed_questions = []
    for question in questions:
        content = question.get("content", "")
        parsed_questions.append(content)
    return parsed_questions