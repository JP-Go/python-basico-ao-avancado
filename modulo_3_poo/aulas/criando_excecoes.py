# Basta criar uma classe que herda de Exception
class TaErradoError(Exception):
    pass


def testar():
    raise TaErradoError('Tá errado!')


try:
    testar()
except TaErradoError as err:
    print(f"ERRO: {err}")
