class A:
    # Disponível para todas as instâncias da classe
    vc = 1234


a1 = A()
a2 = A()

print(a1.vc)
print(a2.vc)
print(A.vc)

# Altera o valor de vc para todas as instâncias
A.vc = 321

print(a1.vc)
print(a2.vc)
print(A.vc)

# Cria o valor vc para a1, somente. Não altera o valor vc
a1.vc = 222

print(a1.vc)
print(a2.vc)
print(A.vc)
