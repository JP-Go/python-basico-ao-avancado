from endereco import Grupo

DECIMAIS = [10, 20, 12, 45]

grupos = [Grupo(x) for x in DECIMAIS]

ip_em_bytes = ".".join([grupo.valor_binario for grupo in grupos])
print(ip_em_bytes)
