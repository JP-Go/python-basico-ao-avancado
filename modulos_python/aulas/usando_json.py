from dados import *
import json

lista = [1, 2, 3, 4, 5, 6]
# json.dumps(dados): transforma dados em uma string json
dados_json = json.dumps(lista)
dados_clientes = json.dumps(clientes_dicionario, indent=4)
print(dados_json)
print(dados_clientes)

# json.loads(string json-like): transforma a string em um objeto nativo do python

dicionário_clientes = json.loads(clientes_json)
print(dicionário_clientes)

# json.dump(dados,file-like obj): dump em um arquivo json file-like obj é um
# handler de arquivo (retorno da fun open())
with open('aulas/output/clientes.json', 'w') as file:
    json.dump(clientes_dicionario, file, indent=4)

print('####################')
print()
# json.load(file-like obj): lê json de um arquivo
with open('aulas/output/clientes.json', 'r') as file:
    # le o arquivo e retorna um dicionário para esse arquivo
    data = json.load(file)
    for key, value in data.items():
        print(key, value)
