class Grupo:
    def __init__(self, valor_decimal: int):
        self.valor_decimal: int = valor_decimal
        self.valor_binario: str = Grupo.converter_para_binario(valor_decimal)

    @staticmethod
    def converter_para_binario(valor: int) -> str:
        return f"{bin(valor)[2:]:>08}"

    @staticmethod
    def converter_para_decimal(valor: str) -> int:
        return int(valor, 2)


class EnderecoDeIP:
    def __init__(self) -> None:
        self.grupos: list[Grupo] = []

    def adicionar_grupo(self, grupo: Grupo) -> None:
        self.grupos.append(grupo)

    def calcular_hosts(self, mask: int) -> int:
        bits = 8 * len(self.grupos)
        bits_desmacarados = bits - mask
        return 2 ** bits_desmacarados - 2

    def obter_ip(self):
        ip_bruto = "".join([grupo.valor_binario for grupo in self.grupos])
