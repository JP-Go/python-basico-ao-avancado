from converter import IpConverter


class CalcIpv4:
    """Classe that, given a base ip address and a mask ip address in the Ipv4 format, calculates info about the network"""

    def __init__(self, address: str, mask: str = None, prefix: int = None) -> None:
        self.address = address
        self.prefix = prefix
        self.mask = mask
        self.host_ip_bits = self.calculate_host_ip_bits()
        self.number_of_ips = self.calculate_number_of_ips()
        self.network_ip = self.calculate_network_ip()
        self.broadcast_ip = self.calculate_broadcast_ip()
        self.first_ip = self.calculate_first_available_ip()
        self.last_ip = self.calculate_last_available_ip()

    @property
    def mask(self):
        """The mask property."""
        return self._mask

    @mask.setter
    def mask(self, value):
        if not value:
            return
        self._mask = value
        self._prefix = self.calculate_prefix()

    @property
    def prefix(self):
        """The prefix property."""
        return self._prefix

    @prefix.setter
    def prefix(self, value):
        if not value:
            return
        if not 0 < value < 32:
            raise ValueError("Prefix has to be between 0 and 32")

        self._prefix = value
        self._mask = self.calculate_mask()

    def calculate_mask(self) -> str:
        bits = 8
        prefix_bits: str = "1" * self.prefix
        groups = [prefix_bits[i : i + bits] for i in range(0, self.prefix, bits)]
        mask = IpConverter.to_decimal_repr(".".join(groups).ljust(35, "0"))
        return mask

    def calculate_prefix(self) -> int:
        convert_to_byte = IpConverter.to_byte_repr
        prefix = len([i for i in convert_to_byte(self.mask) if i == "1"])
        return prefix

    def calculate_network_ip(self) -> str:
        host_ip_bits = self.calculate_host_ip_bits()
        addres_byte_repr = IpConverter.to_byte_repr(self.address)
        network_ip_byte_repr = addres_byte_repr[:-host_ip_bits].ljust(35, "0")
        network_ip = IpConverter.to_decimal_repr(network_ip_byte_repr)
        return network_ip

    def calculate_broadcast_ip(self) -> str:
        host_ip_bits = self.calculate_host_ip_bits()
        addres_byte_repr = IpConverter.to_byte_repr(self.address)
        broadcast_ip_byte_repr = addres_byte_repr[:-host_ip_bits].ljust(35, "1")
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
        print(f"IP: {self.address}/{self.prefix}")
        print(f"Máscara: { self.mask }/{self.prefix}")
        print(f"IP de rede: {self.network_ip}/{self.prefix}")
        print(f"IP de broadcast: {self.broadcast_ip}/{self.prefix}")
        print(f"Número de IPs: {self.number_of_ips}")
        print(f"Primeiro IP disponível: {self.first_ip}/{self.prefix}")
        print(f"Último IP disponível: {self.last_ip}/{self.prefix}")
