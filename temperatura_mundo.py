def get_weather(city):
    import requests
    url= 'https://api.weatherbit.io/v2.0/current?city=' + city + '&key=f4e3cc35398f49ff910168b505d58275'
    r= requests.get(url)
    data = r.json()
    return data['data'][0]['temp']

cidade = str(input('Nome da cidade que você deseja saber a temperatura: ')) 
print('A temperatura em {} é de {}°C'.format(cidade, get_weather(cidade)))

