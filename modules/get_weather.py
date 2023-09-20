import requests
import json

API = 'API token'


def get_weather():
    """Shows weather in entered city"""
    city = input("Enter the name of the city: ").strip().lower()
    res = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = {
            'temperature': data['main']['temp'],
            'sky': data['weather'][0]['main'],
            'wind speed': data['wind']['speed']
        }
        print(f""" Now the weather in {city} is: 
            The temperature is: {temp['temperature']}
            The sky is: {temp['sky']}
            The wind speed is: {temp['wind speed']}
""")
    else:
        print('The name of the city is entered incorrectly!')
