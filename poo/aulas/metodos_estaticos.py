from random import randint


class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    def __repr__(self) -> str:
        return f"Nome: {self.nome}; Idade: {self.idade}"

    # Método que pertence somente a classe Pessoa, e não aos objetos
    # Esse método de criar um objeto da classe pessoa só faz sentido
    # para a classe e não para o objeto
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        # cls representa a classe
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)  # chamada da classe, criando um novo objeto

    # Método estático: não precisa nem da instancia nem da classe
    # é independente de qualquer instancia da classe ou dela mesma
    # mas está na classe por organização
    @staticmethod
    def gera_id():
        return randint(10000, 19999)


p1 = Pessoa('Raimundo', 15)
print(p1.gera_id())  # gera um id
print(Pessoa.gera_id())  # gera outro id
