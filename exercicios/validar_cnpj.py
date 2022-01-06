# Title: CNPJ Validator in python
# Description: This program checks if a given brazilian CNPJ is valid by
# checking its digits
# Author: João Pedro Gomes (github: https://www.github.com/JP-Go)

FRST_DIGIT_VALIDATORS = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
SEC_DIGIT_VALIDATORS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
CNPJ_LEN = 14  # The length of a tipical brazilian CNPJ


def normalize_digit(generator_num: int) -> int:
    """ Normalizes a CNPJ validation digit to be between 0 or 9 and returns it"""
    trial_digit = 11 - (generator_num % 11)
    return trial_digit if trial_digit <= 9 else 0


def generate_validation_digit(non_validation_digits: list[int],
                              validators: list[int]) -> int:
    """ Generates a validation digit given the digits of a CNPJ and a validation sequence and returns it"""
    generator_num = sum(
        [x * y for x, y in zip(non_validation_digits, validators)])
    return normalize_digit(generator_num)


def parse_cnpj(cnpj: str) -> list[int]:
    """ Parses a suposelly valid cnpj string, removing non digit characters and returns its digits"""
    return [int(digit) for digit in cnpj if digit.isdigit()]


def get_non_validation_digits(cnpj_digits: list[int]) -> list[int]:
    """ Returns all non validation digits of a CNPJ from a list of CNPJ digits"""
    return cnpj_digits[:-2]


def validate_cnpj(cnpj: str) -> bool:
    """ Validates a given CNPJ. Returns True if the CNPJ is valid, and False otherwise"""
    cnpj_digits = parse_cnpj(cnpj)
    if len(cnpj_digits) != CNPJ_LEN:
        return False
    new_cnpj_digits = get_non_validation_digits(cnpj_digits)
    first_validation_digit = generate_validation_digit(new_cnpj_digits,
                                                       FRST_DIGIT_VALIDATORS)
    new_cnpj_digits.append(first_validation_digit)
    second_validation_digit = generate_validation_digit(
        new_cnpj_digits, SEC_DIGIT_VALIDATORS)
    new_cnpj_digits.append(second_validation_digit)
    return cnpj_digits == new_cnpj_digits


def welcome() -> None:
    """ Prints the welcome message """
    print("Welcome to CNPJ validator")
    print("To start provide a brazilian CNPJ to test if it is a valid CNPJ")


def main():
    welcome()
    while True:
        to_validate = input(
            "Type a CNPJ, (or type 'exit' to close the program) and press enter: "
        )
        if to_validate == "exit":
            print("Goodbye!")
            break
        if validate_cnpj(to_validate):
            print("That is a valid CNPJ")
            continue
        print("Not a valid CNPJ")


if __name__ == "__main__":
    main()
