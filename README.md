# Energy Dashboard Project

## Overview
This project is a modern energy monitoring dashboard with a Flask backend and a responsive frontend built with Tailwind CSS, Chart.js, and Leaflet.js. It provides real-time energy data, alerts, and chatbot assistance.

## Repository Structure

- **/server**  
  Contains the main Flask server application (`app_server.py`) which serves the API endpoints and static files.

- **/ui**  
  Contains the frontend HTML files:  
  - `index.html` (Login page)  
  - `dashboard.html` (Main dashboard)  
  - `monitoring.html` (Detailed monitoring with tabs and chatbot)  
  - `alerts.html` (Alerts page)  
  - `settings.html` (Settings and configuration)

- **/static**  
  Contains static assets such as CSS, JS, images, and JSON data (`weather_data.json`).

## Running the Server

1. Navigate to the server directory:  
   ```bash
   cd server
   ```

2. Run the Flask server:  
   ```bash
   python3 app_server.py
   ```

3. Access the application in your browser at:  
   ```
   http://localhost:8000
   ```

## Features

- Real-time energy consumption and production monitoring  
- Interactive charts and maps  
- Alerts and notifications  
- User login and guest mode  
- Chatbot assistant for energy-related queries  
- Configurable system settings  

## Notes

- The server serves the frontend files and API endpoints.  
- Weather data is updated every 5 minutes in the background.  
- The chatbot API supports queries in French.  
- The UI uses Google Fonts and Font Awesome for modern styling.  
- Images and icons are loaded via CDN for performance.

## Future Enhancements

- Persist user settings via API  
- Add authentication and user management  
- Integrate real sensor data for energy production and consumption  
- Improve chatbot intelligence and language support
# OPTIMIX
