def falar_oi(nome):
    return f"Oi {nome}!"


def dar_tchau(nome, despedida):
    return f"{despedida} {nome}!"


def executar(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


print(executar(falar_oi, "Roberto"))
print(executar(dar_tchau, "Luiz", despedida="Ciao"))
