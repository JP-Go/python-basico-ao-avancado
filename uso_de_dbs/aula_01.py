import sqlite3


def main():
    # Criar uma conexão com a base de dados
    connection = sqlite3.connect("test.db")
    # Criar um cursor, que executa commandos na base de dados
    cursor = connection.cursor()
    # cursor.execute(SQl:string,parameters:Iterable)
    # Executa um comando sql na base de dados
    # cursor.execute(
    #     "CREATE TABLE IF NOT EXISTS clientes ("
    #     "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    #     "name TEXT,"
    #     "peso REAL"
    #     ")"
    # )
    # Não usar, possibilita SQL Injection
    # cursor.execute('INSERT INTO clientes (name,peso) VALUES ("Luiz Otávio",70.4)')
    # cursor.execute('INSERT INTO clientes (name,peso) VALUES (?,?)',("Fracisco Edson",80.5))
    # cursor.execute('INSERT INTO clientes (name,peso) VALUES (:name,:peso)',{"name":"Francisco Edilson", "peso": 88.3})

    # connection.commit(): Salvar alterações na base de dados
    # connection.commit()

    # UPDATE <tabela> SET <campo> = <valor> WHERE <condicao>
    # Atualiza um campo da tabela em que condicao é verdadeira
    # cursor.execute(
    #     "UPDATE clientes SET name=:name WHERE id=:id", {"name": "Daniel", "id": 1}
    # )

    # DELETE FROM <tabela> WHERE condicao
    # Apaga um campo da tabela onde condicao é verdadeira

    cursor.execute("DELETE FROM clientes WHERE id=:id", {"id": 3})

    # Salva os dados
    connection.commit()
    # cursor.execute("SELECT <campos> FROM <tabela> [WHERE condicao]"):
    # Dá ao cursor o resultado de um
    cursor.execute("SELECT name,peso FROM clientes WHERE peso > :peso", {"peso": 72})

    # Cursor.fetchall(): Devolve ao python os dados armazenados no cursor.
    for line in cursor.fetchall():
        print(line)
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
