FIZZ = "fizz"
BUZZ = "buzz"


def greet(greeting: str, name: str) -> None:
    """Sauda o usuário 'name' com saudação 'gretting' no stdout"""
    print(greeting, name)
    return


# Type alias for any type of number
number = int and float


def sum_3(num1: number, num2: number, num3: number) -> None:
    """Soma três números e os imprime no stdout"""
    print(num1 + num2 + num3)
    return


def increase_by_percentage(value: number, percentage: number) -> number:
    """Retorna 'value' aumentado por um percentual 'percentage'"""
    return value * (1 + (percentage * 0.01))


def fizz_buzz(iter_number: int) -> str:
    """
    Testa se 'iter_number' é divisível por 2 ou 5 e retorna 'fizz' se
    'iter_number' é divissível somente por 2, 'buzz' se 'iter_number' é divisível somente por 5
    e 'fizzbuzz' se for divisível por ambos. Caso contrário, retorna 'iter_num'
    """
    result = ""
    if iter_number % 3 == 0:
        result += FIZZ
    if iter_number % 5 == 0:
        result += BUZZ
    return result if result else str(iter_number)


def main():
    greet("oi", "maurício")
    sum_3(1, 2, 3)
    print(increase_by_percentage(100, 10))
    for i in range(1, 16):
        print(fizz_buzz(i))


if __name__ == "__main__":
    main()
