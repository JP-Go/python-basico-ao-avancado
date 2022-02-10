# Funções decoradoras encapsulam as funções declaradas após elas
# Como se a função chamada após a ela fizesse parte de seu corpo


# Função decoradora: Recebe fun e a executa em seu corpo
def decor1(fun) -> None:
    fname = fun.__name__
    print(f'Executando a função {fname}')
    fun()
    print(f'executou {fname}')


@decor1
# Função decorada pela decor1
def falar_oi() -> None:
    print('oi')


# Uma utilidade: Passar atributos a uma função, por exemplo, uma mensagem
# Muito utilizado para conexão com bancos de dados
def passar_mensagem(fun):
    """ Essa função decoradora passa mensagem como argumento de uma outra função"""
    msg = "Mensagem a exibir"

    def slave():
        print(f"Passando mensagem para a função {fun.__name__}")
        print(f"Executando {fun.__name__}")
        fun(msg)

    return slave


@passar_mensagem
def exibir_mensagem(msg):
    print(msg)


exibir_mensagem()
