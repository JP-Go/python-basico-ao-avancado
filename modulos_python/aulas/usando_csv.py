import csv

# csv.reader(arquivo): retorna um iterador com listas que representam as linhas o arquivo csv
# csv.DictReader(arquivo): retorna um iterador com dicionários que representam as linhas do arquivo csv
# IMPORTANTE: esses métodos só funcionam enquanto o arquivo estiver aberto.
with open('aulas/clientes.csv', 'r') as file:
    # dados = csv.reader(file)
    # next(dados)  # pula uma iteração do iterador (cabeçalho da tabela)
    # for linha in dados:
    #     print(linha)
    # Transformando os dados em uma lista para poder acessar os dados fora do ctxmngr
    dados = [x for x in csv.DictReader(file)]
    for linha in dados:
        print(linha['Nome'])

print(dados)

with open('aulas/output/clientes2.csv', 'w') as file:
    # csv.writer: cria um escreverdor em um arquivo e retorna os dados escritos
    # delimiter: delimitador das colunas
    # quotechar: caractere que representa uma aspa
    # quoting: determina se o arquivo vai envolver os dados das celulas em aspas
    writer = csv.writer(
        file,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL,
    )
    # csv.writer.writerow([celula1,celula2,etc...]):
    # recebe uma lista com os dados a escrever em uma linha da tabela csv e
    # escreve ela na ordem.
    cabecalho = list(dados[0].keys())
    writer.writerow(cabecalho)
    for i, dado in enumerate(dados):
        print("Escrevendo", *dado.values(), f'na linha {i} ')
        writer.writerow([i, *dado.values()])
