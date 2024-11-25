# Data Parsing and Dashboard Web App

## Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python 3
- Flask library (`pip install flask`)

## Getting Started

1. Open a terminal or command prompt and navigate to the project folder.
2. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

3. Start the Flask development server:

   ```
   flask run
   ```

4. Access the web app by visiting `http://localhost:5000` in your web browser.

## How it Works

1. The Flask web app consists of two routes:

   - `/`: This is the homepage route that displays a button labeled "Parse Data from Source".
   - `/dashboard`: This route is triggered when the "Parse Data" button is clicked. It makes a GET request to the data source, extracts relevant information, and renders the dashboard template.

2. When the user clicks the "Parse Data from Source" button on the homepage, the application sends a request to the data source `https://api.weather.gov/points/37.7749,-122.4194`.
3. The response from the data source is parsed and relevant information is extracted, such as the coordinates, forecast office, city, and state.
4. The extracted data is then passed to the `dashboard.html` template, where it is displayed in a user-friendly format.

## Project Structure

- `app.py`: This is the main Flask application file that contains the routes and logic for parsing and displaying data.
- `templates/`: This folder contains the HTML templates used by the Flask application.

  - `index.html`: The homepage template with a button to trigger data parsing.
  - `dashboard.html`: The dashboard template that displays the parsed data.

- `requirements.txt`: A file containing the required dependencies for the application. You can install these dependencies using `pip install -r requirements.txt`.
