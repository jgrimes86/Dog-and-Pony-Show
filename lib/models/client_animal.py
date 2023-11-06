# from models.config import CONN, CURSOR
from config import CONN, CURSOR

import ipdb
from datetime import datetime

class Client_Animal:
    
    def __init__(self, event_date, client_id, animal_id, id=None):
        self.event_date = event_date
        self.client_id = client_id
        self.animal_id = animal_id
        self.id = id

    def __repr__(self):
        return f"<Event {self.id}: date = {self.event_date}, client = {self.client_id}, animal = {self.animal_id}>"

    #PROPERTY for validating event_date
    @property
    def event_date(self):
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        try:
            if datetime.strptime(event_date, "%b %d, %Y"):
                self._event_date = event_date
        except ValueError:
            raise ValueError("Date must be in the format of Nov 06, 2023")

    #PROPERTY for validating client_id exists
    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        # VALIDATE USING Client.find_by_id function?
        if type(client_id) is int:
            self._client_id = client_id
        else:
            print(f"Client id {client_id} not found")

    #PROPERTY for validating animal_id exists
    @property
    def animal_id(self):
        return self._animal_id

    @animal_id.setter
    def animal_id(self, animal_id):
        # VALIDATE USING Animal.find_by_id function?
        if type(animal_id) is int:
            self._animal_id = animal_id
        else:
            print(f"Animal id {animal_id} not found")

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
            DROP TABLE client_animals
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO client_animals (event_date, client_id, animal_id) VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.event_date, self.client_id, self.animal_id))
        CONN.commit()

    @classmethod
    def create(cls, event_date, client_id, animal_id):
        event = cls(event_date, client_id, animal_id)
        event.save()
        return event

    @classmethod
    def delete(cls, id):
        sql = """
            DELETE FROM client_animals WHERE id = ?
        """
        CURSOR.execute(sql, (id,))
        CONN.commit()
        print(f"Event {id} deleted")

    @classmethod
    def event_from_row(self, row):
        return Client_Animal(row[1], row[2], row[3], row[0])

    @classmethod
    def view_all(cls):
        sql = """
            SELECT * FROM client_animals
        """
        events = CURSOR.execute(sql).fetchall()
        [print(cls.event_from_row(row)) for row in events]

    @classmethod
    def find_by_date(cls, date):
        sql = """
            SELECT * FROM client_animals WHERE event_date = ?
        """
        if events := CURSOR.execute(sql, (date,)).fetchall():
            [print(cls.event_from_row(row)) for row in events]
        else:
            print(f"No events scheduled on {date}")

    @classmethod
    def find_by_animal_type(cls, type):
        sql = """
            SELECT client_animals.* FROM client_animals
            INNER JOIN animals
            ON client_animals.animal_id = animals.id
            WHERE animals.species = ?
        """
        events = CURSOR.execute(sql, (type,)).fetchall()
        [print(cls.event_from_row(row)) for row in events]


    @classmethod
    def find_by_client_type(cls, type):
        sql = """
            SELECT client_animals.* FROM client_animals
            INNER JOIN clients
            ON client_animals.client_id = clients.id
            WHERE clients.type = ?
        """
        events = CURSOR.execute(sql, (type,)).fetchall()
        [print(cls.event_from_row(row)) for row in events]

    @classmethod
    def event_details(cls, id):
        sql = """
            SELECT client_animals.event_date
            FROM client_animals
            WHERE id = ?
        """
        if event := CURSOR.execute(sql, (id,)).fetchone():
            # get client info from a Client.find_by_id function
            client = None
            # get animal info from an Animal.find_by_id function
            animal = None
            print(f"{event[0]}: {animal} performing at {client}'s event.")
        else:
            print(f"Event {id} not found")

    @classmethod
    def available_animals(cls, date):
        # display all animals that are not already booked for an event on a certain date
        sql = """
            SELECT animals.*, client_animals.*
            FROM animals
            LEFT JOIN client_animals
            ON animals.id = client_animals.animal_id
            WHERE (event_date != ?) OR (event_date IS NULL)
        """
        animals = CURSOR.execute(sql, (date,)).fetchall()
        if animals:
            [print(f"{row[1]} is available") for row in animals]
        else:
            print("No animals available")


ipdb.set_trace()
