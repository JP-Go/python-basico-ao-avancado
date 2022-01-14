# Classes exemplos para estudo de POO


## Classes de associação
class Escritor:
    """ Representa um escritor, a pessoa que escreve"""

    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    """ Representa uma caneta de uma marca qualquer"""

    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    def escrever(self):
        print("Caneta escrevendo")


class MaquinaDeEscrever:
    """ Representa uma máquina de escrever genérica"""

    def __init__(self):
        pass

    def escrever(self):
        print("Máquina escrevendo")


## Classes de agregação
class Produto:
    """ Representa um produto de uma loja com um valor e nome"""

    def __init__(self, nome: str, valor: float) -> None:
        self._nome = nome
        self._valor = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor: float):
        self._valor = float(valor)


class CarrinhoDeCompras:
    """ Representa um conjunto de produtos a serem comprados"""

    def __init__(self) -> None:
        self._produtos: list[Produto] = []

    def inserir_produto(self, produto: Produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        return sum(produto.valor for produto in self.produtos)

    def remover_ultimo_produto(self):
        self.produtos.pop()

    @property
    def produtos(self):
        return self._produtos

    @produtos.setter
    def produtos(self, produtos):
        self._produtos = produtos


## Classes de composição


class Endereco:

    def __init__(self, cidade, estado) -> None:
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} deletado')


class Cliente:
    """ Representa um cliente de uma loja"""

    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade
        self._enderecos = []  # Um cliente pode ter vários endereções

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, idade: int) -> None:
        self._idade = idade

    @property
    def enderecos(self) -> list[Endereco]:
        return self._enderecos

    def inserir_endereco(self, cidade, estado) -> None:
        self.enderecos.append(Endereco(cidade, estado))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f"Cliente {self.nome} deletado")


# Classes de herança
