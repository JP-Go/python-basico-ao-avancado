# A função open(path,mode) abre um arquivo em 'path' no modo 'mode',
# retorna uma handle para o arquivo
# Ver documentação em https://docs.python.org/3/library/functions.html#open

# Abrindo de forma "ingênua"
# modo w+: w -> lê e (sobre)escreve; + -> cria se não existir
file = open("output/ingenuo.txt", 'w+')

# file.write(string) escreve a string no arquivo
linha_3 = "Linha 3"
file.write("Linha 1\nLinha 2\n")
file.write(linha_3)

# file.seek(off,col) Move o 'cursor' para a posição off,col do arquivo em relação ao começo do arquivo
file.seek(0, 0)

# file.read() retorna todo o conteúdo do arquivo
# file.readline() retorna uma linha do arquivo em leitura sequencial
# file.readlines() retorna uma lista com todas as linhas do arquivo
print(file.read())

# file é iterável
file.seek(0, 0)
for line in file:
    print(line, end='')

# SEMPRE FECHE O ARQUIVO, OU SOFRA AS CONSEQUÊNCIAS
file.close()
print()

# Maneira pythonica: Utilizando gerenciadores de contexto
# O gerenciador de contexto vai fechar o arquivo automaticamente
with open("output/pythonico.txt", 'w+') as file:
    for i in range(1, 4):
        file.write(f'Linha {i}\n')
    file.seek(0, 0)
    print(file.read())
