import requests
import streamlit as st
import json
import os
from dotenv.main import load_dotenv

load_dotenv()
def get_weather(city):
    """Gets the current weather forecast for the given city."""

    # Get the API key from OpenWeatherMap.
    api_key = os.environ['API_KEY'] 

    # Make a request to the OpenWeatherMap API.
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)
    )

    # Check for errors.
    if response.status_code != 200:
        raise Exception("Error getting weather data: {}".format(response.status_code))

    # Parse the JSON response.
    weather_data = json.loads(response.content.decode("utf-8"))

    # Return the current weather forecast.
    return weather_data["weather"][0]["description"], weather_data["main"]["temp"], weather_data["main"]["pressure"], weather_data["main"]["humidity"]

#main function
if __name__ == "__main__":

    # Create a title for the app.
    st.title("Weather Forecast")

    # Get the city name from the user.
    city = st.text_input("Enter a city name: ")

    # Show the weather forecast for the city.
    if city:
        weather_description, temperature, pressure, humidity = get_weather(city)

        # Add a background image.
        st.markdown(f"""<style>.stApp {{
             background-image: url("https://images.unsplash.com/photo-1474540412665-1cdae210ae6b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y2FsbXxlbnwwfHwwfHx8MA%3D%3D&w=1000&q=80");
             background-attachment: fixed;
             background-size: cover
         }}</style>""",unsafe_allow_html=True)

        # Add a heading.
        st.header("Weather in **{}** ".format(city))

        # Add a paragraph.
        st.markdown("The weather in **{}** is **{}** and the temperature is **{}** Kelvin Unit.".format(city, weather_description, temperature))
        
        col1, col2, col3 = st.columns(3)
        
        # Add a button to convert the temperature to Celsius.
        with col1:
            convert_to_celsius = st.button("Convert to Celsius")

        if convert_to_celsius:
            temperature_in_celsius = float("{:.2f}".format(temperature - 273.15))
            st.markdown(
                f"""
                    The temperature in **{city}** is **{weather_description}** and the temperature is **{temperature_in_celsius}** degrees Celsius.
                    """
                )

        #Add button to convert the temperature to Fahrenheit
        with col2:
            convert_to_fahrenheit = st.button("Convert to Fahrenheit")

        if convert_to_fahrenheit:
            temperature_in_fahrenheit = float("{:.2f}".format((temperature - 273.15) * 9 / 5 + 32))
            st.markdown(
                f"""
                    The temperature in **{city}** is **{weather_description}** and the temperature is **{temperature_in_fahrenheit}** degrees Fahrenheit.
                    """
                )

        #Add pressure and humidity
        with col3:
            p_and_h = st.button("Pressure and Humidity")
            
        if p_and_h:
            st.markdown("The pressure is **{}** hPa and the humidity is **{}**%.".format(pressure, humidity))