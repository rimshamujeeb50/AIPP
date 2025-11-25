import requests
import json

def get_weather_no_error_handling(city):
    api_key = "24743a68c9449d25758c2ac0e78ff300"   # Replace with your actual API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)          # No error handling (as per task)
    data = response.json()                # Convert to JSON
    pretty = json.dumps(data, indent=4)   # Pretty format
    print(pretty)                         # Display output
    return data                           # Optional return


# ---- Run the function ----
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather_no_error_handling(city_name)
