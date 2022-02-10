from converter import IpConverter

CASE_ONE_ADDRESS = "192.168.0.25"
CASE_ONE_MASK = "255.255.255.192"
CASE_TWO_ADDRESS = "10.20.12.45"
CASE_TWO_MASK = "255.255.255.192"


class CalcIpv4:
    """Classe that, given a base ip address and a mask ip address in the Ipv4 format, calculates info about the network"""

    def __init__(self, address: str, mask: str) -> None:
        self.address = address
        self.mask = mask
        self.host_ip_bits = self.calculate_host_ip_bits()
        self.mask_type = self.calculate_mask_type()
        self.number_of_ips = self.calculate_number_of_ips()
        self.network_ip = self.calculate_network_ip()
        self.broadcast_ip = self.calculate_broadcast_ip()
        self.first_ip = self.calculate_first_available_ip()
        self.last_ip = self.calculate_last_available_ip()

    def calculate_mask_type(self) -> int:
        convert_to_byte = IpConverter.to_byte_repr
        return len([i for i in convert_to_byte(self.mask) if i == "1"])

    def calculate_network_ip(self) -> str:
        host_ip_bits = self.calculate_host_ip_bits()
        addres_byte_repr = IpConverter.to_byte_repr(self.address)
        network_ip_byte_repr = addres_byte_repr[:-host_ip_bits] + host_ip_bits * "0"
        network_ip = IpConverter.to_decimal_repr(network_ip_byte_repr)
        return network_ip

    def calculate_broadcast_ip(self) -> str:
        host_ip_bits = self.calculate_host_ip_bits()
        addres_byte_repr = IpConverter.to_byte_repr(self.address)
        broadcast_ip_byte_repr = addres_byte_repr[:-host_ip_bits] + host_ip_bits * "1"
        broadcast_ip = IpConverter.to_decimal_repr(broadcast_ip_byte_repr)
        return broadcast_ip

    def calculate_number_of_ips(self) -> int:
        host_ip_bits = self.calculate_host_ip_bits()
        return 2 ** host_ip_bits - 2

    def calculate_first_available_ip(self) -> str | None:
        *base_network_ip, first_occupied_host = self.network_ip.split(".")
        first_available_host = str(int(first_occupied_host) + 1)
        return ".".join([*base_network_ip, first_available_host])

    def calculate_last_available_ip(self) -> str | None:
        *base_broadcast_ip, last_occupied_host = self.broadcast_ip.split(".")
        last_available_host = str(int(last_occupied_host) - 1)
        return ".".join([*base_broadcast_ip, last_available_host])

    def calculate_host_ip_bits(self) -> int:
        mask_repr = self.mask
        if len(self.mask) <= 15:
            mask_repr = IpConverter.to_byte_repr(self.mask)
        return len(list(filter(lambda x: x == "0", mask_repr)))

    def print_info(self):
        print(f"IP: {self.address}/{self.mask_type}")
        print(f"Máscara: { self.mask }/{self.mask_type}")
        print(f"IP de rede: {self.network_ip}/{self.mask_type}")
        print(f"IP de broadcast: {self.broadcast_ip}/{self.mask_type}")
        print(f"Número de IPs: {self.number_of_ips}")
        print(f"Primeiro IP disponível: {self.first_ip}/{self.mask_type}")
        print(f"Último IP disponível: {self.last_ip}/{self.mask_type}")


network1_info = CalcIpv4(address=CASE_ONE_ADDRESS, mask=CASE_ONE_MASK)
print("##### Net 1 ############")
network1_info.print_info()
network2_info = CalcIpv4(address=CASE_TWO_ADDRESS, mask=CASE_TWO_MASK)
print("##### Net 2 ############")
network2_info.print_info()
