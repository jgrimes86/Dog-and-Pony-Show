from models.config import CONN, CURSOR
import ipdb

class Animal:

    def __init__(self, name, species, breed, skill, id= None):
        self.name= name
        self.species= species
        self.breed= breed
        self.skill= skill

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str:
            self._name= name
        else:
            raise TypeError('Name must be a string')
    
    @property
    def species(self):
        return self._species
    
    @species.setter
    def species(self, species):
        if not hasattr(self, '_species'):
            if type(species) == str:
                if species == 'Dog' or species == 'dog' or species == 'Pony' or species == 'pony':
                    self._species= species
                else:
                    raise ValueError('Species options: dog, pony')
            else:
                raise TypeError('Species must be a string')
        else:
            raise Exception("Species can't be changed")
    
    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, breed):
        if not hasattr(self, '_breed'):
            if type(breed) == str:
                self._breed= breed
            else:
                raise TypeError('Breed must be a string')
        else:
            raise Exception("Breed can't be changed")
    
    @property
    def skill(self):
        return self._skill
    
    @skill.setter
    def skill(self, skill):
        if type(skill) == str:
            self._skill= skill
        else:
            raise TypeError('Skill must be a string')


    def __repr__(self):
        return f"<Animal {self.id}: {self.name}, the {self.species}>"
    

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
    
    @classmethod
    def drop_table(cls):
        sql= "DROP TABLE animals;"
        CURSOR.execute(sql)
        CONN.commit()


    def save(self):
        sql= """
        INSERT INTO animals (name, species, breed, skill) VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.species, self.breed, self.skill))
        CONN.commit()
        self.id= CURSOR.lastrowid

    # This creates a new Animal instance and also adds the new animal info to a row in the database
    @classmethod
    def create(cls, name, species, breed, skill):
        animal= cls(name, species, breed, skill)
        animal.save()
        return animal
    
    # This deletes a row from the animals table
    def delete(self):
        sql= "DELETE FROM animals WHERE id= ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id= None
    
    # This returns a single animal instance
    @classmethod
    def from_db(cls, row):
        animal_instance= Animal(row[1], row[2], row[3], row[4])
        animal_instance.id= row[0]
        return animal_instance

    # This returns all of the animal instances in a list
    @classmethod
    def all(cls):
        sql= "SELECT * FROM animals"
        rows= CURSOR.execute(sql).fetchall()
        return [cls.from_db(row) for row in rows]
    
    @classmethod
    def find_by_species(cls, species):
        sql= "SELECT * FROM animals WHERE species is ?"
        rows= CURSOR.execute(sql, (species,)).fetchall()
        return [cls.from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        sql= "SELECT * FROM animals WHERE name is ?"
        row= CURSOR.execute(sql, (name,)).fetchone()
        return cls.from_db(row)
    
    @classmethod
    def find_by_id(cls, id):
        sql= "SELECT * FROM animals WHERE id= ?"
        row= CURSOR.execute(sql, (id,)).fetchone()
        return cls.from_db(row) if row else None

    
# ipdb.set_trace()