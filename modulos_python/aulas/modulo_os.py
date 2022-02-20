import os

# os.walk -> caminha por todos os diretórios recursivamente a partir de uma
# pasta base. Retorna uma 3-tupla para cada arquivo encontrado a partir da pasta base
# contendo o diretório do arquivo,uma lista de sub_diretorios de diretório, e uma lista de
# arquivos de diretório

# os.path -> utilitário para lidar com arquivos
# os.path.join -> junta dois caminhos, colocando / se necessário
# os.path.splitext -> retorna uma tupla contendo (raiz,extensão); divide o caminho de
# um arquivo em raiz e extensão
# os.path.getsize -> recebe o caminho para um arquivo e retorna o tamanho do arquivo, em bytes, se existir

# DICA IMPORTANTE: Como strings são iteráveis, pode-se procurar uma substring com a palavra-chave in


def converter_tamanho(tamanho, base=2**10):
    sufixo = 'B'
    if tamanho > base:
        tamanho /= base
        sufixo = 'KiB'
    if tamanho > base**2:
        tamanho /= base**2
        sufixo = 'MiB'
    if tamanho > base**3:
        tamanho /= base**3
        sufixo = 'GiB'

    return f'{round(tamanho,2)} {sufixo}'


def print_file_info_from_dict(info_dict):
    print()
    arquivo, outras_info = info_dict.pop('arquivo'), info_dict
    print('Encontrei o arquivo', arquivo)
    for key, value in outras_info.items():
        print(f'{key.capitalize()}:', value)


def main():

    caminho_base = input('Digite um caminho: ')
    termo_procurado = input('Digite o termo de busca: ')

    contador = 0
    for diretorio, _, arquivos in os.walk(
            os.path.expandvars(os.path.expanduser(caminho_base))):
        for arquivo in arquivos:
            if termo_procurado in arquivo:
                try:
                    contador += 1
                    caminho_completo = os.path.join(diretorio, arquivo)
                    nome_arquivo, extensao = os.path.splitext(arquivo)
                    tamanho = os.path.getsize(caminho_completo)
                    info = {
                        'arquivo': arquivo,
                        'nome do arquivo': nome_arquivo,
                        'caminho': caminho_completo,
                        'extensão': extensao,
                        'tamanho': converter_tamanho(tamanho),
                        'tamanho em bytes': tamanho
                    }
                    print_file_info_from_dict(info)
                except PermissionError:
                    print('Você não ter permissão para ler esse arquivo')
                except FileNotFoundError:
                    print('Arquivo não encontrado')
                except Exception as e:
                    print('Erro desconhecido', e)

    print('---------------------------')
    print(f'Achou {contador} arquivos')


if __name__ == "__main__":
    main()
