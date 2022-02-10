# Relação de agregação: A classe depende de outra classe
from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()
p1 = Produto('Camisa', 50.00)
p2 = Produto('Iphone', 5000.00)
p3 = Produto('Caneca', 15.00)

for p in [p1, p2, p3]:
    print(f"Inserindo produto {p.nome}")
    carrinho.inserir_produto(p)
    carrinho.lista_produtos()

for p in [p1, p3]:
    carrinho.inserir_produto(p)

carrinho.lista_produtos()
print(carrinho.soma_total())
