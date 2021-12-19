import re


class NotIntException(Exception):
    """Exception raised if a given value is not a integer"""

    def __init__(self, message="Valor dado não é um inteiro"):
        self.message = message
        super().__init__(self.message)


class InvalidHourException(Exception):
    """Exception raised if a given value is greater than 24 and less than 0"""

    def __init__(
        self,
        hour,
        message="Valor dado não é uma hora válida (não é inteiro > 0 e < 24)",
    ):

        if not hour:
            self.message = message
        self.message = (
            f"{hour} não é uma hora válida "
            "(hora deve ser inteiro maior que 0 e menor que 24) "
        )
        super().__init__(self.message)


def is_int(arg: str) -> bool:
    return re.match("[-+]?\d+$", arg) is not None


def is_float(arg: str) -> bool:
    return re.match("[-+]?\d+\.\d+$", arg) is not None


def convert_to_int(input: str) -> int:
    if not is_int(input):
        raise NotIntException()
    return int(input)


def ex1():
    """
    Função que determina se o número dado é impar ou par
    retorna uma string dizendo se o número é par
    """
    user_input = input("Digite um número inteiro: ")
    num = convert_to_int(user_input)
    print(f"{num} é {'par' if num % 2 == 0 else 'impar'}")


def greet(hour: int) -> str:
    """
    Função que retorna um cumprimento de acordo com a hora do dia
    """
    is_morning = hour in range(0, 12)
    is_afternoon = hour in range(12, 18)
    if is_morning:
        return "Bom dia!"
    if is_afternoon:
        return "Boa tarde!"
    return "Boa Noite!"


def ex2():
    """
    Função que um cumprimenta o usuário de acordo com a hora do dia
    """
    user_input = input("Que horas são? ")
    hour = convert_to_int(user_input)
    if not (0 < hour < 24):
        raise InvalidHourException(hour)
    print(greet(hour))


def classify_name_length(length: int) -> str:
    if length <= 4:
        return "Seu nome é curto"
    if length <= 6:
        return "Seu nome é normal."
    return "Seu nome muito grande"


def ex3():
    """
    Função que classifica o tamanho do nome do usuário
    """
    nome = input("Qual seu nome? ").strip()
    print(classify_name_length(len(nome)))


def main():
    # ex1()
    # ex2()
    ex3()


if __name__ == "__main__":
    main()
