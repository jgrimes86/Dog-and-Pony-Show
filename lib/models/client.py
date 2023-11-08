from models.config import CONN, CURSOR

class Client:

    def __init__(self, name, type, phone_number, id= None):
        self.name= name
        self.type= type
        self.phone_number= phone_number
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if type(name) == str:
            self._name = name
        else:
            raise TypeError("Name must be a string")
        
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        if isinstance(type, str):
            if type in ["Corporate Seminar", "Team-Building Event", "Birthday Party"]:
                self._type= type
            else:
                raise ValueError("Event type has 3 options: Corporate Seminar, Team-Building Event, and Birthday Party")
        else:
            raise TypeError("Event type needs to be a string")
        
    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, phone_number):
        if type(phone_number) == str:
            if len(phone_number) == 12:
                self._phone_number= phone_number
            else:
                raise ValueError("Required phone number format: xxx-xxx-xxxx")
        else:
            raise TypeError("Phone number must be a string")
                        

    def __repr__(self):
        return f"Client {self.id}: {self.name}" 

    @classmethod
    def create_table(cls):
        sql= """
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY, 
            name TEXT,
            type TEXT,
            phone_number TEXT
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql= "DROP TABLE clients;"
        CURSOR.execute(sql)
        CONN.commit() 

    def save(self):
        sql= """
        INSERT INTO clients (name, type, phone_number) VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.type, self.phone_number))
        CONN.commit()
        self.id= CURSOR.lastrowid

    @classmethod
    def create(cls, name, type, phone_number):
        client= cls(name, type, phone_number)
        client.save()
        return client 
    
    def delete(self):
        sql= "DELETE FROM clients WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id= None

    @classmethod
    def from_db(cls, row):
        client_instance= Client(row[1], row[2], row[3])
        client_instance.id= row[0]
        return client_instance

    @classmethod
    def find_by_name(cls,name):
        query = "SELECT * FROM clients WHERE name is ?"
        result = CURSOR.execute(query,(name,)).fetchone()
        if result:
            return cls.from_db(result)
        else:
            return None
    
    @classmethod
    def display_all_clients(cls):
        rows = CURSOR.execute("SELECT * FROM clients" ).fetchall()
        return [cls.from_db(row) for row in rows]  

    @classmethod
    def view_by_type(cls, type):  
        rows = CURSOR.execute("SELECT * FROM clients WHERE type is ?", (type,)).fetchall()
        return [cls.from_db(row) for row in rows] 
    

    @classmethod
    def find_by_id(cls, id):
        sql= "SELECT * FROM clients WHERE id= ?"
        row= CURSOR.execute(sql, (id,)).fetchone()
        return cls.from_db(row) if row else None
    
    def animals(self):
        from models.animal import Animal 
        sql= """
        SELECT DISTINCT animals.* FROM animals
        JOIN client_animals ON client_animals.animal_id= animals.id
        WHERE client_animals.client_id= ?
        """
        rows= CURSOR.execute(sql, (self.id,)).fetchall()
        return [Animal.from_db(row) for row in rows]
    
    


