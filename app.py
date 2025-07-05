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

pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"  # may need updating later

app = Flask(__name__)
CORS(app)

# ... all your routes ...

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
