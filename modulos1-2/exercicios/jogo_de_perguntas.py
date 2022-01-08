PERGUNTAS = {
    "Pergunta 1": {
        "enunciado": "Quanto é 2 + 2?",
        "resposta": "a",
        "alternativas": {"a": "4", "b": "5", "c": "42"},
    },
    "Pergunta 2": {
        "enunciado": "Quanto é 3 + 2?",
        "resposta": "b",
        "alternativas": {"a": "4", "b": "5", "c": "42"},
    },
    "Pergunta 3": {
        "enunciado": "Qual o sentido da vida?",
        "resposta": "c",
        "alternativas": {"a": "4", "b": "5", "c": "42"},
    },
}

Alternativas = dict[str, str]
Pergunta = dict[str, str and Alternativas]
Pergunta_List = dict[str, Pergunta]


def mostrar_alternativas(alternativas: Alternativas):
    if not alternativas:
        raise Exception("[Erro] sem alternativas para essa pergunta")
    for alternativa, valor in alternativas.items():
        print(f"{alternativa}) {valor}")


def perguntar(enunciado: str, alternativas: Alternativas, resposta: str) -> bool:
    """
    Realiza uma pergunta e retorna True se o usuário acertar a resposta
    """
    print(enunciado)
    alternativas_handle = ",".join(alternativas.keys())
    print(f"Digite a alternativa da sua resposta ({alternativas_handle}): ")
    mostrar_alternativas(alternativas)
    resposta_usuario = input("Resposta: ")
    is_resposta_valida = resposta_usuario in alternativas.keys()
    while not (resposta_usuario and is_resposta_valida):
        print(f"Por favor digite uma resposta válida ({alternativas_handle})")
        resposta_usuario = input("Resposta: ")
        is_resposta_valida = resposta_usuario in alternativas.keys()

    return resposta_usuario.strip() == resposta


def play():
    respostas_corretas = 0
    for pergunta in PERGUNTAS.values():
        enunciado, resposta, alternativas = (
            pergunta["enunciado"],
            pergunta["resposta"],
            pergunta["alternativas"],
        )
        resposta = perguntar(enunciado, alternativas, resposta)
        if not resposta:
            print("Você errou, que pena!")
        else:
            print("Você acertou!")
            respostas_corretas += 1
        print()

    print(f"Você acertou {respostas_corretas} de {len(PERGUNTAS)} perguntas")


if __name__ == "__main__":
    play()
    while input("Você quer jogar novamente?[s|N]: ") == "s":
        play()
