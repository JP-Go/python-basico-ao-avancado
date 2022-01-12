from classes import Cliente, Endereco

cliente1 = Cliente('Luiz', 21)
cliente1.inserir_endereco('Belo Horizonte', 'MG')

cliente2 = Cliente('Maria', 43)
cliente2.inserir_endereco('Salvador', 'BA')
cliente2.inserir_endereco('Rio de Janeiro', 'RJ')

cliente3 = Cliente('João', 18)
cliente3.inserir_endereco('São Paulo', 'SP')

for c in [cliente1, cliente2, cliente3]:
    print(f"{c.nome}")
    c.listar_enderecos()
    print()
print('###############################')
