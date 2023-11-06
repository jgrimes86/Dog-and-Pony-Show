#!/usr/bin/env python3
# lib/debug.py

from models.config import CONN, CURSOR
from models.animal import Animal
import ipdb

Animal.drop_table()
Animal.create_table()

animal1= Animal.create('Fido', 'Dog', 'Golden Retriever', 'Jumping')
animal2= Animal.create('Rover', 'Dog', 'Dalmation', 'Sleeping')
animal3= Animal.create('Lucky', 'Pony', 'Shetland', 'Trotting')

ipdb.set_trace()
