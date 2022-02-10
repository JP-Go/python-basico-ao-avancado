from abc import ABC, abstractmethod

# Classe abstrata : Que cria um molde para uma classe mas não é instanciável
# class A(ABC):
#     @abstractmethod
#     def falar(self):
#         pass
# class B(A):
#     falar deve ser definido em B, se B herda de A.
#     def falar(self):
#         print('Falando .. B ..')


class Conta(ABC):

    def __init__(self, agencia, conta, saldo) -> None:
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor dado não é um número')
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor dado não é um número')
        self.saldo += valor
        self.get_detalhes()

    @abstractmethod
    def sacar(self, valor):
        pass

    def get_detalhes(self):
        print(
            f'Agencia: {self.agencia} Conta: {self.conta} Saldo: {self.saldo}')


# Conta poupança deve implementar o método sacar
class ContaPoupanca(Conta):

    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente.")
            return
        self.saldo -= valor
        self.get_detalhes()


# Conta corrente deve implementar o método sacar
class ContaCorrente(Conta):

    def __init__(self, agencia, conta, saldo, limite=100) -> None:
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print("Saldo insuficiente.")
            return
        self.saldo -= valor
        self.get_detalhes()


cp = ContaPoupanca(1, 7012, 0)

cp.depositar(100)
cp.sacar(10)
cp.sacar(90)
cp.sacar(1)

print("################################")
cc = ContaCorrente(agencia=1, conta=5050, saldo=0, limite=200)

cc.sacar(100)
cc.depositar(300)
