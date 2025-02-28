from flask import Flask, render_template, jsonify, request
import random
import string
import time
import threading

app = Flask(__name__)

# Liste des IP autorisées
ALLOWED_IPS = ["192.168.1.1", "203.0.113.0"]  # Remplace ces IP par celles que tu autorises

# Dictionnaire pour stocker le code et son expiration
active_code = {"value": None, "expires_at": None}
CODE_DURATION = 300  # Durée de validité en secondes (5 minutes)


def generate_code():
    """Génère un code aléatoire à 6 caractères."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


def update_code():
    """Met à jour le code périodiquement."""
    while True:
        active_code["value"] = generate_code()
        active_code["expires_at"] = time.time() + CODE_DURATION
        print(f"Nouveau code généré : {active_code['value']} (Expire dans {CODE_DURATION} sec)")
        time.sleep(CODE_DURATION)


def check_ip():
    """Vérifie si l'IP de la requête est autorisée."""
    user_ip = request.remote_addr  # Obtient l'IP de l'utilisateur
    if user_ip not in ALLOWED_IPS:
        return False
    return True


@app.route('/')
def index():
    """Page principale affichant le code actuel si l'IP est autorisée."""
    if not check_ip():  # Vérifie si l'IP de la requête est autorisée
        return jsonify({"error": "Accès non autorisé"}), 403

    return render_template('index.html', code=active_code["value"])


@app.route('/api/verify/<code>', methods=['GET'])
def verify_code(code):
    """Vérifie si un code est valide."""
    if not check_ip():  # Vérifie si l'IP de la requête est autorisée
        return jsonify({"error": "Accès non autorisé"}), 403
    
    if active_code["value"] == code and time.time() < active_code["expires_at"]:
        return jsonify({"valid": True})
    return jsonify({"valid": False})


# Lancer le thread pour mettre à jour le code en arrière-plan
threading.Thread(target=update_code, daemon=True).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
