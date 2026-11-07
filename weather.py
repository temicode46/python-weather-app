
import requests

# Ask the user for a city
city = input("Enter a city: ")

# Search for the city
geo_url = "https://geocoding-api.open-meteo.com/v1/search"

geo_parameters = {
    "name": city,
    "count": 1,
    "language": "en",
    "format": "json"
}

geo_response = requests.get(geo_url, params=geo_parameters)
geo_data = geo_response.json()

# Check if the city was found
if "results" not in geo_data:
    print("City not found!")
else:
    location = geo_data["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]

    print("Found:", location["name"])
    print("Country:", location["country"])

    # Get the weather
    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_parameters = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
    }

    weather_response = requests.get(weather_url, params=weather_parameters)
    weather_data = weather_response.json()

    current = weather_data["current"]
    weather_codes = {
    0: "Clear sky ☀️",
    1: "Mainly clear 🌤️",
    2: "Partly cloudy ⛅",
    3: "Overcast ☁️",
    45: "Foggy 🌫️",
    48: "Foggy 🌫️",
    51: "Light drizzle 🌦️",
    61: "Rain 🌧️",
    63: "Moderate rain 🌧️",
    65: "Heavy rain 🌧️",
    71: "Snow ❄️",
    80: "Rain showers 🌦️",
    95: "Thunderstorm ⛈️"
}

    weather_code = current["weather_code"]
    description = weather_codes.get(weather_code, "Unknown conditions")

    # Display the report
    print("\n===== WEATHER REPORT =====")
    print("Temperature:", current["temperature_2m"], "°C")
    print("Conditions:", description)
    print("Humidity:", current["relative_humidity_2m"], "%")
    print("Wind Speed:", current["wind_speed_10m"], "km/h")
    print("Last Updated:", current["time"])
    print("==========================")