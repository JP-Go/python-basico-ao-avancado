def parse_cnpj(cnpj: str) -> list[int]:
    """ Parses a suposelly valid cnpj string, removing non digit characters and returns its digits"""
    return [int(digit) for digit in cnpj if digit.isdigit()]


def get_non_validation_digits(cnpj_digits: list[int]) -> list[int]:
    """ Returns all non validation digits of a CNPJ from a list of CNPJ digits"""
    return cnpj_digits[:-2]
