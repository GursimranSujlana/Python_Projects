# weather.py
import requests

def fetch_weather_data(location, api_key):
    """
    Fetch weather data from the Tomorrow.io API based on the provided location.

    Args:
    - location (str): The location for which to fetch weather data.
    - api_key (str): The API key for accessing the Tomorrow.io API.

    Returns:
    - dict: Weather data for the specified location.
    """
    # API endpoint
    api_url = f'https://api.tomorrow.io/v4/weather/forecast?location={location}&apikey={api_key}'
    
    # Make the API request
    response = requests.get(api_url)
    
    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        # If the request was not successful, raise an exception
        response.raise_for_status()
