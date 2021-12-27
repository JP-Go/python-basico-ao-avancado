from itertools import zip_longest


def main():

    lista_a = [1, 2, 3, 4, 5]
    lista_b = [1, 2, 3, 4]
    lista_c = [1, 2, 3, 4, 5, 6, 7, 8]
    lista_d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def sum_lists(*args):
        """ Usando zip e *args para desempacotar as listas passadas"""
        return [sum(values) for values in zip(*args)]

    def sum_lists_longest(*args, **kwargs):
        return [sum(values) for values in zip_longest(*args, **kwargs)]

    # Solução mais óbvia e pouco flexível
    lista_soma = [a + b for a, b in zip(lista_a, lista_b)]

    print(f"Solução um: {lista_soma}")
    print(
        f"Solução dois (várias listas): {sum_lists(lista_a, lista_b, lista_c, lista_d)}"
    )
    print(
        "Solução três (várias listas, zip_longest):",
        f"{sum_lists_longest(lista_a, lista_b, lista_c, lista_d,fillvalue=0)}")


if __name__ == "__main__":
    main()
