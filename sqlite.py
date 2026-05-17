import sqlite3
import json

connection = sqlite3.connect("/home/romeo/Octopus_Tech_Test/locations.db")

cursor = connection.cursor()

cursor.execute( """create table if not exists locations(
    ID integer primary key autoincrement,
    lat real,
    lon real,
    operator_reference text,
    country_reference text,
    postal_code text,
    number_of_evses integer)
    """)
    

cursor.execute( """create table if not exists eves(
    ID integer primary key autoincrement,
    physical_identifer text,
    status text)
    """)

cursor.execute( """create table if not exists connectors(
    ID integer primary key autoincrement,

    standard text,
    power integer)
    """)

connection.commit()
connection.close()



with open('data/integrated.json') as f:
    locations = json.load(f)
    print(locations)
    
    