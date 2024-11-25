from flask import Flask, render_template, request, redirect
import requests
import json
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')

    if not latitude or not longitude:
        return redirect('/')

    # Construct the API URL with the provided latitude and longitude
    url = f'https://api.weather.gov/points/{latitude},{longitude}'

    # Make a request to the data source
    response = requests.get(url)
    data = json.loads(response.text)

    # Extract relevant information from the response data
    coordinates = data['geometry']['coordinates']
    forecast_office = data['properties']['forecastOffice']
    relative_location = data['properties']['relativeLocation']
    city = relative_location['properties']['city']
    state = relative_location['properties']['state']
    forecast_url = data['properties']['forecast']

    # Make a request to the forecast URL to get the weather forecast data
    forecast_response = requests.get(forecast_url)
    forecast_data = json.loads(forecast_response.text)

    # Extract the weather forecast from the forecast data
    periods = forecast_data['properties']['periods']
    weather_forecast = [(period['name'], period['detailedForecast']) for period in periods]

    # Pass the extracted data to the dashboard template
    return render_template('dashboard.html', coordinates=coordinates,
                           forecast_office=forecast_office, city=city, state=state,
                           weather_forecast=weather_forecast)

if __name__ == '__main__':
    app.run(debug=True)
