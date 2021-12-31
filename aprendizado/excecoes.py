""" Podemos tratar exceções com blocos try/except"""

try:
    print(1 / 0)
except ZeroDivisionError as ne:  # É bom sempre usar a exceção nomeada
    print("Erro. Fale com o desenvolvedor", ne)
else:
    print("Executa se não ouver nenhum erro")
finally:
    print(" Executa independente de qualquer coisa")
