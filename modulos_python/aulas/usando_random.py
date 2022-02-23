import random
import string

# random.randint(a,b): número inteiro aleatório de a a b
# random.uniform(a,b): número float aleatório (dist uniforme) de a a b
# random.random(): Número float aleatório de 0 a 1

inteiro = random.randint(0, 20)
flutuante = random.uniform(10.0, 20.0)
aleatorio_0a1 = random.random()
print(f"Inteiro aleatório: {inteiro}")
print(f"Float aleatório de 10 a 20:  {flutuante}")
print(f"Float aleatório de 0 a 1: {aleatorio_0a1}")

# random.randrange(a,b[,delta]): número aleatório de range(a,b,delta)
com_range = random.randrange(900, 1000, 10)
print(f"Com randrange {com_range}")

candidatos = [
    'João', 'Felipe', 'Roberto', 'Pedro', 'Maria', 'Rose', 'Laiza', 'Melody'
]

# random.choice(lista): Escolhe um item aleatório de lista
sorteado = random.choice(candidatos)
print(f'Pessoa sorteada: {sorteado}')

# random.choices(lista[,k]): Escolhe k itens de uma lista e retorna a lista com a escolhas. Um item da lista pode ser escolhido mais de uma vez.

sorteio_repetido = random.choices(candidatos, k=2)
print(f'Pessoas sorteadas repetidas(?): {sorteio_repetido}')

# random.sample(lista,k): Escolhe uma sublista de lista com k itens
sorteio_unico = random.sample(candidatos, 2)
print(f'Pessoas sorteadas unicas: {sorteio_unico}')

# random.shuffle(lista): embaralha uma lista
random.shuffle(candidatos)
print(candidatos)

mostraveis = string.printable.strip(string.whitespace)

senha = ''.join(random.choices(mostraveis, k=20))
print(senha)
