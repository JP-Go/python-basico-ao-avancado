import json

# Dicionarios podem ser convertido para json

d1 = {
    "Pessoa 1": {
        "nome": "Jack",
        "idade": 29,
    },
    "Pessoa 2": {
        "nome": "Rose",
        "idade": 27,
    },
}

# json.dumps(obj): serializa o objeto para uma string formatada como json
d1_json = json.dumps(d1, indent=True)
print(d1_json)

# Escrevendo json em um arquivo (utilizando open)
with open('output/pessoas.json', 'w+') as file:
    file.write(d1_json)
    file.seek(0, 0)
    print(file.readlines())

# Lendo o arquivo json (deserializando)
with open('output/pessoas.json', 'r') as file:
    json_str = file.read()
    novo_dict = json.loads(json_str)
    print(novo_dict, type(novo_dict))
