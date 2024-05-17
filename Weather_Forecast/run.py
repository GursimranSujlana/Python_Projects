from flask import Flask, render_template, request
import requests
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
    else:
        # Default location or coordinates
        location = '42.3478,-71.0466'  # Example location

    # Fetch weather data based on the provided location
    weather_data = fetch_weather_data(location)

    # Extract relevant weather parameters
    current_weather = weather_data.get('current', {})
    temperature = current_weather.get('temperature')
    apparent_temperature = current_weather.get('apparentTemperature')
    description = current_weather.get('weather', [{}])[0].get('description')
    precipitation_probability = current_weather.get('precipitationProbability')
    wind_speed = current_weather.get('windSpeed')
    wind_direction = current_weather.get('windDirection')
    humidity = current_weather.get('humidity')
    visibility = current_weather.get('visibility')
    sunrise_time = current_weather.get('sunriseTime')
    sunset_time = current_weather.get('sunsetTime')

    return render_template('index.html', temperature=temperature, apparent_temperature=apparent_temperature,
                           description=description, precipitation_probability=precipitation_probability,
                           wind_speed=wind_speed, wind_direction=wind_direction, humidity=humidity,
                           visibility=visibility, sunrise_time=sunrise_time, sunset_time=sunset_time)

def fetch_weather_data(location):
    api_key = 'api'  # Replace with your Tomorrow.io API key
    api_url = f'https://api.tomorrow.io/v4/weather/forecast?location={location}&apikey={api_key}'
    
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch weather data. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    app.run(debug=True)
