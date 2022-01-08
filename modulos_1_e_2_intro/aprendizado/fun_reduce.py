from dummy_data import lista, produtos, pessoas
from functools import reduce
"""
reduce(func(acc,item),iter,inicial) -> reduz o iter a um acumulador acc, utilizando func como função acumuladora
o valor retornado por func é passado para acc e acc é passado para a próxima iteração, com um novo item de iter
"""

soma_lista = reduce(lambda acc, i: i + acc, lista, 0)
print(soma_lista)

soma_precos = reduce(lambda acc, p: round(p["preco"] + acc), produtos, 0)
print(soma_precos)

idade_media = reduce(lambda acc,p: acc+p["idade"],pessoas,0) / len(pessoas)

print(idade_media)
