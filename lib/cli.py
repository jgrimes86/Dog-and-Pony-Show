# lib/cli.py

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
    find_event_by_id,
    delete_event,
    display_all_events,
    event_by_date,
    event_by_animal_type,
    event_by_client_type,
    show_available_animals,
    exit_program
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
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
        elif choice == "8":
            create_animal()
        elif choice == "9":
            find_animal_by_id()
        elif choice == "10":
            delete_animal()
        elif choice == "11":
            display_all_animals()
        elif choice == "12":
            find_animal_by_species()
        elif choice == "13":
            find_animal_by_name()
        elif choice == "14":
            animal_clients()
        elif choice == "15":
            create_event()
        elif choice == "16":
            find_event_by_id()
        elif choice == "17":
            delete_event()
        elif choice == "18":
            display_all_events()
        elif choice == "19":
            event_by_date()
        elif choice == "20":
            event_by_animal_type()
        elif choice == "21":
            event_by_client_type()
        elif choice == "22":
            show_available_animals()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("1. Create a client")
    print("2. Find client by ID")
    print("3. Delete client")
    print("4. Find client by name")
    print("5. Display all clients")
    print("6. Find client by type")
    print("7. Show all animals that beling to client")
    print("8. Create animal")
    print("9. Find animal by ID")
    print("10. Delete animal")
    print("11. Display all animals")
    print("12. Show animals by species")
    print("13. Find animal by name")
    print("14. Show all clients of an animal")
    print("15. Create event")
    print("16. Find event by ID")
    print("17. Delete event")
    print("18. Display all events")
    print("19. Show events on a date")
    print("20. Show events by animal type")
    print("21. Show events by client type")
    print("22. Show animals available on date")
    print("0. Exit the program")


if __name__ == "__main__":
    main()
