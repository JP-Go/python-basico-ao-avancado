#!/usr/bin/env python3
TESTE = [("Produto 1", 20), ("Produto 2", 10), ("Produto 3", 20)]

CARRINHO = [
    ("Produto 1", 29.99),
    ("Produto 2", 19.99),
    ("Produto 3", 25.99),
    ("Produto 4", 49.99),
    ("Produto 5", 9.99),
    ("Produto 6", 59.99),
]
number = int or float
produto = tuple[str, number]
carrinho = list[produto]


def calcular_total(carrinho: carrinho) -> number:
    return sum([preco for _, preco in carrinho])


def main():
    print(calcular_total(TESTE))
    print(calcular_total(CARRINHO))
    pass


if __name__ == "__main__":
    main()
