import requests
import json

def get_weather(city):
    """Gets the current weather forecast for the given city."""

    # Get the API key from OpenWeatherMap.
    API_KEY = "5New 8bb081f22fea521a4a3cd7ccb24aa88"

    # Make a request to the OpenWeatherMap API.
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, API_KEY)
    )

    # Check for errors.
    if response.status_code != 200:
        raise Exception("Error getting weather data: {}".format(response.status_code))

    # Parse the JSON response.
    weather_data = json.loads(response.content)

    # Return the current weather forecast.
    return weather_data["weather"][0]["description"], weather_data["main"]["temp"]

if __name__ == "__main__":
    # Get the city name from the command line.
    city = input("Enter a city name: ")

    # Get the current weather forecast.
    weather_description, temperature = get_weather(city)

    # Print the weather forecast.
    print("The weather in {} is {} and the temperature is {} degrees Fahrenheit.".format(city, weather_description, temperature))