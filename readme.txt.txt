# Weather App

## Description

This is a simple weather application built using Python's Tkinter library for the graphical user interface. It fetches real-time weather data from the OpenWeatherMap API and displays information such as temperature, wind speed, humidity, pressure, and a brief weather description based on the city entered by the user.

## Features

- Fetches weather data for any city worldwide
- Displays current temperature, weather condition, wind speed, humidity, and pressure
- Shows real-time local time for the selected location
- User-friendly graphical interface built with Tkinter
- Error handling for invalid city names and API request failures
- Responsive UI layout with well-structured labels and fields

## Files and Their Functions

1. **helper.py**

   - Fetches weather data from the OpenWeatherMap API
   - Uses `geopy` to get location coordinates
   - Uses `timezonefinder` and `pytz` to determine the local time of the city
   - Handles errors and ensures smooth API communication
   - Updates the UI with weather information

2. **ui.py**

   - Creates the graphical user interface using Tkinter
   - Contains input fields, buttons, labels, and images for displaying weather data
   - Calls the `getWeather` function from `helper.py` when the user searches for a city
   - Organizes widgets for an intuitive user experience

3. **run.py**

   - Starts the application by calling the `ui()` function from `ui.py`
   - Acts as the main entry point for the weather app

## Requirements

- Python 3.x
- Required Python libraries:
  - tkinter`
  - geopy`
  - timezonefinder`
  - pytz`
  - requests`

## Installation & Usage

1. Clone or download this repository.
2. Install the required dependencies using:
   
   pip install geopy timezonefinder pytz requests
   
3. Run the application:
   
   python run.py
   
4. Enter the city name in the search box and press the search button.

## Notes

- Ensure you have an active internet connection for fetching weather data.
- Replace the API key in `helper.py` with your own OpenWeatherMap API key.
- The application uses local images stored at specific paths (`Weather App/images/`). Update these paths as needed for proper UI rendering.
- If the UI does not display correctly, verify that all images are in the correct directory.

## Credits

Developed by **Shubham Parmar**

