import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Remplace par ton propre token Hugging Face
API_TOKEN = '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'
API_URL = "https://api-inference.huggingface.co/models/CHARLESL16/gpt2-student-question-answer-memorization"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query_huggingface(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    try:
        response.raise_for_status()  # Gérer les erreurs HTTP
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except Exception as err:
        return {"error": f"An error occurred: {err}"}

@app.route('/ask', methods=['POST'])
def ask_model():
    data = request.json
    question = data.get('question')

    if not question:
        return jsonify({'error': 'No question provided'}), 400

    payload = {
        "inputs": question
    }

    result = query_huggingface(payload)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
