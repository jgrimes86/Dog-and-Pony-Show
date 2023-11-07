from animal import Animal
from client import Client
from client_animal import Client_Animal

def seed_database():

    Client_Animal.drop_table()

    Animal.create_table()
    Client.create_table()
    Client_Animal.create_table()

    Animal.create('Fido', 'Dog', 'Golden Retriever', 'Jumping')
    Animal.create('Rover', 'Dog', 'Dalmation', 'Sleeping')

    Client.create('Dewey Chetum & Howe', 'Business', '555-555-5555')

    Client_Animal.create("Nov 14, 2023", 1, 1)

seed_database()

