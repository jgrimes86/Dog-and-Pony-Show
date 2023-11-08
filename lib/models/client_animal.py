from models.config import CONN, CURSOR
from models.animal import Animal
from models.client import Client

import ipdb
from datetime import datetime

class Client_Animal:
    
    def __init__(self, event_date, client_id, animal_id, id=None):
        self.event_date = event_date
        self.client_id = client_id
        self.animal_id = animal_id
        self.id = id

    def __repr__(self):
        return f"Event {self.id}: Animal {self.animal_id} performing for Client {self.client_id}"

    @classmethod
    def date_validator(cls, date):
        if datetime.strptime(date, "%b %d, %Y"):
            return True
        else:
            return False

    @property
    def event_date(self):
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        try:
            if Client_Animal.date_validator(event_date):
                self._event_date = event_date
        except ValueError:
            raise ValueError("Date must match the format of Nov 06, 2023")

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        if type(client_id) is int and Client.find_by_id(client_id):
            self._client_id = client_id
        else:
            raise ValueError("Client ID must reference a client in the database")

    @property
    def animal_id(self):
        return self._animal_id

    @animal_id.setter
    def animal_id(self, animal_id):
        if type(animal_id) is int and Animal.find_by_id(animal_id):
            self._animal_id = animal_id
        else:
            raise ValueError("Animal ID must reference an animal in the database")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS client_animals (
                id INTEGER PRIMARY KEY,
                event_date TEXT,
                client_id INTEGER,
                animal_id INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS client_animals
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO client_animals (event_date, client_id, animal_id) VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.event_date, self.client_id, self.animal_id))
        CONN.commit()
        self.id= CURSOR.lastrowid

    @classmethod
    def create(cls, event_date, client_id, animal_id):
        event = cls(event_date, client_id, animal_id)
        event.save()
        return event

    def delete(self):
        sql = """
            DELETE FROM client_animals WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id = None

    @classmethod
    def from_db(self, row):
        return Client_Animal(row[1], row[2], row[3], row[0])

    @classmethod
    def view_all(cls):
        sql = """
            SELECT * FROM client_animals
        """
        events = CURSOR.execute(sql).fetchall()
        return [cls.from_db(row) for row in events]

    @classmethod
    def find_by_date(cls, date):
        try:
            if cls.date_validator(date):
                sql = """
                    SELECT * FROM client_animals WHERE event_date = ?
                """
                if events := CURSOR.execute(sql, (date,)).fetchall():
                    return [cls.from_db(row) for row in events]
                else:
                    raise Exception(f"No events scheduled on {date}")
        except ValueError:
            raise ValueError("Date must match the format of Nov 06, 2023")        

    @classmethod
    def find_by_animal_type(cls, type):
        sql = """
            SELECT client_animals.* FROM client_animals
            INNER JOIN animals
            ON client_animals.animal_id = animals.id
            WHERE animals.species = ?
        """
        events = CURSOR.execute(sql, (type,)).fetchall()
        return [cls.from_db(row) for row in events]

    @classmethod
    def find_by_client_type(cls, type):
        sql = """
            SELECT client_animals.* FROM client_animals
            INNER JOIN clients
            ON client_animals.client_id = clients.id
            WHERE clients.type = ?
        """
        events = CURSOR.execute(sql, (type,)).fetchall()
        return [cls.from_db(row) for row in events]

    @classmethod
    def find_by_id(cls, event_id):
        sql = """
            SELECT client_animals.id, client_animals.event_date, animals.name, clients.name, clients.type
            FROM client_animals
            LEFT JOIN animals
            ON client_animals.animal_id = animals.id
            LEFT JOIN clients
            ON client_animals.client_id = clients.id
            WHERE client_animals.id = ?
        """
        row = CURSOR.execute(sql, (event_id,)).fetchone()
        return row if row else None

    @classmethod
    def available_animals(cls, date):
        # display all animals that are not already booked for an event on a certain date
        try:
            if cls.date_validator(date):
                sql = """
                    SELECT animals.* FROM animals
                    EXCEPT
                    SELECT animals.* FROM animals
                    INNER JOIN client_animals
                    ON animals.id = client_animals.animal_id
                    WHERE (event_date IS ?)
                """
                if animals := CURSOR.execute(sql, (date,)).fetchall():
                    return [row for row in animals]
                else:
                    return None
        except ValueError:
            raise ValueError("Date must match the format of Nov 06, 2023")


# ipdb.set_trace()
