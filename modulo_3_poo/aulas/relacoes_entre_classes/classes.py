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


class Pessoa:

    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print('Falando')


class ClienteH(Pessoa):

    def comprar(self):
        print('Comprando')

    def falar(self):
        print('Em cliente')


class ClienteVIP(ClienteH):

    def __init__(self, nome: str, sobrenome: str, idade: int):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome

    # Sobrepõe o método falar de Pessoa()
    def falar(self):
        print(f"{self.nome} {self.sobrenome} está falando vip-mente")

    def falar_como_cliente(self):
        super().falar()

    def falar_como_pessoa(self):
        # Chamar o método de uma classe dessa forma exige que passemos a instância
        Pessoa.falar(self)


class Aluno(Pessoa):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def estudar(self):
        print('Estudando')


# Classe mixin: Adiciona uma funcionalidade a uma classe, funcionalidade essa
# não relacionada com a classe
class LogMixin:

    @staticmethod
    def write(msg):
        with open('aulas/relacoes_entre_classes/output/log.log', 'a+') as file:
            file.write(msg)
            file.write('\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')


# Classes de herança múltipla
class Eletronico:

    def __init__(self, nome) -> None:
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            return
        self._ligado = False


class SmartPhone(Eletronico, LogMixin):

    def __init__(self, nome) -> None:
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            error = f"{self._nome} não está ligado"
            print(error)
            self.log_error(error)
            return
        if self._conectado:
            error = f"{self._nome} já está conectado"
            print(error)
            self.log_info(error)
            return
        print(f"{self._nome} conectou")
        self._conectado = True

    def desconectar(self):
        if not self._ligado:
            error = f"{self._nome} não está ligado"
            print(error)
            self.log_error(error)
            return
        if not self._conectado:
            info = f"{self._nome} já está desconectado"
            print(info)
            self.log_info(info)
            return
        self._conectado = False
