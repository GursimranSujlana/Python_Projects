document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('search-form');
    const input = document.getElementById('location-input');
    const forecastContainer = document.getElementById('forecast-container');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const location = input.value.trim();
        if (location !== '') {
            fetchWeatherData(location);
        } else {
            alert('Please enter a location.');
        }
    });
});

function fetchWeatherData(location) {
    fetch(`/weather/${location}`)
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Network response was not ok.');
            }
        })
        .then(data => {
            updateWeatherUI(data);
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}

function updateWeatherUI(data) {
    const forecastContainer = document.getElementById('forecast-container');
    forecastContainer.innerHTML = ''; // Clear previous content

    const forecastData = data.forecast;
    for (const forecastItem of forecastData) {
        const forecastItemElement = document.createElement('div');
        forecastItemElement.classList.add('forecast-item');

        const dayElement = document.createElement('div');
        dayElement.classList.add('day');
        dayElement.textContent = forecastItem.day;
        forecastItemElement.appendChild(dayElement);

        const temperatureElement = document.createElement('div');
        temperatureElement.classList.add('temperature');
        temperatureElement.textContent = `${forecastItem.temperature}°C`;
        forecastItemElement.appendChild(temperatureElement);

        forecastContainer.appendChild(forecastItemElement);
    }
}
