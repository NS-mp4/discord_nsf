from flask import Flask, render_template, jsonify
import random
import string
import time
import threading

app = Flask(__name__)

# Dictionnaire pour stocker le code et son expiration
active_code = {"value": None, "expires_at": None}
CODE_DURATION = 3600  # Durée de validité du code en secondes (1 heure)

def generate_code():
    """Génère un code aléatoire à 6 caractères."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


def update_code():
    """Met à jour le code toutes les heures."""
    while True:
        # Le temps actuel
        current_time = time.time()
        
        # Si nous ne sommes pas encore à l'heure exacte, attendre jusqu'à la prochaine heure
        time_to_wait = CODE_DURATION - (current_time % CODE_DURATION)
        
        # Affichage du temps d'attente pour le debug
        print(f"Attente de {time_to_wait} secondes avant de mettre à jour le code.")
        
        # Attente jusqu'à la prochaine heure
        time.sleep(time_to_wait)
        
        # Mise à jour du code
        active_code["value"] = generate_code()
        active_code["expires_at"] = current_time + CODE_DURATION
        print(f"Nouveau code généré : {active_code['value']} (Expire dans 1 heure)")

@app.route('/')
def index():
    """Page principale affichant le code actuel."""
    return render_template('index.html', code=active_code["value"])


@app.route('/api/verify/<code>', methods=['GET'])
def verify_code(code):
    """Vérifie si un code est valide."""
    if active_code["value"] == code and time.time() < active_code["expires_at"]:
        return jsonify({"valid": True})
    return jsonify({"valid": False})


# Lancer le thread pour mettre à jour le code en arrière-plan
threading.Thread(target=update_code, daemon=True).start()

if __name__ == '__main__':
    # On démarre le serveur Flask sur le port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
