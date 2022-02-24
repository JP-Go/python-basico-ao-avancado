import os
from zipfile import ZipFile

# ZipFile().write(caminho_arquivo[,nome_do_arquivo]): Inclui no arquivo zip o
# arquivo em caminho_arquivo com nome nome_do_arquivo

path = r'./aulas'
with ZipFile('./aulas/output/zipfile.zip', 'w') as zip:
    for arquivo in os.listdir(path):
        abspath = os.path.join(path, arquivo)
        if ('.py' not in arquivo) and (os.path.isfile(abspath)):
            print(f'Incluindo arquivo {arquivo} no zip')
            zip.write(abspath, arquivo)

with ZipFile('./aulas/output/zipfile.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

with ZipFile('./aulas/output/zipfile.zip', 'r') as zip:
    zip.extractall('./aulas/output/descompactado')
