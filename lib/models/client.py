from models.config import CONN, CURSOR
import ipdb

class Client:

    def __init__(self, name, type, contact_info):
        self.name= name
        self.type= type
        self.contact_info= contact_info

    @classmethod
    def create_table(cls):
        sql= """
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY, 
            name TEXT,
            type TEXT,
            contact_info TEXT
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql= """
        INSERT INTO clients (name, type, contact_info) VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.type, self.contact_info))
        CONN.commit()
        # self.id= CURSOR.lastrowid

    @classmethod
    def create(cls, name, type, contact_info):
        client= cls(name, type, contact_info)
        client.save()
        return client 
    
    @classmethod
    def delete(cls, client_id):
        sql= "DELETE FROM clients WHERE id = ?"
        CURSOR.execute(sql,(client_id,))
        CONN.commit()

    @classmethod
    def find_by_name(cls,name):
        query = "SELECT * FROM clients WHERE name is ?"
        result = CURSOR.execute(query,(name,)).fetchone()
        if result:
            
            return (result)
        else:
            return None
    
    @classmethod
    def display_all_clients(cursor):
        cursor.execute("SELECT * FROM clients" )
        rows = cursor.fetchall()

        if len(rows) == 0:
            print("no clients found")
        else:
            print("Clients:")
            for row in rows:
                print(row)    