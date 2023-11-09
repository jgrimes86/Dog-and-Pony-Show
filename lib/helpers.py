# lib/helpers.py
from models.animal import Animal
from models.client import Client
from models.client_animal import Client_Animal

from InquirerPy import inquirer, prompt, get_style
from InquirerPy.base.control import Choice

from termcolor import colored

def create_client():
    print("Type 'exit' to return to Client Menu")
    name = inquirer.text(message= "Enter the client's name: ").execute()
    if name != "exit":
        type= inquirer.select(
            message= "Select client's event type",
            choices= [
                "Corporate Seminar",
                "Team-Building Event",
                "Birthday Party",
                Choice(value=None, name="Return to Client Menu"),
            ],
            default= "Corporate Seminar"
        ).execute()
        if type != None:
            print("Type 'exit' to return to Client Menu")
            print("Required phone number format: xxx-xxx-xxxx ")
            phone_number = inquirer.text(message="Enter the client's phone number: ").execute()
            if phone_number != "exit":
                try:
                    client= Client.create(name, type, phone_number)
                    print(colored(f"Success: {client} has been created", color="green"))
                except Exception as exc:
                    print("Error creating client: ", exc)
    

def find_client_by_id():
    print("Type 'exit' to return to Client Menu")
    id_ = inquirer.text(message= "Enter client ID: ").execute()
    if id_ != "exit":
        client= Client.find_by_id(id_)
        if client: 
            print(colored(f"Client {client.id}: {client.name}. Event Type: {client.type}; Phone Number: {client.phone_number}", color="green"))
        else: 
            print(f"There is no client with an ID of {id_}")


def delete_client():
    print("Type 'exit' to return to Client Menu")
    id_ = inquirer.text(message="Enter client ID: ").execute()
    if id_ != "exit":
        if client := Client.find_by_id(id_):
            client.delete()
            print(colored(f'Client {id_} deleted', color="green"))
        else:
            print(f'There is no client with an ID of {id_}')
   
def client_by_name():
    print("Type 'exit' to return to Client Menu")
    name = inquirer.text(message= "Enter client name: ").execute()
    if name != "exit":
        client = Client.find_by_name(name)
        if client:
            print(colored(f"Client {client.id}: {client.name}. Event Type: {client.type}; Phone Number: {client.phone_number}", color="green"))
        else:
            print(f"There is no client with the name of {name}")


def display_all_clients():
    clients = Client.display_all_clients()
    for client in clients:
        print(colored(f"{client}", color="green"))


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
                print(colored(f"{client}", color="green"))
        else:
            print("No clients have that event type")
    

def client_animals():
    print("Type 'exit' to return to Client Menu")
    id_ = inquirer.text(message= "Enter client ID: ").execute()
    if id_ != "exit":
        client= Client.find_by_id(id_)
        if client:
            animals= client.animals()
            if animals:
                for animal in animals:
                    print(colored(f"{animal}", color="green"))
            else:
                print(f"{client.name} hasn't reserved any animals yet.")
        else:
            print(f"There is no animal with an ID of {id_}")


def create_animal():
    print("Type 'exit' to return to Animal Menu")
    name = inquirer.text(message="Enter the animal's name: ").execute()
    if name != "exit":
        species= inquirer.select(
            message= "Select animal's species",
            choices= [
                "Dog",
                "Pony",
                Choice(value=None, name="Return to Animal Menu")
            ],
            default= 'Dog'
        ).execute()
        if species != None:
            print("Type 'exit' to return to Animal Menu")
            breed = inquirer.text(message="Enter the animal's breed: ").execute()
            if breed != "exit":
                print("Type 'exit' to return to Event Menu")
                skill = inquirer.text(message="Enter the animal's skill: ").execute()
                if skill != "exit":
                    try:
                        animal= Animal.create(name, species, breed, skill)
                        print(colored(f"Success: {animal} has been created", color="green"))
                    except Exception as exc:
                        print("Error creating animal: ", exc)


def find_animal_by_id():
    print("Type 'exit' to return to Animal Menu")
    id_ = inquirer.text(message="Enter the animal's ID: ").execute()
    if id_ != "exit":
        animal= Animal.find_by_id(id_)
        print(colored(f"Name: {animal.name}  Species: {animal.species}  Breed: {animal.breed}  Skill: {animal.skill}", color="green")) if animal else print(f"There is no animal with an ID of {id_}")

def delete_animal():
    print("Type 'exit' to return to Animal Menu")
    id_ = inquirer.text(message="Enter the animal's ID: ").execute()
    if id_ != "exit":
        if animal := Animal.find_by_id(id_):
            animal.delete()
            print(colored(f'Animal {id_} deleted', color="green"))
        else:
            print(f'There is no animal with an ID of {id_}')

def display_all_animals():
    animals= Animal.all()
    for animal in animals:
        print(colored(f"{animal}", color="green"))

def find_animal_by_species():
    species= inquirer.select(
        message= "Select animal type",
        choices= [
            "Dog",
            "Pony",
            Choice(value=None, name="Return to Animal Menu")
        ],
        default = "Dog"
    ).execute()
    if species != None:
        animals= Animal.find_by_species(species)
        if animals:
            for animal in animals:
                print(colored(f"{animal}", color="green"))
        else:
            print('No aminals have that species')

def find_animal_by_name():
    print("Type 'exit' to return to Animal Menu")
    name = inquirer.text(message="Enter animal name: ").execute()
    if name != "exit":
        try:
            if animal := Animal.find_by_name(name):
                print(colored(f"{animal}", color="green"))
        except:
            print(f"There is no animal with the name of {name}")

def animal_clients():
    print("Type 'exit' to return to Animal Menu")
    id_ = inquirer.text(message="Enter animal ID: ").execute()
    if id_ != "exit":
        animal= Animal.find_by_id(id_)
        if animal:
            clients = animal.clients()
            if clients:
                for client in clients:
                    print(colored(f"{client}", color="green"))
            else:
                print(f"{animal.name} doesn't currently have any clients")
        else:
            print(f"There is no animal with an ID of {id_}")


def create_event():
    print("Type 'exit' to return to Event Menu")
    print("Date must match the format of November 06, 2023")
    event_date = inquirer.text(message="Enter event date: ").execute()
    if event_date != "exit":
        client_id = inquirer.text(message="Enter client ID: ").execute()
        if client_id != "exit":
            animal_id = inquirer.text(message="Enter animal ID: ").execute()
            if animal_id != "exit":
                try:
                    new_event = Client_Animal.create(event_date, int(client_id), int(animal_id))
                    print(colored(f"Event created: {new_event}", color="green"))
                except Exception as exc:
                    print("Error creating event: ", exc)

def event_details_by_id():
    print("Type 'exit' to return to Event Menu")
    id_ = inquirer.text(message="Enter event ID: ").execute()
    if id_ != "exit":
        row = Client_Animal.show_event_details(id_)
        if row:
            pass
            print(colored(f"Event {row[0]}: {row[1]}, {row[2]} performs at a {row[4]} for {row[3]}", color="green"))
        else:
            print(f"Event {id_} not found")

def delete_event():
    print("Type 'exit' to return to Event Menu")
    id_ = inquirer.text(message="Enter event ID: ").execute()
    if id_ != "exit":
        if event := Client_Animal.find_by_id(id_):
            event.delete()
            print(colored(f"Event {id_} deleted", color="green"))
        else:
            print(f"Event {id_} not found")

def display_all_events():
    events = Client_Animal.view_all()
    for event in events:
        print(colored(f"{event}", color="green"))

def event_by_date():
    print("Type 'exit' to return to Event Menu")
    date = inquirer.text(message="Enter date: ").execute()
    if date != "exit":
        try:
            events = Client_Animal.find_by_date(date)
            for event in events:
                print(colored(f"{event}", color="green"))
        except Exception as exc:
            print("Error: ", exc)

def event_by_animal_type():
    species = inquirer.select(
        message = "Select animal type",
        choices = [
            "Dog",
            "Pony",
            Choice(value=None, name="Return to Event Menu"),
        ],
        default = "Dog",
    ).execute()
    if species != None:
        if events := Client_Animal.find_by_animal_type(species):
            for event in events:
                print(colored(f"{event}", color="green"))
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
                print(colored(f"{event}", color="green"))
        else:
            print(f"No events found for client event type: {event_type}")

def show_available_animals():
    print("Type 'exit' to return to Event Menu")
    date = inquirer.text(message="Enter date: ").execute()
    if date != "exit":
        try:
            if rows := Client_Animal.available_animals(date):
                for row in rows:
                    print(colored(f"Animal {row[0]}: {row[1]}, a {row[2]} who is good at {row[4]}", color="green"))
            else:
                print(f"No animals available on {date}")
        except Exception as exc:
            print("Error: ", exc)


def exit_program():
    print("Goodbye!")
    exit()
