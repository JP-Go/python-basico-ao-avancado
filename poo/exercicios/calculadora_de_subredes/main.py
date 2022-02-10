from converter import NumberConverter


class CalcIpv4:
    """Classe que, dado um ip base e uma máscara de ip no protocolo Ipv4, calcula informações sobre a rede Ipv4"""

    def __init__(self, ip: str, mascara: str):
        self.ip = ip
        self.mascara = mascara
        self.numero_de_ips = self.calcular_numero_de_ips()

    def calcular_ip_de_rede(self):
        pass

    def calcular_ip_de_broadcast(self):
        pass

    def calcular_numero_de_ips(self):
        pass

    def calcula_primeiro_ip(self):
        pass

    def calcula_ultimo_ip(self):
        pass


print(NumberConverter.convert_byte_to_int("0000.0000.0000.0001"))
