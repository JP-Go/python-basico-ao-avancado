# Poo -> paradigma de programação em que objetos, físicos ou abstratos, do
# mundo real são representados em código

# Estrutura de criação uma classe em python:
# class Nome_da_Classe(Classe-mãe): -> Nome e classe-mãe geralente em PascalCase
# (Primeira letra de cada palavra em maiúsculo)

# Uma classe representa um 'molde' de como um objeto é construido. Por exemplo:
# uma pessoa, em termos gerais, pode possuir nome, telefone, endereço, pode
# falar, pode olhar, pode andar. Essas caractertísticas, em termos gerais,
# fazem parte do que uma pessoa é.

# Um objeto, em POO, é uma instância de uma classe, isto é, é algo criado a partir
# de uma classe, com suas características específicas: Por exemplo, uma pessoa
# com nome João, que mora em Teresina, e tem um telefone da oi é um objeto de classe
# pessoa.

from datetime import datetime


# Exemplo da definição de classe em python
class Pessoa:

    # Variável de classe: pertence a classe, e não somente a um objeto
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    # É passado para todos os objetos dessa classe, logo pode ser acessado com self

    # Inicializador da classe (O que a classe precisa de início)
    def __init__(self, nome, idade, comendo=False, falando=False):
        # self é um parâmetro quse sempre passado a métodos de uma classe
        # e se refere a instância de um objeto. É autmaticamente passado
        # Passando nome à instância de Pessoa, a instancia, quando inicializada
        # terá os atributos abaixo
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    # Método da classe pessoa: Ações que a pessoa pode realizar
    def falar(self):
        # self.falando refere-se ao atributo falando do objeto de classe pessoa
        # criada, definido no Instanciamento
        if not self.falando:
            print('Humpf!')
            return
        print("Bla " * 3)

    def comer(self, comida: str) -> None:
        anuncio = 'Estou com vontade de comer'
        if self.comendo:
            anuncio = 'Estou comendo'
        print(anuncio, comida.lower())

    def get_ano_nascimento(self):
        print(f'{self.nome} nasceu no ano de {self.ano_atual - self.idade}')
        pass


# Instanciamento de uma classe, definição de um objeto
p1 = Pessoa("Luiz", 25)

# podemos dar atributos (ou propriedades), isto é, características a um objeto,
# acessando o objeto.

# Acesso da propriedade nome de p1
# p1.nome = 'João'
# OBS.: não se recomenda criar atributos de um objeto dessa forma. O correto é
# definir os atributos na inicialização ou criar um método setter

print(p1.nome)  # Luiz
print(p1.idade)  # 25
p1.falar()
p1.comer('banana')
p1.get_ano_nascimento()
