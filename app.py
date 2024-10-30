from flask import Flask, render_template, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from flask_cors import CORS

# Initialisation du modèle et du tokenizer
model = GPT2LMHeadModel.from_pretrained("CHARLESL16/gpt2-student-question-answer-memorization-v3")
tokenizer = GPT2Tokenizer.from_pretrained("CHARLESL16/gpt2-student-question-answer-memorization-v3")

app = Flask(__name__)

# Autoriser CORS pour toutes les origines
CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')
# Route pour les requêtes POST
@app.route('/answer', methods=['POST'])
def get_answer():
    data = request.get_json()

    if 'question' not in data:
        return jsonify({'error': 'Veuillez fournir une question'}), 400

    question = data['question']
    
    # Prétraiter la question
    inputs = tokenizer(question, return_tensors="pt")

    # Générer une réponse à partir du modèle
    outputs = model.generate(**inputs, max_length=100, num_return_sequences=1)

    # Décoder la réponse
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Retourner la réponse sous forme de JSON
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
