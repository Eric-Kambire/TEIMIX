import requests
import json
import os

API_KEY = "972b7987d0148a821a2a4236cd4f70f5"
VILLE = "Casablanca"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={VILLE}&appid={API_KEY}&units=metric&lang=fr"

def get_weather_data():
    try:
        reponse = requests.get(URL)
        reponse.raise_for_status()

        donnees = reponse.json()
        weather_data = {
            "ville": VILLE,
            "temperature": round(donnees["main"]["temp"]),
            "description": donnees["weather"][0]["description"],
            "humidity": donnees["main"]["humidity"],
            "wind_speed": round(donnees["wind"]["speed"] * 3.6, 1),  # Convert m/s to km/h
            "timestamp": donnees["dt"]
        }
        
        # Ensure static directory exists
        os.makedirs('static', exist_ok=True)
        
        # Save to both locations for compatibility
        for path in ['static/weather_data.json', 'weather_data.json']:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(weather_data, f, ensure_ascii=False)
                
        print(f"📍 Ville: {weather_data['ville']}")
        print(f"🌡 Température: {weather_data['temperature']}°C")
        print(f"☁️ Ciel: {weather_data['description']}")
        print(f"💧 Humidité: {weather_data['humidity']}%")
        print(f"💨 Vitesse du vent: {weather_data['wind_speed']} km/h")
        
        return weather_data
        
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la récupération des données météo:", e)
        return None

if __name__ == "__main__":
    get_weather_data()
