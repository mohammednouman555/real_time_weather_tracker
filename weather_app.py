import requests
from colorama import Fore, Style

API_KEY = "a7bb13c93491405aeb3d86df4f737eeb"  # Your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        print("\n=== Weather Report ===")
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels Like: {data['main']['feels_like']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
        print(f"Weather: {data['weather'][0]['description'].capitalize()}")
        print("========================\n")
    else:
        print("City not found or API error!")

def main():
    print("=== Real-Time Weather App ===")
    while True:
        city = input("\nEnter city name (or 'exit' to quit): ")
        if city.lower() == "exit":
            print("\nThank you for using the Real-Time Weather App! ☁️")
            break
        get_weather(city)

if __name__ == "__main__":
    main()
