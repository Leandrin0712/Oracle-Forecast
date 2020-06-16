import requests
import json
import sys

cidade = sys.argv[1]
print(cidade)

requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=8947a1be67924f45dc1f5b77fd8ef54f')

tempo = json.loads(requisicao.text)

sys.stdout = open("condicao.txt", "w")
print('Condição do tempo:', tempo['weather'][0]['main'])


sys.stdout.close()

sys.stdout = open("temperatura.txt", "w")
print('Temperatura:', float(tempo['main']['temp']) - 273.15)
sys.stdout.close()
