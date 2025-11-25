import requests

def display_weather(city_name):
    api_key = '24743a68c9449d25758c2ac0e78ff300'  # Your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        # Check if city is found
        if response.status_code == 404 or data.get('cod') == '404':
            print("Error: City not found. Please enter a valid city.")
            return

        # Extract required fields
        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        # Display in user-friendly format
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description.capitalize()}")

    except requests.exceptions.RequestException as err:
        print(f"Error: Unable to fetch data. {err}")

# Example usage
display_weather("New York")
display_weather("xyz123")
