# lib/helpers.py
from models.animal import Animal
from models.client import Client
from models.client_animal import Client_Animal

from InquirerPy import inquirer, prompt, get_style
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

####### PROVIDE OPPORTUNITY TO EXIT INPUT
def create_client():
    name= input("Enter the client's name: ")
    type= inquirer.select(
        message= "Select client's event type",
        choices= [
            "Corporate Seminar",
            "Team-Building Event",
            "Birthday Party",
        ],
        default= "Corporate Seminar"
    ).execute()
    print("Required phone number format: xxx-xxx-xxxx ")
    phone_number= input("Enter the client's phone number: ")
    try:
        client= Client.create(name, type, phone_number)
        print(f"Success: {client} has been created")
    except Exception as exc:
        print("Error creating client: ", exc)
    

def find_client_by_id():
    print("Type 'exit' to return to Event Menu")
    id_ = inquirer.text(message="Enter client ID: ").execute()
    if id_ != "exit":
        client= Client.find_by_id(id_)
        if client: 
            print(f"Client {client.id}: {client.name}. Event Type: {client.type}; Phone Number: {client.phone_number}")
        else: 
            print(f"There is no client with an ID of {id_}")


def delete_client():
    print("Type 'exit' to return to Event Menu")
    id_ = inquirer.text(message="Enter event ID: ").execute()
    if id_ != "exit":
        if client := Client.find_by_id(id_):
            client.delete()
            print(f'Client {id_} deleted')
        else:
            print(f'There is no client with an ID of {id_}')
   
def client_by_name():
    print("Type 'exit' to return to Event Menu")
    name = inquirer.text(message="Enter client name: ").execute()
    if name != "exit":
        client = Client.find_by_name(name)
        if client:
            print(f"Client {client.id}: {client.name}. Event Type: {client.type}; Phone Number: {client.phone_number}")
        else:
            print(f"There is no client with the name of {name}")


def display_all_clients():
    clients = Client.display_all_clients()
    for client in clients:
        print(client)


def all_clients_by_type(): 
    choice = inquirer.select(
        message = "Select client type",
        choices = [
            "Corporate Seminar",
            "Team-Building Event",
            "Birthday Party",
            Choice(value=None, name="Return to Client Menu"),
        ],
        default = "Corporate Seminar"
    ).execute()
    if choice != None:
        clients= Client.view_by_type(choice)
        if clients:
            for client in clients:
                print(client)
        else:
            print("No clients have that event type")
    

def client_animals():
    print("Type 'exit' to return to Event Menu")
    id_ = inquirer.text(message="Enter event ID: ").execute()
    if id_ != "exit":
        client= Client.find_by_id(id_)
        if client:
            animals= client.animals()
            if animals:
                for animal in animals:
                    print(animal)
            else:
                print(f"{client.name} hasn't reserved any animals yet.")
        else:
            print(f"There is no animal with an ID of {id_}")


######### PROVIDE OPPORTUNITY TO EXIT INPUT
def create_animal():
    name= input("Enter the animal's name: ")
    species= inquirer.select(
        message= "Select animal's species",
        choices= [
            "Dog",
            "Pony"
        ],
        default= 'Dog'
    ).execute()
    breed= input("Enter the animal's breed: ")
    skill= input("Enter the animal's skill: ")
    try:
        animal= Animal.create(name, species, breed, skill)
        print(f"Success: {animal} has been created")
    except Exception as exc:
        print("Error creating animal: ", exc)


def find_animal_by_id():
    print("Type 'exit' to return to Event Menu")
    id_ = inquirer.text(message="Enter event ID: ").execute()
    if id_ != "exit":
        animal= Animal.find_by_id(id_)
        print(f"Name: {animal.name}  Species: {animal.species}  Breed: {animal.breed}  Skill: {animal.skill}") if animal else print(f"There is no animal with an ID of {id_}")

def delete_animal():
    print("Type 'exit' to return to Event Menu")
    id_ = inquirer.text(message="Enter event ID: ").execute()
    if id_ != "exit":
        if animal := Animal.find_by_id(id_):
            animal.delete()
            print(f'Animal {id_} deleted')
        else:
            print(f'There is no animal with an ID of {id_}')

def display_all_animals():
    animals= Animal.all()
    for animal in animals:
        print(animal)

def find_animal_by_species():
    species= inquirer.select(
        message= "Select animal type",
        choices= [
            "Dog",
            "Pony",
            Choice(value=None, name="Go Back")
        ],
        default = "Dog"
    ).execute()
    if species != None:
        animals= Animal.find_by_species(species)
        if animals:
            for animal in animals:
                print(animal)
        else:
            print('No aminals have that species')

def find_animal_by_name():
    print("Type 'exit' to return to Event Menu")
    name = inquirer.text(message="Enter animal name: ").execute()
    if name != "exit":
        try:
            if animal := Animal.find_by_name(name):
                print(animal)
        except:
            print(f"There is no animal with the name of {name}")

def animal_clients():
    print("Type 'exit' to return to Event Menu")
    id_ = inquirer.text(message="Enter animal ID: ").execute()
    if id_ != "exit":
        animal= Animal.find_by_id(id_)
        if animal:
            clients = animal.clients()
            if clients:
                for client in clients:
                    print(client)
            else:
                print(f"{animal.name} doesn't currently have any clients")
        else:
            print(f"There is no animal with an ID of {id_}")


def create_event():
    print("Type 'exit' to return to Event Menu")
    event_date = inquirer.text(message="Enter event date: ").execute()
    if event_date != "exit":
        client_id = inquirer.text(message="Enter client ID: ").execute()
        if client_id != "exit":
            animal_id = inquirer.text(message="Enter animal ID: ").execute()
            if animal_id != "exit":
                try:
                    new_event = Client_Animal.create(event_date, int(client_id), int(animal_id))
                    print(f"Event created: {new_event}")
                except Exception as exc:
                    print("Error creating event: ", exc)

def event_details_by_id():
    print("Type 'exit' to return to Event Menu")
    id_ = inquirer.text(message="Enter event ID: ").execute()
    if id_ != "exit":
        row = Client_Animal.show_event_details(id_)
        if row:
            pass
            print(f"Event {row[0]}: {row[1]}, {row[2]} performs at a {row[4]} for {row[3]}")
        else:
            print(f"Event {id_} not found")

def delete_event():
    print("Type 'exit' to return to Event Menu")
    id_ = inquirer.text(message="Enter event ID: ").execute()
    if id_ != "exit":
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
    print("Type 'exit' to return to Event Menu")
    date = inquirer.text(message="Enter date: ").execute()
    if date != "exit":
        try:
            events = Client_Animal.find_by_date(date)
            for event in events:
                print(event)
        except Exception as exc:
            print("Error: ", exc)

# style = get_style({'questionmark': "#e5c07b"})

def event_by_animal_type():
    species = inquirer.select(
        message = "Select animal type",
        choices = [
            "Dog",
            "Pony",
            Choice(value=None, name="Return to Event Menu"),
        ],
        default = "Dog",
        # style = style
    ).execute()
    if species != None:
        if events := Client_Animal.find_by_animal_type(species):
            for event in events:
                print(event)
        else:
            print(f"No events found for animal species: {species}")

def event_by_client_type():
    event_type = inquirer.select(
        message = "Select event type",
        choices = [
            "Corporate Seminar",
            "Team-Building Event",
            "Birthday Party",
            Choice(value=None, name="Return to Event Menu")
        ],
        default = "Corporate Seminar"
    ).execute()
    if event_type != None:
        if events := Client_Animal.find_by_client_type(event_type):
            for event in events:
                print(event)
        else:
            print(f"No events found for client event type: {event_type}")

def show_available_animals():
    print("Type 'exit' to return to Event Menu")
    date = inquirer.text(message="Enter date: ").execute()
    if date != "exit":
        try:
            if rows := Client_Animal.available_animals(date):
                for row in rows:
                    print(f"Animal {row[0]}: {row[1]}, a {row[2]} who is good at {row[4]}")
            else:
                print(f"No animals available on {date}")
        except Exception as exc:
            print("Error: ", exc)


def exit_program():
    print("Goodbye!")
    exit()
