from flask import Flask, request, jsonify
from flask_cors import CORS
from solver.banking_solver import (
    solve_banking_question,
    get_summary,
    generate_question,
    generate_mock_test
)
import pytesseract
from PIL import Image

# 🛠️ Important for Windows (update path if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

app = Flask(__name__)
CORS(app)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image_file = request.files['image']
    image = Image.open(image_file.stream)
    text = pytesseract.image_to_string(image)
    return jsonify({"text": text.strip()})

@app.route('/solve', methods=['POST'])
def solve():
    data = request.get_json()
    chapter = data.get("chapter")
    question = data.get("question")

    if chapter.lower() != "banking":
        return jsonify({
            "answer": f"The question you asked is from '{chapter}' which is outside the scope of the Banking chapter in ICSE 10th Math."
        })

    answer = solve_banking_question(question)
    return jsonify({"answer": answer})

@app.route('/summary', methods=['GET'])
def summary():
    return jsonify({"summary": get_summary()})

@app.route('/generate-question', methods=['GET'])
def generate():
    return jsonify({"question": generate_question()})

@app.route('/mock-test', methods=['GET'])
def mock_test():
    return jsonify(generate_mock_test())

if __name__ == '__main__':
    app.run(debug=True)
