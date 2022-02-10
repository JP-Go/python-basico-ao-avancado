"""
No python, tudo é uma classe, então todo operador que atua nos primitivos de python são na verdade
métodos especiais da classe que representa aquele primitivo. Exemplo:
"""
# A classe int, que representa o primitivo int, possui um método de adição
print(1 + 1)


class Vec:
    """
    Representa um vetor com componentes paralelas aos eixos x e y no plano cartesiano
    """

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


p1 = Vec(0, 1)
p2 = Vec(1, 0)

# Esse código da erro pois não definimos o operador '+' na nossa classe
# print(p1 + p2)


class Vec2(Vec):

    # define o operado '+'
    def __add__(self, other):
        if not isinstance(other, Vec2 or Vec):
            raise ValueError(
                f"Can't sum vector and object of type {type(other).__name__}"
            )
        result = Vec2(self.x + other.x, self.y + other.y)
        return result

    # define o operado '-'
    def __sub__(self, other):
        if not isinstance(other, Vec2 or Vec):
            raise ValueError(
                f"Can't sum vector and object of type {type(other).__name__}"
            )
        return Vec2(self.x - other.x, self.y - other.y)

    # Não define operador (não é sobrecarga de método)
    def __repr__(self) -> str:
        return f"{self.__class__.__name__} -> ({ self.x},{ self.y })"

    # Define o operador '=='
    def __eq__(self, other) -> bool:
        if isinstance(other, Vec):
            other = Vec2.from_vec(other)
        if not isinstance(other, Vec2):
            return False
        return self.x == other.x and self.y == other.y

    @staticmethod
    def from_vec(vec: Vec):
        return Vec2(vec.x, vec.y)


p3 = Vec2.from_vec(p1)
p4 = Vec2.from_vec(p2)

print(p3 + p4)
print(p3 - p4)

print(p1 == p4)
print(p1 == p3)
