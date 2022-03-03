import subprocess

# subprocess.run(args_list:list[str]):
# opções:
#   stdout=True -> Printa o resultado do comando no stdout se True
#   capture_True=False -> Redireciona a saída do processo e manda para o atributo stdout de proc se True
#   text = False -> Converte a saida capturada do stdout para texto
proc = subprocess.run(["ping", "localhost", "-c", "4"], capture_output=True, text=True)
print("Erro?", proc.stderr)  # Dados mandados para o stderr em caso de erro
print("Saida", proc.stdout)  # Saida mandada para o stdout
print(
    "Código de saida", proc.returncode
)  # Código de saida. 0 se o processo foi executado com sucesso
print("Argumentos", proc.args)  # Argumento passados para o proc
