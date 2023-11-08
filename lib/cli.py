# lib/cli.py

from termcolor import colored

from helpers import (
    create_client,
    find_client_by_id,
    delete_client,
    client_by_name,
    display_all_clients,
    all_clients_by_type,
    client_animals,
    create_animal,
    find_animal_by_id,
    delete_animal,
    display_all_animals,
    find_animal_by_species,
    find_animal_by_name,
    animal_clients,
    create_event,
    event_details_by_id,
    delete_event,
    display_all_events,
    event_by_date,
    event_by_animal_type,
    event_by_client_type,
    show_available_animals,
    exit_program
)


def home():
    while True:
        print()
        print(colored("THE DOG AND PONY SHOW", color="blue"))
        print(colored("***Home Menu***", color="blue"))
        print()
        home_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            client()
        elif choice == "2":
            animal()
        elif choice == "3":
            event()
        else:
            print("Invalid choice")


def home_menu():
    print("Please select an option:")
    print("1. Go to Client Menu")
    print("2. Go to Animal Menu")
    print("3. Go to Event Menu")
    print("0. Exit the program")
    print()


def client():
    while True:
        print()
        print(colored("***Client Menu***", color="blue"))
        print()
        client_menu()
        choice = input("> ")
        if choice == "0":
            break
            home_menu()
        elif choice == "1":
            create_client()
        elif choice == "2":
            find_client_by_id()
        elif choice == "3":
            delete_client()
        elif choice == "4":
            client_by_name()
        elif choice == "5":
            display_all_clients()
        elif choice == "6":
            all_clients_by_type()
        elif choice == "7":
            client_animals()
        else:
            print("Invalid choice")

def client_menu():
    print("Please select an option:")
    print("1. Create a client")
    print("2. Find client by ID")
    print("3. Delete client")
    print("4. Find client by name")
    print("5. Display all clients")
    print("6. Find client by event type")
    print("7. Show all animals rented by a client")
    print("0. Return to Home Menu")
    print()


def animal():
    while True:
        print()
        print(colored("***Animal Menu***", color="blue"))
        print()    
        animal_menu()
        choice = input("> ")
        if choice == "0":
            break
            home_menu()   
        elif choice == "1":
            create_animal()
        elif choice == "2":
            find_animal_by_id()
        elif choice == "3":
            delete_animal()
        elif choice == "4":
            display_all_animals()
        elif choice == "5":
            find_animal_by_species()
        elif choice == "6":
            find_animal_by_name()
        elif choice == "7":
            animal_clients()    
        else:
            print("Invalid choice")

def animal_menu():
    print("Please select an option:")
    print("1. Create animal")
    print("2. Find animal by ID")
    print("3. Delete animal")
    print("4. Display all animals")
    print("5. Show animals by species")
    print("6. Find animal by name")
    print("7. Show all clients of an animal")
    print("0. Return to Home Menu")
    print()


def event():
    while True:
        print()
        print(colored("***Event Menu***", color="blue"))
        print()
        event_menu()
        choice = input("> ")
        if choice == "0":
            break
            home_menu()    
        elif choice == "1":
            create_event()
        elif choice == "2":
            event_details_by_id()
        elif choice == "3":
            delete_event()
        elif choice == "4":
            display_all_events()
        elif choice == "5":
            event_by_date()
        elif choice == "6":
            event_by_animal_type()
        elif choice == "7":
            event_by_client_type()
        elif choice == "8":
            show_available_animals()        
        else:
            print("Invalid choice")

def event_menu():
    print("Please select an option:")
    print("1. Create event")
    print("2. Show event details by event ID")
    print("3. Delete event")
    print("4. Display all events")
    print("5. Show events on a date")
    print("6. Show events by animal type")
    print("7. Show events by event type")
    print("8. Show animals available on date")
    print("0. Return to Home Menu")
    print()



if __name__ == "__main__":
    home()
