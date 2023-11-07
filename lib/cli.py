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
    exit_program,
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
