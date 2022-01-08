""" Podemos tratar exceções com blocos try/except"""

try:
    print(1 / 0)
except ZeroDivisionError as ne:  # É bom sempre usar a exceção nomeada
    print("Erro. Fale com o desenvolvedor", ne)
else:
    print("Executa se não ouver nenhum erro")
finally:
    print(" Executa independente de qualquer coisa")

# Pode-se criar uma nova exeção


def divide(dividendo, divisor):
    if not divisor == 0:
        return dividendo / divisor
    raise ValueError("Division by zero")


print(divide(1, 2))
print(divide(1, 0))
