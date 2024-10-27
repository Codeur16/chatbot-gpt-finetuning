from flask import Flask, render_template, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from flask_cors import CORS

# Initialisation du modèle et du tokenizer
model = GPT2LMHeadModel.from_pretrained("CHARLESL16/gpt2-student-question-answer-memorization")
tokenizer = GPT2Tokenizer.from_pretrained("CHARLESL16/gpt2-student-question-answer-memorization")

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







# from transformers import GPT2LMHeadModel, GPT2Tokenizer

# model = GPT2LMHeadModel.from_pretrained("CHARLESL16/gpt2-student-question-answer-memorization")  # Replace with your Hugging Face repo ID
# tokenizer = GPT2Tokenizer.from_pretrained("CHARLESL16/gpt2-student-question-answer-memorization")

# #Generate Responses and Test Performance

# input_text = "Quel est le matricule de l'étudiant ayant le nom NOA NGONO NOA Yannick"
# inputs = tokenizer(input_text, return_tensors="pt")

# # Generate a response from the model
# outputs = model.generate(**inputs, max_length=100, num_return_sequences=1)

# # Decode the response
# response = tokenizer.decode(outputs[0], skip_special_tokens=True)
# print(response)




# from flask import Flask, render_template, request, jsonify
# from transformers import GPT2LMHeadModel, GPT2Tokenizer
# import torch

# # Initialisation du modèle et du tokenizer
# model = GPT2LMHeadModel.from_pretrained("CHARLESL16/gpt2-student-question-answer-memorization")
# tokenizer = GPT2Tokenizer.from_pretrained("CHARLESL16/gpt2-student-question-answer-memorization")

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def hello_world():
#     return render_template('index.html')
# # Route pour les requêtes POST
# @app.route('/answer', methods=['POST'])
# def get_answer():
#     data = request.get_json()

#     if 'question' not in data:
#         return jsonify({'error': 'Veuillez fournir une question'}), 400

#     question = data['question']
    
#     # Prétraiter la question
#     inputs = tokenizer(question, return_tensors="pt")

#     # Générer une réponse à partir du modèle
#     outputs = model.generate(**inputs, max_length=100, num_return_sequences=1)

#     # Décoder la réponse
#     response = tokenizer.decode(outputs[0], skip_special_tokens=True)

#     # Retourner la réponse sous forme de JSON
#     return jsonify({'response': response})

# if __name__ == '__main__':
#     app.run(debug=True)













# from flask import Flask, render_template, request, jsonify  # Importez jsonify
# from transformers import AutoModelForQuestionAnswering, AutoTokenizer
# import torch

# app = Flask(__name__)

# # Charger le modèle et le tokenizer depuis Hugging Face
# model_name = "CHARLESL16/gpt2-student-question-answer-memorization"
# model = AutoModelForQuestionAnswering.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

# @app.route('/', methods=['GET'])
# def hello_world():
#     return render_template('index.html')

# @app.route('/ask', methods=['POST'])
# def predict():
#     try:
#         data = request.get_json()  # Obtient les données JSON
#         question = data.get('question')  # Utilise get() pour éviter une erreur KeyError

#         # Vérifiez si la question a été fournie
#         if not question:
#             return jsonify({"error": "No question provided."}), 400

#         # Tokenisation de la question
#         inputs = tokenizer(question, return_tensors="pt")

#         # Prédire avec le modèle
#         with torch.no_grad():
#             outputs = model(**inputs)

#         # Obtenir les indices de la réponse
#         answer_start_index = outputs.start_logits.argmax().item()
#         answer_end_index = outputs.end_logits.argmax().item()

#         # Obtenir la réponse en fonction des indices
#         answer_tokens = inputs['input_ids'][0][answer_start_index:answer_end_index + 1]
#         answer = tokenizer.decode(answer_tokens)

#         return jsonify(answer=answer)  # Retourne la réponse en JSON

#     except Exception as e:
#         # Retourne un message d'erreur détaillé
#         return jsonify({"error": str(e)}), 500  # Retourne une réponse 500 en cas d'erreur

# if __name__ == '__main__':
#     app.run(port=3000, debug=True)
