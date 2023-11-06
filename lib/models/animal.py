from models.config import CONN, CURSOR
import ipdb

class Animal:

    def __init__(self, name, species, breed, skill):
        self.name= name
        self.species= species
        self.breed= breed
        self.skill= skill

    def __repr__(self):
        return f"Animal: {name}, the {species}"

    @classmethod
    def create_table(cls):
        sql= """
        CREATE TABLE IF NOT EXISTS animals (
            id INTEGER PRIMARY KEY, 
            name TEXT,
            species TEXT,
            breed TEXT,
            skill TEXT
        )
         """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql= """
        INSERT INTO animals (name, species, breed, skill) VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.species, self.breed, self.skill))
        CONN.commit()
        # self.id= CURSOR.lastrowid

    @classmethod
    def create(cls, name, species, breed, skill):
        animal= cls(name, species, breed, skill)
        animal.save()
        return animal
    
# ipdb.set_trace()