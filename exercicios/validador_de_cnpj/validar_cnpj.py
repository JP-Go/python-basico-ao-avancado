# Title: CNPJ Validator in python
# Description: This program checks if a given brazilian CNPJ is valid by
# checking its digits
# Author: João Pedro Gomes (github: https://www.github.com/JP-Go)

import validator_constants as validators
from generators import generate_cnpj_digits
from parsers import parse_cnpj, get_non_validation_digits


def validate_cnpj(cnpj: str) -> bool:
    """ Validates a given CNPJ by checking its digits. Returns True if the CNPJ is valid, and False otherwise"""
    cnpj_digits = parse_cnpj(cnpj)
    if len(cnpj_digits) != validators.CNPJ_LEN:
        return False
    new_cnpj_digits = generate_cnpj_digits(
        get_non_validation_digits(cnpj_digits))
    return cnpj_digits == new_cnpj_digits


def main():
    print("Welcome to CNPJ validator")
    print("To start provide a brazilian CNPJ to test if it is a valid CNPJ")
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
