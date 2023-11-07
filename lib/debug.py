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
animal2= Animal.create('Rover', 'Dog', 'Dalmation', 'Sleeping')
animal3= Animal.create('Lucky', 'Pony', 'Shetland', 'Trotting') 

client1= Client.create('Dewey Chetum & Howe', 'Business', '555-555-5555')
client2= Client.create('LeBron James', 'Personal', '216-465-2306')

event1= Client_Animal.create("Nov 14, 2023", 1, 1)
event2= Client_Animal.create("Jun 03, 2024", 2, 1)

ipdb.set_trace()
