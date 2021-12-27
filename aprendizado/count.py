"""
Count function form itertools:
Gera um contador infinito, esse contador é um iterador
"""
from itertools import count

# Um contador infinito
counter1 = count()
print(next(counter1))

# Um contador que começa de 3
counter3 = count(3)
print(next(counter3))

# Um contador que começa em 0 e conta de 2 em 2
counter2_by_2 = count(start=0,step=2)
print(next(counter2_by_2))
print(next(counter2_by_2))
