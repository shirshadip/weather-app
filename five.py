import requests
from datetime import datetime

API_KEY = "enter your API key of openweathermap.org"

def get_forecast(city):
    """
    Fetches and prints current weather and 5-day forecast for a given city.
    """
    # Get current weather
    current_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    current_response = requests.get(current_url)

    if current_response.status_code == 200:
        data = current_response.json()
        main = data.get('main', {})
        weather = data.get('weather', [{}])[0]
        sys_info = data.get('sys', {})

        temperature = main.get('temp')
        feels_like = main.get('feels_like')
        humidity = main.get('humidity')
        description = weather.get('description', '')

        sunrise = datetime.fromtimestamp(sys_info.get('sunrise', 0)).strftime("%H:%M:%S") if sys_info.get('sunrise') else "N/A"
        sunset = datetime.fromtimestamp(sys_info.get('sunset', 0)).strftime("%H:%M:%S") if sys_info.get('sunset') else "N/A"

        print(f"\nWeather in {city.capitalize()}:")
        print(f"Temperature: {temperature}°C (Feels like {feels_like}°C)")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description.capitalize()}")
        print(f"🌅 Sunrise: {sunrise}")
        print(f"🌇 Sunset: {sunset}")
    else:
        print("API request failed with status:", current_response.status_code)
        return

    # Get 5-day forecast
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    if response.get("cod") != "200":
        print("Error fetching forecast:", response.get("message", "Unknown error"))
        return

    print(f"\n5-Day Weather Forecast for {city.capitalize()}:\n")

    daily_data = {}
    for entry in response["list"]:
        date = datetime.fromtimestamp(entry["dt"]).strftime("%Y-%m-%d")
        temp = entry["main"]["temp"]
        weather = entry["weather"][0]["description"]

        if date not in daily_data:
            daily_data[date] = {"temps": [], "conditions": []}

        daily_data[date]["temps"].append(temp)
        daily_data[date]["conditions"].append(weather)

    for date, data in daily_data.items():
        avg_temp = sum(data["temps"]) / len(data["temps"])
        most_common_weather = max(set(data["conditions"]), key=data["conditions"].count)
        print(f"{date}: {avg_temp:.1f}°C, {most_common_weather.capitalize()}")


# Only run interactively
if __name__ == "__main__":
    
    get_forecast(city=input("Enter city name (e.g., kolkata,IN): "))
