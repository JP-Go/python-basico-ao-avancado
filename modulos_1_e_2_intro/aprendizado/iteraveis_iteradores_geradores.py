# Iteraveis são objetos que possuem o metodo  __iter__
# Iterador é um objeto que possui o método __next__

from typing import Generator
from sys import getsizeof
from time import time


lista = list(range(10))

print(hasattr(lista, "__iter__"))  # Lista é iterável
print(hasattr(lista, "__next__"))  # Lista NÃO é um iterador

# Podemos criar um iterador de um iterável utilizando a função iter()

iterador_da_lista = iter(lista)
print(iterador_da_lista)

# Para conseguir o próximo elemento de um iterador, utilizamos a função next()

print(next(iterador_da_lista))

# Geradores são utilizados para otimizar o espaço utilizado por iteráveis. Um exemplo:


def generate_list(n: int) -> Generator:
    for i in range(n):
        yield i


gen = generate_list(1000)  # Gerador de uma lista enorme. Esse gerador é iteravel
lista2 = list(range(1000))

print(gen)
print(f"tamanho gerador {getsizeof(gen)} tamanho lista {getsizeof(lista2)} (em bytes)")


def percorre_gerador(gerador: Generator) -> None:
    for _ in gerador:
        pass


def percorre_lista(lista: list) -> None:
    for _ in lista:
        pass


start_list = time()
percorre_lista(lista2)
end_list = time()
print("Tempo de execucao da lista:", end_list - start_list)

start_gen = time()
percorre_gerador(gen)
end_gen = time()
print("Tempo de execucao gerador:", end_gen - start_gen)

# Listas são mais rápidas que geradores
