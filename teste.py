import requests
import json

cidade = input("Escreva sua cidade: ")

requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=8947a1be67924f45dc1f5b77fd8ef54f')

tempo = json.loads(requisicao.text)
print('condição do tempo:', tempo['weather'][0]['main'])
print('temperatura', float(tempo['main']['temp']) - 273.15)



