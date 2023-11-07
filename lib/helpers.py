# lib/helpers.py
from models.animal import Animal
from models.client import Client
from models.client_animal import Client_Animal

import sqlite3

def create_client():
    pass

def find_client_by_id():
    id_= input("Enter client ID: ")
    client= Client.find_by_id(id_)
    print(client) if client else print(f"Client {id_} not found")

def delete_client():
    pass

def client_by_name():
    pass

def display_all_clients():
    pass

def all_clients_by_type():
    pass

def client_animals():
    pass
 

def create_animal():
    name= input("Enter the animal's name: ")
    species= input("Enter the animal's species: ")
    breed= input("Enter the animal's breed: ")
    skill= input("Enter the animal's skill: ")
    try:
        animal= Animal.create(name, species, breed, skill)
        print(f"Success: {animal}")
    except Exception as exc:
        print("Error creating animal: ", exc)


def find_animal_by_id():
    id_= input("Enter animal ID: ")
    animal= Animal.find_by_id(id_)
    print(animal) if animal else print(f"Animal {id_} not found")

def delete_animal():
    id_= input("Enter animal's ID: ")
    if animal := Animal.find_by_id(id_):
        animal.delete()
        print(f'Animal {id_} deleted')
    else:
        print(f'Animal {id_} not found')


def display_all_animals():
    animals= Animal.all()
    for animal in animals:
        print(animal)

def find_animal_by_species():
    species= input("Enter animal species: ")
    animal= Animal.find_by_species(species)
    print(animal) if animal else print(f"There are no animals with the species {species}")

def find_animal_by_name():
    name= input("Enter animal name: ")
    animal= Animal.find_by_name(name)
    print(animal) if animal else print(f"Animal {name} not found")

def animal_clients():
    name= input("Enter animal name: ")
    animal= Animal.find_by_name(name)
    for client in animal.clients():
        print(client)


def create_event():
    pass

def find_event_by_id():
    pass

def delete_event():
    pass

def display_all_events():
    pass

def event_by_date():
    pass

def event_by_animal_type():
    pass

def event_by_client_type():
    pass

def show_available_animals():
    pass


def exit_program():
    print("Goodbye!")
    exit()
