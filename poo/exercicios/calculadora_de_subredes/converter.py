class NumberConverter:
    @staticmethod
    def convert_int_to_byte(integer: int) -> str:
        if not isinstance(integer, int):
            raise ValueError("Value has to be an integer")
        if integer < 0:
            raise ValueError("Value cannot be negative")
        byte = bin(integer)[2:]
        if len(byte) < 8:
            return f"{byte:>08}"
        return byte

    @staticmethod
    def convert_byte_to_int(byte: str) -> int:
        if not isinstance(byte, str):
            raise ValueError("Value has to be an string")
        if not byte.isnumeric():
            raise ValueError("Value has to be a string composed of ones and zeroes")
        return int(byte, 2)
