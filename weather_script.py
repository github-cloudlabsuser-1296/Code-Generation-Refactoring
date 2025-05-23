import requests

def fetch_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    # Replace with your actual OpenWeatherMap API key
    API_KEY = "5990e53a1b76a81e0200b84788850ef1"
    city = input("Enter city name: ")
    try:
        weather_data = fetch_weather(city, API_KEY)
        print(f"Weather in {city}: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
    except requests.HTTPError as e:
        print(f"Failed to fetch weather data: {e}")