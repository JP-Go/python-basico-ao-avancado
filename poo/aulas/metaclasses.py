"""
Em python tudo é um objeto, inclusive classes. Metaclasse é uma classe que cria outra classe
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == "A":
            return type.__new__(mcs, name, bases, namespace)

        # Força as classes filhas de 'A' a possuirem um método b_fala
        if "b_fala" not in namespace:
            raise AttributeError(f"{name} needs to implement b_fala method")
        else:
            if not callable(namespace["b_fala"]):
                raise AttributeError(
                    f"{name} needs to implement b_fala method as a method, not a attribute"
                )

        # Impede que o atributo attr_classe seja sobreescrito por classes filhas:
        if "attr_classe" in namespace:
            del namespace["attr_classe"]
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_classe = "Valor A"

    def falar(self):
        # type: ignore
        self.b_fala()


class B(A):
    attr_classe = "Valor B"

    def b_fala(self):
        print("oi")

    pass


b = B()
print(b.attr_classe)
