import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, request, jsonify, send_from_directory, redirect, url_for
from flask_cors import CORS
import threading
import time
from weather_service import get_weather_data

app = Flask(__name__, static_url_path='')
CORS(app)

@app.route('/')
def root():
    return send_from_directory('../ui', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('../ui', path)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        query = data.get('message', '').lower()
        
        responses = {
            "consommation": "Votre consommation d'énergie actuelle est optimale. Les panneaux solaires fonctionnent à 85% d'efficacité.",
            "économies": "Sur la base des données actuelles, vous avez économisé 50kg de CO2 ce mois-ci grâce à l'utilisation d'énergie renouvelable.",
            "maintenance": "La prochaine maintenance est prévue dans 2 semaines. Tous les systèmes fonctionnent normalement.",
            "aide": "Je peux vous aider avec : la consommation d'énergie, les économies, les horaires de maintenance et l'état général du système.",
            "état": "Tous les systèmes fonctionnent normalement. Efficacité solaire : 85%, Éolienne : active, Batterie : 70% chargée."
        }
        
        response = "Je ne suis pas sûr de comprendre. Essayez de me poser des questions sur la consommation, les économies, la maintenance ou l'état du système."
        for key in responses:
            if key in query:
                response = responses[key]
                break
        
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({
            "response": "Désolé, une erreur s'est produite. Veuillez réessayer.",
            "error": str(e)
        }), 500

def update_weather():
    while True:
        try:
            get_weather_data()
            print("Weather data updated successfully")
        except Exception as e:
            print(f"Error updating weather data: {e}")
        time.sleep(300)  # Update every 5 minutes

if __name__ == '__main__':
    # Ensure static directory exists
    os.makedirs('static', exist_ok=True)
    
    # Start weather updates in background
    weather_thread = threading.Thread(target=update_weather)
    weather_thread.daemon = True
    weather_thread.start()
    
    # Start Flask server
    app.run(host='0.0.0.0', port=8000, debug=True)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        query = data.get('message', '').lower()
        
        responses = {
            "consommation": "Votre consommation d'énergie actuelle est optimale. Les panneaux solaires fonctionnent à 85% d'efficacité.",
            "économies": "Sur la base des données actuelles, vous avez économisé 50kg de CO2 ce mois-ci grâce à l'utilisation d'énergie renouvelable.",
            "maintenance": "La prochaine maintenance est prévue dans 2 semaines. Tous les systèmes fonctionnent normalement.",
            "aide": "Je peux vous aider avec : la consommation d'énergie, les économies, les horaires de maintenance et l'état général du système.",
            "état": "Tous les systèmes fonctionnent normalement. Efficacité solaire : 85%, Éolienne : active, Batterie : 70% chargée."
        }
        
        response = "Je ne suis pas sûr de comprendre. Essayez de me poser des questions sur la consommation, les économies, la maintenance ou l'état du système."
        for key in responses:
            if key in query:
                response = responses[key]
                break
        
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({
            "response": "Désolé, une erreur s'est produite. Veuillez réessayer.",
            "error": str(e)
        }), 500

def update_weather():
    while True:
        try:
            get_weather_data()
            print("Weather data updated successfully")
        except Exception as e:
            print(f"Error updating weather data: {e}")
        time.sleep(300)  # Update every 5 minutes

if __name__ == '__main__':
    # Ensure static directory exists
    os.makedirs('static', exist_ok=True)
    
    # Start weather updates in background
    weather_thread = threading.Thread(target=update_weather)
    weather_thread.daemon = True
    weather_thread.start()
    
    # Start Flask server
    app.run(host='0.0.0.0', port=8000, debug=True)
