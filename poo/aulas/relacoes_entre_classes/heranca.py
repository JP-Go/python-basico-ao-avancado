from classes import Aluno, ClienteH, ClienteVIP, Pessoa

c1 = ClienteH('Roberto', 38)
a1 = Aluno('Maria', 13)
p1 = Pessoa('João', 23)

print(c1.nome)
print(a1.nome)

c1.comprar()
a1.estudar()

c1.falar()
a1.falar()
p1.falar()

# c2 possui todos os métodos de ClienteH e Pessoa
c2 = ClienteVIP('Gerald', 'Houston', 34)
c2.falar_como_cliente()
c2.falar_como_pessoa()
c2.falar()
