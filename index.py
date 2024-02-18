import requests

api_key = '29f87feda138ff2e32bccfbfd719a584'

city = input('Enter city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    a={temp}
    b=float(list(a)[0])-273
    print(f'Temperature: ',b,' degree celsius')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')