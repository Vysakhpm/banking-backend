import os
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

# Optional: You may set the tesseract path manually if needed on Render
# pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def index():
    return "✅ Banking AI Backend is Live!"

@app.route("/solve", methods=["POST"])
def solve():
    data = request.get_json()
    chapter = data.get("chapter")
    question = data.get("question")

    if chapter.lower() != "banking":
        return jsonify({"answer": "❌ Sorry, only Banking chapter questions are supported."})

    answer = solve_banking_question(question)
    return jsonify({"answer": answer})

@app.route("/summary", methods=["GET"])
def summary():
    return jsonify({"summary": get_summary()})

@app.route("/generate-question", methods=["GET"])
def generate():
    return jsonify({"question": generate_question()})

@app.route("/mock-test", methods=["GET"])
def mock():
    return jsonify(generate_mock_test())

@app.route("/ocr", methods=["POST"])
def ocr():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    image = request.files["image"]
    img = Image.open(image.stream)
    text = pytesseract.image_to_string(img)
    return jsonify({"text": text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
