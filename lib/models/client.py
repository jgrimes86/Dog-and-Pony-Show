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
    
# ipdb.set_trace()