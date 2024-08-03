from flask import Flask, request, render_template
import os
import fitz  # PyMuPDF
from generate_questions import generate_questions, parse_questions

app = Flask(__name__)

def load_document(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

@app.route('/', methods=['GET', 'POST'])
def index():
    questions = []
    if request.method == 'POST':
        file = request.files['file']
        api_key = request.form['api_key']
        
        if file and api_key:
            file_path = os.path.join("uploads", file.filename)
            file.save(file_path)
            
            document_text = load_document(file_path)
            response = generate_questions(api_key, document_text)
            questions = parse_questions(response)
            
    return render_template('index.html', questions=questions)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)