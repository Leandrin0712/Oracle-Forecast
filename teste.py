import requests
import json
import sys

tamanho = len(sys.argv) - 1

if tamanho == 1:
	cidade = sys.argv[1]
	print(cidade)
elif tamanho == 2:
	print(sys.argv[1], sys.argv[2])


print(cidade)

# Faz a requisição da previsão 

requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=8947a1be67924f45dc1f5b77fd8ef54f')
tempo = json.loads(requisicao.text)

# Gera os arquivos para mostrar no site

sys.stdout = open("condicao.txt", "w")
print('Condição do tempo:', tempo['weather'][0]['main'])
sys.stdout.close()

sys.stdout = open("temperatura.txt", "w")
print('Temperatura:', float(tempo['main']['temp']) - 273.15)
sys.stdout.close()
