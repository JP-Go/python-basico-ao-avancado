def validate_cpf(cpf: str) -> None:
    digits = cpf.replace(".", "").replace("-", "")
    first_verifier = calcular_primeiro_verificador(digits)
    second_verifier = calcular_segundo_verificador(digits)
    calculated_verifiers = f"{first_verifier}{second_verifier}"
    is_valid = calculated_verifiers == digits[-2:]

    print("Válido" if is_valid else "Inválido")


def calculate_verifier_digit(digits: str, regresor: int) -> int:
    end_idx = regresor - 1
    return sum(int(digit) * (regresor - i) for i, digit in enumerate(digits[:end_idx]))


def calcular_primeiro_verificador(digits: str) -> int:
    acc = calculate_verifier_digit(digits, 10)
    return (11 - (acc % 11)) if ((11 - (acc % 11)) <= 9) else 0


def calcular_segundo_verificador(digits: str) -> int:
    acc = calculate_verifier_digit(digits, 11)
    return (11 - (acc % 11)) if ((11 - (acc % 11)) <= 9) else 0


if __name__ == "__main__":
    validate_cpf("168.995.350-09")  # True
    validate_cpf("162.285.576-02")  # True
    validate_cpf("142.285.576-02")  # False
