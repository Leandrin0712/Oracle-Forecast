import requests
import json
import sys


cidade = sys.argv[1]
cidadeFormatada = cidade.replace('-', ' ')

condicao = tempo['weather'][0]['main']

temperatura = float(tempo['main']['temp']) - 273.15
temperaturaFormatada = round(temperatura, 2)

# Faz a requisição da previsão 

requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=8947a1be67924f45dc1f5b77fd8ef54f')
tempo = json.loads(requisicao.text)

# Gera os arquivos para mostrar no site

sys.stdout = open("condicao.txt", "w")

print('Condição do tempo:', condicao)
sys.stdout.close()

sys.stdout = open("temperatura.txt", "w")

print('Temperatura:', temperaturaFormatada)
sys.stdout.close()
