# lib/helpers.py
from models.animal import Animal
from models.client import Client
from models.client_animal import Client_Animal

import sqlite3

def create_client(name,client_type,contact_info):
    new_client = Client.create(name, client_type, contact_info)
    return new_client
    

def find_client_by_id():
    id_= input("Enter client ID: ")
    client= Client.find_by_id(id_)
    print(client) if client else print(f"Client {id_} not found")

def delete_client():
    id_=input("Enter client ID:")
    client= Client.find_by_id(id_)
    if client:
        client.delete()
        print(f"Client{id_} deleted successfully")
    else: 
        print(f"Client{id_} deletion failed")
   

def client_by_name():
    name = input("Enter client name: ")
    clients = Client.find_by_name(name)
    if clients:
        for client in clients:
            print(client)
    else:
        print(f"No clients found with the name{name}.")

    

def display_all_clients():
    clients = Client.display_all_clients()
    if clients:
        for client in clients:
            print(client)
        else:
            print("no clients found.")
    

def all_clients_by_type(client_type):
    return Client.view_by_type(client_type)

    

def client_animals():
    pass
 

def create_animal():
    pass

def find_animal_by_id():
    pass

def delete_animal():
    pass

def display_all_animals():
    pass

def find_animal_by_species():
    pass

def find_animal_by_name():
    pass

def animal_clients():
    pass


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
