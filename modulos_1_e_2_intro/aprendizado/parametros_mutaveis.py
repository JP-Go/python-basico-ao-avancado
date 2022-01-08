# Quando utilizamos um parâmetro mutável, como uma lista, como valor padrão de
# um parâmetro em uma função, esse valor é criado na memória e a referência dela é passada cada vez que a função é executada sem este parâmetro.


# a chamada dessa função duas vezes resulta em uma lista só com os dois argumentos
def adicionar_clientes(clientes: list[str],
                       lista: list[str] = []) -> list[str]:
    lista.extend(clientes)
    return lista


clientes1 = adicionar_clientes(['Jão', 'Anitta'])
clientes2 = adicionar_clientes(['Rihanna', 'Beyonce'])

# Se printarmos clientes1 e clientes2 veremos que a mesma lista é exibida:
print(clientes1)
print(clientes2)

# Assim, podemos evitar esse comportamento ao Evitar utilizar parâmetros
# mutáveis como valor padrão de uma função, ou utilizar valores imutáveis
