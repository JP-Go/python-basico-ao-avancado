"""
O gerenciador de contexto do python cria uma variável durante a execução do
código no contexto. É muito útil para manipulação de arquivos. É possível
definir seu próprio gerenciador de contexto para outras funcionalidade. Para
arquivos, o gerenciador de contexto fecha o arquivo.
"""


class Arquivo:

    def __init__(self, arquivo, modo) -> None:
        self.arquivo = open(arquivo, modo)  # Abre um arquivo

    def write(self, text) -> None:
        self.write(text)

    # Define o que fazer quando o gerenciador de contexto é iniciado
    def __enter__(self):
        # Deve retornar algo para o context manager
        # Irá retornar o handle do arquivo para o context manager
        return self.arquivo

    # Define o que fazer quando o gerenciador de contexto é finalizado
    def __exit__(self, exc_type, exc_val, exc_tb):
        # exc_type, exc_val,exc_tbc são valores que serão definidos quando uma exceção
        # for capturada no gerenciador de contexto
        # exc_type informa o tipo da exceção, exc_val, o valor da exceção (normalmente o texto do erro)
        # e exc_tb é a próŕia exceção
        # Fecha o arquivo quando o contexto é acabado
        self.arquivo.close()

        # se essa função retornar True, o gerenciador de contexto não lança a exceção recebida no atributo
        # Caso contrário, ele lança a exceção


with Arquivo("./output/ctx_mgr_class.txt", 'w+') as file:
    file.write("Alguma coisa")

# Outra maneira de criar um context manager é utilzar o decorador para uma função que lidará com
# o gerenciamento do contexto:

from contextlib import contextmanager


@contextmanager
def abrir_arquivo(arquivo, modo):
    try:
        print("Abrindo arquivo")
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print("Fechando arquivo")
        arquivo.close()


with abrir_arquivo("./output/ctx_mgr_func.txt", 'w+') as file:
    file.write("Linha 1\n")
    file.write("Linha 2\n")
