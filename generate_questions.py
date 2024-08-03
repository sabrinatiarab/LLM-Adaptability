import requests
import json

API_ENDPOINT = "https://saas.cakra.ai/genv2/llms"

def generate_questions(api_key, document_text):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    question_generation_prompt = f"Generate multiple-choice questions from the following text:\n\n{document_text}"

    payload = {
        "model_name": "brain-v2",
        "messages": [
            {"role": "system", "content": "Your Chatbot AI Assistant"},
            {"role": "user", "content": question_generation_prompt}
        ],
        "max_new_tokens": 150,
        "do_sample": False,
        "temperature": 0.7,
        "top_k": 50,
        "top_p": 1.0
    }

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        response_data = response.json()
        generated_text = response_data["choices"][0]["content"]
        questions_and_answers = parse_generated_text(generated_text)
        return questions_and_answers
    else:
        return [{"question": "Error", "options": [], "correct_answer": f"Error: {response.status_code} - {response.text}"}]

def parse_generated_text(generated_text):
    questions_and_answers = []
    qa_pairs = generated_text.split("\n\n")
    for qa in qa_pairs:
        parts = qa.split("\n")
        if len(parts) >= 3:
            question = parts[0].strip()
            options = [part.strip() for part in parts[1:-1]]
            correct_answer = parts[-1].strip()
            questions_and_answers.append({
                "question": question,
                "options": options,
                "correct_answer": correct_answer
            })
    return questions_and_answers