class NumberConverter:
    """Class that defines a tool to convert number from decimal to byte and vice-versa"""

    @staticmethod
    def convert_int_to_byte(integer: int) -> str:
        """Converts a decimal integer to its byte corresponding number"""
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
        """Converts a byte number to its decimal integer number"""
        byte = byte.replace(".", "")
        if not isinstance(byte, str):
            raise ValueError("Value has to be an string")
        if not byte.isnumeric():
            raise ValueError("Value has to be a string composed of ones and zeroes")
        return int(byte, 2)


class IpConverter:
    """Class desingned to convert ip addresses from one representation to another"""

    @staticmethod
    def to_byte_repr(ip: str) -> str:
        """Converts a ipv4 ip address from its decimal representation to byte representation"""
        convert_to_byte = NumberConverter().convert_int_to_byte
        byte_groups = [convert_to_byte(int(group)) for group in ip.split(".")]
        return ".".join(byte_groups)

    @staticmethod
    def to_decimal_repr(ip: str) -> str:
        """Converts a ipv4 ip from its byte representation to decimal representation"""
        decimal_groups = [str(int(group, 2)) for group in ip.split(".")]
        return ".".join(decimal_groups)
