#!/usr/bin/env python3
from enum import Enum, auto

# Usar enums quando existe uma decisão com um numero limitado de escolhas


# Criando um enum:
class DirectionsEnum(Enum):
    right = auto()  # auto() dá um valor automático para o membro do Enum
    left = auto()
    up = auto()
    down = auto()


def move(direction: DirectionsEnum):
    if not isinstance(direction, DirectionsEnum):
        raise ValueError()
    return f"Moving {direction.name} ({direction.value})"


if __name__ == "__main__":
    print(move(DirectionsEnum.right))
    print(move(DirectionsEnum.left))
    print(move(DirectionsEnum.up))
    print(move(DirectionsEnum.down))

    print()

    # O enum pode ser iterado
    for direction in DirectionsEnum:
        print(direction)
