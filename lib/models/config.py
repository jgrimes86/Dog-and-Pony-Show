import sqlite3

CONN = sqlite3.connect('dog_and_pony.db')
CURSOR = CONN.cursor()
