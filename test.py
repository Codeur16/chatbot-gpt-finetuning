import requests

url = "http://127.0.0.1:5000/answer"
data = {
    "question": "Quel est le matricule de l'étudiant ayant le nom NOA NGONO NOA Yannick"
}

response = requests.post(url, json=data)
print(response.json())
