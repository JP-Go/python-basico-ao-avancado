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
        byte = byte.replace(".", "")
        print(byte)
        if not isinstance(byte, str):
            raise ValueError("Value has to be an string")
        if not byte.isnumeric():
            raise ValueError("Value has to be a string composed of ones and zeroes")
        return int(byte, 2)


class IpRepresentationConverter:
    @staticmethod
    def to_byte_representation(ip: str) -> str:
        convert_to_byte = NumberConverter().convert_int_to_byte
        byte_groups = [convert_to_byte(int(group)) for group in ip.split(".")]
        return ".".join(byte_groups)

    @staticmethod
    def to_decimal_representation(ip: str) -> str:
        decimal_groups = [str(int(group)) for group in ip.split(".")]
        return ".".join(decimal_groups)
