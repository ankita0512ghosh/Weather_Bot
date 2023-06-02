# Weather Forecast Command-Line Tool

This is a command-line tool that fetches and displays the current weather forecast for a given city. The tool leverages the OpenWeatherMap API to retrieve weather data and parses it using Python. It also demonstrates how GitHub Copilot can assist with API usage, data parsing, and error handling. Additionally, the tool provides a frontend interface through Streamlit for a user-friendly experience.

## Features

- Fetches current weather forecast data from the OpenWeatherMap API.
- Accepts a city name as input from the user.
- Displays weather information including precipitation, humidity, and temperature.
- Supports temperature units in Celsius, Fahrenheit, or Kelvin.
- Demonstrates error handling for network connectivity issues and invalid user input.
- Integrates with Streamlit to provide a frontend interface for easy interaction.

## Requirements

To run this project, you need the following:

- Python 3.7 or above
- `requests` library to make API requests (`pip install requests`)
- `streamlit` library for the frontend interface (`pip install streamlit`)

## Getting Started

1. Clone the repository:

   ```
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```
   cd weather-forecast-tool
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/) by signing up for a free account.

5. Rename the `.env.example` file to `.env` and replace `<YOUR_API_KEY>` with your actual OpenWeatherMap API key.

6. Run the command-line tool:

   ```
   python weather_tool.py
   ```

7. Open your web browser and visit `http://localhost:8501` to access the frontend interface provided by Streamlit.

8. Enter a city name in the input field and click the "Get Weather Forecast" button to view the current weather information for that city.

## Usage

When the command-line tool is running, you will be prompted to enter the name of a city. Type the city name and press Enter. The tool will retrieve the current weather forecast for that city and display the information on the console.

To use the frontend interface provided by Streamlit, open the web browser and enter the city name in the input field. Click the "Get Weather Forecast" button, and the weather information will be displayed on the webpage.

## Acknowledgments

- The OpenWeatherMap API for providing the weather data.
- GitHub Copilot for assisting with API usage, data parsing, and error handling.
- Streamlit for the frontend interface.
