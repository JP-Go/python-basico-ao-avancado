from dataclasses import dataclass, field, asdict

# Dataclass é um decorador que gera métodos os métodos
# __eq__, __init__ e __repr__ automaticamente, tornando mais fácil
# a criação de classes

# Documentação
# dataclass(cls=None, /, *, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False)
#     Returns the same class as was passed in, with dunder methods
#     added based on the fields defined in the class.
#
#     If init is true, an __init__() method is added to the class. If
#     repr is true, a __repr__() method is added. If order is true, rich
#     comparison dunder methods are added. If unsafe_hash is true, a
#     __hash__() method function is added. If frozen is true, fields may
#     not be assigned to after instance creation. If match_args is true,
#     the __match_args__ tuple is added. If kw_only is true, then by
#     default all fields are keyword-only. If slots is true, an
#     __slots__ attribute is added.


@dataclass
class Pessoa:
    nome: str
    # Field prove uma classe para esse atributo em vez de um atributo comum
    # repr = False indica que esse atributo não vai aparecer no repr
    # compare = False indica que esse atributo não vai ser usado para comparações
    sobrenome: str = field(repr=False)
    apelido: str = field(compare=False)

    # Método post init é executado após o init da dataclass
    # pode funcionar para inicializar atributos dependentes daqueles da classe
    def __post_init__(self):
        self.nome_completo = f"{self.nome} {self.sobrenome}"


# Definindo duas pessoas do mesmo nome
p1 = Pessoa(nome="Luis", sobrenome="Otávio", apelido="LO")
p2 = Pessoa(nome="Luis", sobrenome="Otávio", apelido="Luizão")
p3 = Pessoa(nome="João", sobrenome="Pedro", apelido="JP")
p4 = Pessoa(nome="Luis", sobrenome="Otévio", apelido="LO")

print(p1)
print(p2)
print(p3)

print(p3.nome_completo)

# p1 é igual p2 pois possuem o mesmo nome e sobrenome, mesmo que tenham apelidos diferentes
print(p1 == p2)
# p1 é diferente p4 pois possuem o mesmo nome mas sobrenome diferente, mesmo que tenham apelidos iguais
print(p1 == p4)

# Podemos usar o método asdict do módulo dataclasses para transformar uma classe para dicionário
print(asdict(p3))
