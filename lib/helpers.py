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
    event_date = input("Enter event date: ")
    client_id = input("Enter client ID: ")
    animal_id = input("Enter animal ID: ")
    try:
        new_event = Client_Animal.create(event_date, int(client_id), int(animal_id))
        print(f"Event created: {new_event}")
    except Exception as exc:
        print("Error creating event: ", exc)

def find_event_by_id():
    id_ = input("Enter event ID: ")
    event = Client_Animal.find_by_id(id_)
    print(event) if event else print(f"Event {id_} not found")

def delete_event():
    id_ = input("Enter event ID: ")
    if event := Client_Animal.find_by_id(id_):
        event.delete()
        print(f"Event {id_} deleted")
    else:
        print(f"Event {id_} not found")

def display_all_events():
    events = Client_Animal.view_all()
    for event in events:
        print(event)

def event_by_date():
    date = input("Enter date: ")
    try:
        events = Client_Animal.find_by_date(date)
        for event in events:
            print(event)
    except Exception as exc:
        print("Error: ", exc)

def event_by_animal_type():
    type_ = input("Enter animal species: ")
    if events := Client_Animal.find_by_animal_type(type_):
        print([event for event in events])
    else:
        print(f"No events found for animal species: {type_}")

def event_by_client_type():
    type_ = input("Enter client type: ")
    if events := Client_Animal.find_by_client_type(type_):
        print([event for event in events])
    else:
        print(f"No events found for client type: {type_}")

def show_available_animals():
    date = input("Enter date: ")
    try:
        if animals := Client_Animal.available_animals(date):
            for animal in animals:
                print(animal)
        else:
            print(f"No animals available on {date}")
    except Exception as exc:
        print("Error: ", exc)


def exit_program():
    print("Goodbye!")
    exit()
