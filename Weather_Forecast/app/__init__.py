from flask import Flask, render_template
import requests

# Initialize Flask application
app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    # Fetch real-time weather data from an API
    api_key = 'api_key'  # Replace with your actual API key
    location = '42.3478,-71.0466'  # Example location
    api_url = f'https://api.tomorrow.io/v4/weather/forecast?location={location}&apikey={api_key}'
    
    # Make the API request
    response = requests.get(api_url)
    
    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        weather_data = response.json()
        
        # Check if 'current' key exists in weather_data
        if 'current' in weather_data:
            current_weather = weather_data['current']
        else:
            current_weather = None  # No current weather data available
        
        return render_template('index.html', current_weather=current_weather)
    else:
        return 'Error fetching weather data'

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
