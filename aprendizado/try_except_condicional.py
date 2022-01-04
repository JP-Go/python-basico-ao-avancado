def convert_to_num(input: str) -> int or float or None:
    try:
        return int(input)
    except ValueError:
        try:
            return float(input)
        except ValueError:
            return None


while True:
    num = convert_to_num(input("Digite um número: "))
    if num is None:
        print("O valor dado não pode ser interpretado como número")
    print(f"{num} x 5 = {num*5}")
