from dummy_data import pessoas, lista, produtos

nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))

produtos_caros = filter(lambda p: p["preco"] > 30, produtos)
for produto in produtos_caros:
    print(produto)


def filtro(produto):
    if produto["preco"] >= 50:
        return True
    return False

menores_de_idade = filter(lambda p:p["idade"] <18,pessoas)

for pessoa in menores_de_idade:
    print(pessoa)
