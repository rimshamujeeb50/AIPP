import requests
import json
def get_and_store_weather(city):
    api_key = "24743a68c9449d25758c2ac0e78ff300"   # Replace with your actual key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=10)
        # If API returns invalid city / wrong key
        if response.status_code != 200:
            print("Error: City not found or invalid API call.")
            return

        data = response.json()

        # Pretty JSON output
        print("\n===== RAW JSON OUTPUT =====")
        print(json.dumps(data, indent=4))

        # Extract fields
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        # Create final dictionary to store
        entry = {
            "city": city.title(),
            "temperature": temperature,
            "humidity": humidity,
            "weather": description.title()
        }

        # Append to a local text file
        with open("results.txt", "a") as file:
            file.write(json.dumps(entry) + "\n")

        # Friendly console output
        print("\n===== STORED WEATHER REPORT =====")
        print(f"City: {entry['city']}")
        print(f"Temperature: {entry['temperature']}°C")
        print(f"Humidity: {entry['humidity']}%")
        print(f"Weather: {entry['weather']}")
        print("\nWeather data appended to results.txt")

    except Exception as e:
        print("Error: Could not connect to the API. Check your network or API key.")
        print("Details:", e)


# RUN
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_and_store_weather(city_name)
