import requests
from colorama import init, Fore, Style

init(autoreset=True)  # automatically reset colors after each print

API_KEY = "74073f1d71032474092aa55018960419"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    """
    Fetches and prints weather information for a given city.
    """
    url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and "main" in data and "weather" in data:
        main = data['main']
        weather = data['weather'][0]

        temperature = main['temp']
        humidity = main['humidity']
        description = weather['description']

        # Color coding based on temperature
        if temperature >= 30:
            temp_color = Fore.RED
        elif temperature >= 20:
            temp_color = Fore.YELLOW
        else:
            temp_color = Fore.CYAN

        print(f"\nWeather in {city}:")
        print(f"Temperature: {temp_color}{temperature}°C{Style.RESET_ALL}")
        print(f"Humidity: {Fore.BLUE}{humidity}%{Style.RESET_ALL}")
        print(f"Condition: {Fore.MAGENTA}{description.capitalize()}{Style.RESET_ALL}")
    else:
        print(Fore.RED + "City not found or API error!" + Style.RESET_ALL)


# If this script is run directly, ask for user input
if __name__ == "__main__":
    
    get_weather(input("Enter city name: "))
