import requests
from rich import print
from datetime import datetime
def current_city_weather(city):
    api_key='da7a1b3d460dbtbf7b304o1bb99604f1'
    api_url=f'https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}'
    response=requests.get(api_url)
    weather=response.json()
    current_city=weather['city']
    current_temperature=round(weather['temperature']['current'])
    print(f'The temperature in {current_city} is {current_temperature}°C')
def forcast_weather(my_city):
    api_key = 'da7a1b3d460dbtbf7b304o1bb99604f1'
    api_url = f'https://api.shecodes.io/weather/v1/forecast?query={my_city}&key={api_key}'
    response = requests.get(api_url)
    forcasts = response.json()
    for day in forcasts['daily']:
        timestamp = day['time']
        formated_date = datetime.fromtimestamp(timestamp)
        formated_day = formated_date.strftime('%A')
        temperature = round(day['temperature']['day'])
        print(f' {formated_day}: {temperature}°C')
    
my_city=input("please enter a city ")
my_city.strip()
if my_city:
    current_city_weather(my_city)
    print('\n')
    forcast_weather(my_city)
    
else:
    print("you need to imput a city 😎")