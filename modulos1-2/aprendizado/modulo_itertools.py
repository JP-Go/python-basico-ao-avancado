"""
count([start=0,step=1]) -> Gera um contador infinito, esse contador é um iterador
permutations(iter,[n=len(iter)]) -> resulta em um iterável de todas as permutações de n itens de iter
combinations(iter,n=2) ->  resulta em um iterável com todas as combinações de n itens de iter
product(*iters,repeat=1) -> resulta em um iterável com todas as combinações de itens de cada iterável em *iters
repeat: número de vezes que *iters vai ser repetido: product(A,repeat=3) = product(A,A,A)
"""
from itertools import count, permutations, combinations, product

# Um contador infinito
counter1 = count()
print(next(counter1))

# Um contador que começa de 3
counter3 = count(3)
print(next(counter3))

# Um contador que começa em 0 e conta de 2 em 2
counter2_by_2 = count(start=0, step=2)
print(next(counter2_by_2))
print(next(counter2_by_2))

um_iteravel = 'ABCD'
print("Permutações de todos os itens: ")
for item in permutations(um_iteravel):
    print(item)
print("Combinações de dois em dois: ")
for item in combinations(um_iteravel, 2):
    print(item)
print("Produto: ", )
for item in product(um_iteravel, repeat=2):
    print(item)
