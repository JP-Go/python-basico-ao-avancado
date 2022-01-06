import validator_constants as validators


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


def generate_cnpj_digits(base_digits: list[int]) -> list[int]:
    cnpj_digits = base_digits
    first_validation_digit = generate_validation_digit(
        cnpj_digits, validators.FRST_DIGIT_VALIDATORS)
    cnpj_digits.append(first_validation_digit)
    second_validation_digit = generate_validation_digit(
        cnpj_digits, validators.SEC_DIGIT_VALIDATORS)
    cnpj_digits.append(second_validation_digit)
    return cnpj_digits
