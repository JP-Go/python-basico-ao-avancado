import sqlite3

def main():
    connection = sqlite3.connect("test.db")
    connection.close()


if __name__ == "__main__":
    main()
