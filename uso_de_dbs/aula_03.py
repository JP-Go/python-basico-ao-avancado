import pymysql
import pymysql.cursors
import my_secrets as secret
from contextlib import contextmanager


@contextmanager
def connect_to_db():
    con = pymysql.connect(
        host="localhost",
        user=secret.DB_USER,
        password=secret.DB_PASSWORD,
        db=secret.DB_DATABASE,
        charset=secret.DB_CHARSET,
        cursorclass=pymysql.cursors.DictCursor,
    )
    try:
        yield con
    finally:
        print("Closed connection")
        con.close()


# Insert one row
# with connect_to_db() as con:
#     with con.cursor() as cur:
#         sql = (
#             "INSERT INTO clientes (nome,sobrenome,idade,peso)"
#             " VALUES (%s, %s, %s, %s)"
#         )
#         cur.execute(sql, ("Jack", "Bauer", 42, 80.2))
#         con.commit()


# Insert many rows
# with connect_to_db() as con:
#     with con.cursor() as cur:
#         sql = (
#             "INSERT INTO clientes (nome, sobrenome, idade, peso)"
#             "VALUES (%s, %s, %s, %s)"
#         )
#         dados = [
#             ("Mario", "Lima", 12, 32),
#             ("Mario", "Sousa", 19, 56),
#             ("José", "Ricardo", 34, 74),
#         ]
#         cur.executemany(sql, dados)
#         con.commit()

# Delete a row
# with connect_to_db() as con:
#     with con.cursor() as cur:
#         sql = "DELETE FROM clientes WHERE id = %s"
#         cur.execute(sql, (6,))
#         con.commit()

# Delete every row in a sequence of id values
# with connect_to_db() as con:
#     with con.cursor() as cur:
#         sql = "DELETE FROM clientes WHERE id IN (%s, %s, %s)"
#         cur.execute(sql, (7, 8, 9))
#         con.commit()

# Delete every row in a range of values (between)
# with connect_to_db() as con:
#     with con.cursor() as cur:
#         sql = "DELETE FROM clientes WHERE id BETWEEN %s AND %s"
#         cur.execute(sql, (10, 12))
#         con.commit()


# Update a register
# with connect_to_db() as con:
#     with con.cursor() as cur:
#         sql = "UPDATE clientes SET nome=%s WHERE id=%s"
#         cur.execute(sql, ("Joana", 5))
#         con.commit()

# Visualize all the rows
with connect_to_db() as con:
    with con.cursor() as cur:
        cur.execute("SELECT * FROM clientes LIMIT 100")
        results = cur.fetchall()
        for row in results:
            print(row)
