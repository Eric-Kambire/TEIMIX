from flask import Flask, request, jsonify, send_from_directory
import threading
import time
from weather_service import get_weather_data
import os

# Initialize Flask app with default static folder (static)
app = Flask(__name__)

# Serve UI files
@app.route('/')
def root():
    return send_from_directory('ui', 'monitoring.html')

@app.route('/<path:path>')
def serve_ui(path):
    # First try to serve from static directory
    try:
        return send_from_directory('static', path)
    except:
        # If not found in static, try ui directory
        try:
            return send_from_directory('ui', path)
        except:
            return "File not found", 404

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    query = data.get('message', '').lower()
    
    responses = {
        "consumption": "Your current energy consumption is optimal. The solar panels are operating at 85% efficiency.",
        "savings": "Based on current data, you've saved 50kg of CO2 this month through renewable energy usage.",
        "maintenance": "Next scheduled maintenance is in 2 weeks. All systems are currently operating normally.",
        "help": "I can help you with: energy consumption, savings, maintenance schedules, and general system status.",
        "status": "All systems are running normally. Solar efficiency: 85%, Wind turbine: active, Battery: 70% charged."
    }
    
    response = "I'm not sure about that. Try asking about consumption, savings, maintenance, or system status."
    for key in responses:
        if key in query:
            response = responses[key]
            break
    
    return jsonify({"response": response})

def update_weather():
    while True:
        try:
            get_weather_data()
        except Exception as e:
            print(f"Error updating weather data: {e}")
        time.sleep(300)

if __name__ == '__main__':
    # Ensure static directory exists
    os.makedirs('static', exist_ok=True)
    
    # Start weather updates in background
    weather_thread = threading.Thread(target=update_weather)
    weather_thread.daemon = True
    weather_thread.start()
    
    # Start Flask server
    app.run(host='0.0.0.0', port=8000)
