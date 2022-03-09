from typing import Any
from collections import deque

"""
Pilha (stack): Uma pilha é uma estrutura de dados que armazena itens e a interação com a coleção de 
itens segue o princípio UEPS (Último que entra, primeiro que sai -- LIFO). 
Fila (queue): Uma fila é uma estrutura de dados que armazena itens e a interação com a coleção de 
itens segue o princípio PEPS (Primeiro que entra, primeiro que sai -- FIFO).
"""


# Vamos implementar uma pilha
class Stack:
    def __init__(self) -> None:
        self._items = []

    @property
    def items(self) -> Any:
        """Acessor dos items da pilha"""
        return self._items

    @items.setter
    def items(self, value) -> None:
        self._items = value

    def add(self, item: Any) -> None:
        self.items.append(item)

    def pop(self) -> Any:
        return self.items.pop()

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({','.join(str(x) for x in  self.items)}) "


# Implementar agora uma fila
class Queue:
    def __init__(self) -> None:
        self._items = []

    @property
    def items(self) -> Any:
        """Acessor dos items da pilha"""
        return self._items

    @items.setter
    def items(self, value) -> None:
        self._items = value

    def add(self, item: Any) -> None:
        self.items.insert(0, item)

    def deque(self) -> Any:
        return self.items.pop(0)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({','.join(str(x) for x in  self.items)}) "


if __name__ == "__main__":
    fila = Queue()

    fila.add(1)
    fila.add(2)
    fila.add(3)

    print(f"{fila}")
    print(f"{fila.deque()}")
    print(f"{fila}")

    # Não é necessário implementar essas classes pois o módulo collections já as possui
    # Cria uma pilha e fila ao mesmo tempo
    outra_fila = deque()

    # Para usar como pilha, utilizar os métodos append, extend,pop,
    outra_fila.append(1)
    outra_fila.extend([2, 3])

    print(f"{outra_fila}")
    print(f"{outra_fila.pop()}")
    print(f"{outra_fila}")

    # Para usar como fila, utilizar os métodos appendleft,extendleft,popleft

    outra_fila.appendleft(3)

    print(f"{outra_fila}")
    print(f"{outra_fila.popleft()}")
    print(f"{outra_fila}")
