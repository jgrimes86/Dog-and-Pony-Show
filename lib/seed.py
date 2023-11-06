#!/usr/bin/env python3

from models.config import CONN, CURSOR
from models.animal import Animal
from models.client import Client

def seed_database():
    Animal.create_table()
    Client.create_table()
    animal1= Animal.create('Fido', 'Dog', 'Golden Retriever', 'Jumping')
    animal2= Animal.create('Rover', 'Dog', 'Dalmation', 'Sleeping')
    animal3= Animal.create('Lucky', 'Pony', 'Shetland', 'Trotting')
    Client.create('Dewey Chetum & Howe', 'Business', '555-555-5555')

seed_database()