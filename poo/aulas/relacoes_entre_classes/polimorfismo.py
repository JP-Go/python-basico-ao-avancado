"""
Polimorfismo é o princípio da POO que permite que classes derivadas de uma mesma superclasse
tenham métodos iguais (de mesma assinatura) mas comportamentos diferentes;
Python só suporta o polimorfismo de sobreposição

Mesma assinatura = mesmo número e tipos de parâmetros
"""

from abc import ABC, abstractmethod


class A(ABC):

    @abstractmethod
    def fala(self, msg):
        pass


class B(A):

    def fala(self, msg):
        return print(f"B fala {msg}")


class C(A):

    def fala(self, msg):
        return print(f"C fala {msg}")
