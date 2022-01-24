"""
Metodos mágicos são métodos de uma classe envolvidos por '__' (dunder) que adicionam funcionalidades
nativas de python na classe definida.
"""


class A:

    # Define a funcionalidade de criação
    def __new__(cls):
        # Obs: Toda classe herda da classe object, por isso é possível chamar o "super"
        return super().__new__(cls)

    # define a funcionalidade de inicialização
    def __init__(self) -> None:
        print("I'm __INIT__, ini't?")

    # __new__ + __init__ é equivalente ao construtor de outras linguagens

    # define a funcionaliade de representação em string (usado para máquina)
    def __repr__(self) -> str:
        return "I'm of class A"

    # define a funcionaliade de representação em string (usado para humanos)
    # chamada quando usamos a função print, por exemplo
    def __str__(self) -> str:
        return "<class A>"


a1 = A()
print(a1)
