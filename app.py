from flask import Flask, request, jsonify
import os
import fitz  # PyMuPDF
from generate_questions import generate_questions

app = Flask(__name__)

def load_document(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        api_key = request.form['api_key']
        
        if file and api_key:
            file_path = os.path.join("uploads", file.filename)
            file.save(file_path)
            
            document_text = load_document(file_path)
            questions = generate_questions(api_key, document_text)
            
            return jsonify(questions)
    else:
        return '''
        <h1>Upload Document and Generate Questions</h1>
        <form method="POST" enctype="multipart/form-data">
            <label for="file">Choose PDF file:</label>
            <input type="file" name="file" id="file" required>
            <br>
            <label for="api_key">Enter API Key:</label>
            <input type="text" name="api_key" id="api_key" required>
            <br>
            <button type="submit">Generate Questions</button>
        </form>
        '''

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)