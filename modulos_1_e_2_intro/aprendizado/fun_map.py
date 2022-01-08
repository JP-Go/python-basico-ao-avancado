from dummy_data import lista, pessoas, produtos
"""
map(func,iter) -> executa func em cada item de iter e retorna um iterador com os itens alterados
"""
# Podem ser funções anonimas
nova_lista = list(map(lambda x: 2 * x, lista))
print(nova_lista)


def aumento(produto):
    produto['preco'] = round(produto['preco'] * 1.05, 2)
    return produto


# ou nomeadas
precos = map(aumento, produtos)

# Retorna um objeto map que é iterável
print(precos)
for preco in precos:
    print(preco)

nomes = map(lambda p: p['nome'], pessoas)
print(list(nomes))


def idade_em_10_anos(pessoa):
    pessoa['em_10_anos'] = pessoa['idade'] + 10
    return pessoa


novas_pessoas = map(idade_em_10_anos, pessoas)
print(list(pessoas))
print(list(novas_pessoas))
