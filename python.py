import requests
import json
import sys

tamanho = len(sys.argv) - 1

if tamanho == 1:
	cidade = sys.argv[1]
elif tamanho == 2:
	cidade = '{} {}'.format(sys.argv[1], sys.argv[2])
else:
	cidade = '{} {} {}'.format(sys.argv[1], sys.argv[2], sys.argv[3])

# Faz a requisição da previsão 

requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + cidade + '&appid=8947a1be67924f45dc1f5b77fd8ef54f')
tempo = json.loads(requisicao.text)

# Gera os arquivos para mostrar no site

sys.stdout = open("condicao.txt", "w")
print('Condição do tempo:', tempo['weather'][0]['main'])
sys.stdout.close()

sys.stdout = open("temperatura.txt", "w")
temperatura = float(tempo['main']['temp']) - 273.15
temperaturaArredondada = round(temperatura, 2)
print('Temperatura:', temperaturaArredondada)
sys.stdout.close()
