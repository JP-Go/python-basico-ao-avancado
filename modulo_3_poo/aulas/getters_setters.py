def number_from_str(string: str):
    digits_and_decimal_point = [
        char for char in string if char.isdigit() or char == ','
    ]
    return float(''.join(digits_and_decimal_point).replace(',', '.'))


class Produto:

    def __init__(self, nome: str, preco) -> None:
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual: float) -> None:
        self.preco = self.preco * (1 - (percentual / 100))

    # Define um getter par a propriedade preco. Essa função funciona como atributo
    @property
    def preco(self):
        return self._preco

    # Define um setter para preco
    @preco.setter
    def preco(self, valor):
        if (isinstance(valor, str)):
            valor = number_from_str(valor)
        self._preco = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()


p1 = Produto('camisa', 50)
p1.desconto(10)

p2 = Produto('CHINELO', 'R$ 20,00')
p2.desconto(10)

print(p1.nome, p1.preco)
print(p2.nome, p2.preco)
