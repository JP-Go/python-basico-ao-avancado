# Como implementar um iterator
# Vamos criar uma lista personalizada
class MinhaLista:

    def __init__(self):
        # Passo 1: dar a essa instância um local para guardar dados
        self.__items = []
        # Passo 2: dar à instância dessa classe um contador para implementar
        # o iterador
        self.__index = 0

    def add(self, value):
        self.__items.append(value)

    # Passo 3: criar o método abaixo que deve retornar uma instância
    # de uma classe iteradora
    def __iter__(self):
        return self

    # Passo 4: criar o método abaixo para definir qual o próximo item que
    # deve ser retornado a cada iteração. Deve retornar o item e levantar
    # uma exceção do tip StopIteration quando a iteração deve ser finalizada
    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    # Opcional: getitem -> implementa indexação de itens
    def __getitem__(self, index):
        return self.__items[index]

    # Opcional: setitem -> implementa atribuição por índice
    def __setitem__(self, index, value):
        if index >= len(self.__items):
            self.__items.append(value)
            return

        self.__items[index] = value

    # Opcional: delitem -> implementa deleção por índice
    def __delitem__(self, index):
        del self.__items[index]

    def __str__(self):
        return f"{self.__class__.__name__} {self.__items}"


if __name__ == "__main__":
    lista = MinhaLista()
    lista.add("luis")
    lista.add("maria")

    for valor in lista:
        print(valor)

    lista[4] = "ricardo"
    print(lista)
