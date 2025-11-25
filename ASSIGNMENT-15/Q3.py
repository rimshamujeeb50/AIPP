import requests

def display_weather_details(city):
    api_key = "24743a68c9449d25758c2ac0e78ff300"   # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)     # No error handling required for Task 3
    data = response.json()

    # Extract specific fields
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    # User-friendly display
    print("\n===== WEATHER REPORT =====")
    print(f"City: {city.title()}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {description.title()}")


# ---- Run the function ----
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    display_weather_details(city_name)
