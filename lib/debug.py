#!/usr/bin/env python3
# lib/debug.py

from models.config import CONN, CURSOR
from models.animal import Animal
from models.client import Client
from models.client_animal import Client_Animal
from helpers import *
import ipdb

Animal.drop_table()
Animal.create_table()
Client.drop_table()
Client.create_table()
Client_Animal.drop_table()
Client_Animal.create_table()


animal1= Animal.create('Fido', 'Dog', 'Golden Retriever', 'Jumping')
animal2= Animal.create('Rover', 'Dog', 'Dalmation', 'Barking at fire')
animal3= Animal.create('Lucky', 'Pony', 'Shetland', 'Trotting')
animal4= Animal.create('Paige', 'Pony', 'Appaloosa', 'Dancing') 
animal5= Animal.create('Max', 'Dog', 'Poodle', 'Sleeping')
animal6= Animal.create("Mr. Ed", 'Pony', 'Miniature Horse', 'Talking')

client1= Client.create('Dewey Chetum & Howe', 'Corporate Seminar', '555-555-5555')
client2= Client.create('LeBron James', 'Birthday Party', '216-465-2306')
client3= Client.create('ACME Corporation', 'Corporate Seminar', '888-293-1948')
client4= Client.create('Calvin Coolidge', 'Birthday Party', '555-104-3582')
client5= Client.create('Republic Citizens Finance', "Team-Building Event", '800-205-1948')

event1= Client_Animal.create("November 14, 2023", 1, 1)
event2= Client_Animal.create("June 03, 2024", 2, 1)
event3= Client_Animal.create("December 25, 2024", 2, 3)
event4= Client_Animal.create("July 08, 2024", 4, 5)
event5= Client_Animal.create("July 08, 2024", 5, 6)

ipdb.set_trace()
