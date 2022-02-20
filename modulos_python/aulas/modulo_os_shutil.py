import os
import shutil

BASE = '~/code/testing/test_fmt/'
DESTINO = '~/code/arquivo/hello_world_rust'

caminho_base = BASE
caminho_novo = DESTINO


def main():
    try:
        os.mkdir(os.path.expanduser(caminho_novo))
    except FileExistsError:
        print(f'Arquivo {caminho_novo} já existe.')

    for root, _, files in os.walk(os.path.expanduser(caminho_base)):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(os.path.expanduser(caminho_novo),
                                         file)

            if '.rs' in file:
                print(f"Movendo arquivo {file} para {new_file_path}.")
                shutil.move(old_file_path, new_file_path)


if __name__ == "__main__":
    main()
