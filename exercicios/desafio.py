nome = "João Pedro"
idade = 23
ano_atual = 2021
ano_de_nascimento = 1998
altura = 1.62
peso = 50.0

imc = peso / (altura * altura)
idade = ano_atual - ano_de_nascimento

print(f"{nome} tem {idade} anos, {altura:.2f} de altura e pesa {peso:.2f}kg.")
print(f"O imc de {nome} é {imc:.2f}.")
print(f"{nome} nasceu em {ano_de_nascimento}.")
