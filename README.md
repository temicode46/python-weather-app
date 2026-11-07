# Python Weather App 🌦️

A simple Python weather application that allows users to search for a city and retrieve its current weather information using the Open-Meteo API.

## Features

- Search for different cities by name.
- Automatically retrieves city coordinates.
- Displays current temperature in Celsius.
- Shows weather conditions (sunny, cloudy, rainy, etc.).
- Displays humidity and wind speed.
- Shows the last weather update time.

## Technologies Used

- Python
- Requests library
- Open-Meteo Geocoding API
- Open-Meteo Weather API

## How to Run

1. Make sure Python is installed.
2. Install the Requests library:

   `pip install requests`

3. Download or clone this repository.
4. Run the program:

   `python weather.py`

5. Enter a city name when prompted.

## Example Output

```text
Enter a city: Lagos

Found: Lagos
Country: Nigeria

===== WEATHER REPORT =====
Temperature: 28.5 °C
Conditions: Partly cloudy
Humidity: 80 %
Wind Speed: 10.3 km/h
==========================
```

*Example output only. Actual weather data changes.*

## API Source

Weather data provided by [Open-Meteo](https://open-meteo.com/).

## About

This project was created as part of my journey learning Python and building practical programming projects.