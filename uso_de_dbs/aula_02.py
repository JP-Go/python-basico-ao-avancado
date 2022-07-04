import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def insert_contact(self, name: str, phone: str):
        sql_command = "INSERT OR IGNORE INTO agenda (name,phone) VALUES (?,?)"
        self.cursor.execute(sql_command, (name, phone))
        self.conn.commit()

    def edit_contact(self, new_name: str, new_phone: str, id: int):
        sql_command = "UPDATE OR IGNORE agenda SET name=?, phone=? WHERE id=?"
        self.cursor.execute(sql_command, (new_name, new_phone, id))
        self.conn.commit()

    def delete_contact(self, id):
        sql_command = "DELETE FROM agenda WHERE id=?"
        self.cursor.execute(sql_command, (id,))
        self.conn.commit()

    def list_contacts(self):
        sql_command = "SELECT * FROM agenda"
        self.cursor.execute(sql_command)
        for row in self.cursor.fetchall():
            id, name, phone = row
            print(f"id: {id}, name:{name}, phone number: {phone}")

    def search_contact_by_name(self, name):
        sql_command = "SELECT * FROM agenda WHERE name LIKE ?"
        self.cursor.execute(sql_command, (f"%{name}%",))
        for line in self.cursor.fetchall():
            print(line)

    def search_contact_by_phone(self, phone):
        sql_command = "SELECT * FROM agenda WHERE phone LIKE ?"
        self.cursor.execute(sql_command, (f"%{phone}%",))
        for line in self.cursor.fetchall():
            print(line)

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    agenda = AgendaDB("agenda.db")
    agenda.search_contact_by_name("Luiz")
