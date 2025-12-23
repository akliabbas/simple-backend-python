import os
from flask import Flask, jsonify, request  # <- ajouter request

app = Flask(__name__)

# Route GET racine
@app.route('/')
def home():
    return "Hello World from Render Akli!"

# Route GET JSON
@app.route('/api/data')
def data():
    return jsonify({"message": "Exemple de JSON via un PaaS"})

# Route POST pour recevoir des données
@app.route('/api/postdata', methods=['POST'])
def post_data():
    try:
        # Récupère les données JSON envoyées
        data = request.get_json()
        # Exemple simple : renvoie ce qui a été reçu
        return jsonify({"received": data}), 200
    except:
        return jsonify({"error": "Invalid JSON"}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
