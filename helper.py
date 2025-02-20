from geopy.geocoders import Nominatim  
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
import requests

def getWeather(textfield, clock, name, t, c , w , h , d , p):
    city = textfield.get().strip()

    if not city:
        print("Please enter a city name")
        return

    try:
        # Location
        geolocator = Nominatim(user_agent="geopiExercises")
        location = geolocator.geocode(city)

        if location is None:
            print(f"Error: Could not find location for '{city}'")
            return  

        # object for timezone
        obj = TimezoneFinder()
        timezone_result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        # Display time 
        home = pytz.timezone(timezone_result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #  API URL
        api_key = "89ffea58ac8b8d8692c5d93611d4a749"  # Replace with your actual API key
        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={api_key}&units=metric"


        json_data = {} 
        
        #  API Request
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                json_data = response.json()
            else:
                print(f"Error: API request failed with status code {response.status_code}")
                print("Response:", response.text)  # Print error response from API
                return  # Exit function if API request fails

        except requests.exceptions.RequestException as e:
            print(f"Error: Failed to fetch weather data: {e}")
            return  # Exit function if request fails

        # Check if 'weather' exists before using it
        if "weather" not in json_data:
            print("Error: 'weather' key not found in API response")
            return

        #  weather details
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'])
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        # Update labels in the UI
        t.config(text=f"{temp}°C")
        c.config(text=f"{condition} | Feels Like {temp}°C")
        
        #code for displaying wind , humidity , description , pressure 
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        print(f"Error: {e}")
