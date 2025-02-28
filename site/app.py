from flask import Flask, jsonify
import random
import string
import time

app = Flask(__name__)

# Dictionnaire pour stocker les codes temporaires
codes = {}

@app.route("/")
def home():
    return "Bienvenue sur mon site de vérification !"

@app.route("/api/generate_code", methods=["GET"])
def generate_code():
    """Génère un code unique et le rend valable pendant 10 minutes."""
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    expiration_time = time.time() + 600  # Code valable pendant 10 minutes
    codes[code] = expiration_time
    return jsonify({"code": code, "expires_in": 600})

@app.route("/api/verify_code/<code>", methods=["GET"])
def verify_code(code):
    """Vérifie si le code est valide et non expiré."""
    if code in codes:
        if time.time() < codes[code]:  # Si le code n'est pas expiré
            return jsonify({"valid": True})
        else:
            del codes[code]  # Supprimer le code expiré
    return jsonify({"valid": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
