import os
import PyPDF2


def main():

    output_dir = "./output"

    """
    path = os.path.expanduser("~/Fisica-22-1/Ins-ensino-medio/")
    pdfs_to_merge = []
    # Merger: Uma classe que representa um fluxo de bytes que podem ser convertidos para um pdf
    merger = PyPDF2.PdfFileMerger()
    for root, _, files in os.walk(path):
        for file in files:
            if "pdf" in file:
                full_path = os.path.join(root, file)
                pdfs_to_merge.append(full_path)

    # Lembrar: Os aquivos devem ser abertos em modo binário para serem entendidos pelo merger
    file_handlers = [open(pdf, "rb") for pdf in pdfs_to_merge]
    for handler in file_handlers:
        # Merger.append(arquivo ou caminho): Concatena os bytes de arquivo para o fluxo de bytes
        merger.append(handler)

    # abrir um arquivo em modo de escrita de bytes para escrever o fluxo de bytes
    with open(os.path.join(output_dir, "out.pdf"), "wb") as new_pdf:
        # Lembrar: Os arquivos adicionados ao stream de bytes devem estar abertos para que a escrita
        # ocorra com sucesso
        merger.write(new_pdf)

    for file in file_handlers:
        # NÃO DEIXE OS AQUIVOS ABERTOS
        file.close() 
    """

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    # Para ler os dados do arquivo, abrir-lo em modo binario
    with open(os.path.join(output_dir, "out.pdf"), "rb") as pdf:
        # reader(arquivo ou caminho): extrai as informações de arquivo (num de páginas, texto)
        reader = PyPDF2.PdfFileReader(pdf)
        # retorna o número de páginas do pdf
        num_of_pages = reader.getNumPages()
        print(num_of_pages)

        for page_index in range(num_of_pages):
            # writer: Um stream de bytes para serem escritos em um arquivo
            writer = PyPDF2.PdfFileWriter()
            # getPage(índice): retorna o conteúdo da página índice (zero-based)
            page_contents = reader.getPage(page_index)
            # witer.addPage(conteudo): Adiciona conteúdo a uma página do novo pdf a ser gerado pelo writer
            writer.addPage(page_contents)

            with open(
                os.path.join(output_dir, f"pagina-{page_index}.pdf"), "wb"
            ) as page:
                writer.write(page)


if __name__ == "__main__":
    main()
