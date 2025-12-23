import os
from flask import Flask, jsonify

app = Flask(__name__)

# Route racine
@app.route('/')
def home():
    return "Hello World from Render Akli!"

# Route JSON
@app.route('/api/data')
def data():
    return jsonify({"message": "Exemple de JSON via un PaaS"})

# Lancement de l'application
if __name__ == "__main__":
    # Render fournit le port via une variable d'environnement
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
