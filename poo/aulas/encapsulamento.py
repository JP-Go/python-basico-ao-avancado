# POO em python: Encapsulamento
# Convenções:
# _propriedade : convencionado privado (não mexer em 90% dos casos)
# __propriedade : convenvionado privado (quase impossível de acessar)


# Vamos fungir que temos uma base de dados:
class BaseDeDados:

    # "Construtor" em python
    def __init__(self) -> None:
        # __data está privado e não é acessível por instâncias da classe
        self.__data = {}

    # mas é possível criar um getter e setter para o atributo __data (não deve ser realmente necessário)
    @property
    def dados(self):
        return self.__data

    # E criar um setter (provavelmente é útil não definir setter)
    @dados.setter
    def dados(self, data):
        self.__data = data

    def inserir_cliente(self, cliente_id: int, nome: str) -> None:
        if 'clientes' not in self.__data:
            self.__data['clientes'] = {cliente_id: nome}
        else:
            self.__data['clientes'].update({cliente_id: nome})

    def listar_clientes(self):
        for id, nome in self.__data['clientes'].items():
            print(id, nome)

    def apagar_cliente(self, cliente_id: int) -> None:
        del self.__data['clientes'][cliente_id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Miranda')
bd.inserir_cliente(2, 'Rosa')
bd.inserir_cliente(3, 'Maria')
bd.apagar_cliente(2)
bd.listar_clientes()
try:
    print(bd.__data)
except:
    print("Data não faz parte de Base de dados")
bd.__data = "What?"
try:
    print(bd.__data)
    print("Agora sim. existe data")
except:
    print("Data não faz parte de Base de dados")
