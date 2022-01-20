# Herança de várias classes

from classes import SmartPhone


class A:

    def falar(self):
        print("falando em A")


class B:

    def falar(self):
        print("Falando em B")


class C(B, A):
    # Quando fazemos uma herança múltipla, o python procura nas classes o
    # método da esquerda para a direita na árvore de herança
    pass


class D(A, B):
    pass


c = C()
d = D()

c.falar()  # Chama o método falar de B
d.falar()  # Chama o método falar de A

fone = SmartPhone("Xiaomi")
fone.conectar()
fone.ligar()
fone.conectar()
fone.conectar()
